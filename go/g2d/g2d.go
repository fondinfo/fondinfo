package g2d

import (
    "crypto/sha1"
    "fmt"
    "math/rand"
    "os"
    "strings"
    "time"
)

type Point struct{ X, Y int }
type Size struct{ W, H int }
type Rect struct{ X, Y, W, H int }
type Color struct{ R, G, B int }

var usrKeydown, usrKeyup func(string)
var usrUpdate func()
var mousePos = Point{0, 0}
var jss = make([]string, 0)
var dialogs = make([]string, 0)
var inited = false
var script = `
window.onload = function(e) { setTimeout("invokeExternal('load')", 100); }
loaded = {};
keyPressed = {};
mouseCodes = ["LeftButton", "MiddleButton", "RightButton"];

function initCanvas(w, h) {
    canvas = document.getElementById("g2d-canvas");
    if (canvas == null) {
        canvas = document.createElement("CANVAS");
        canvas.id = "g2d-canvas";
        document.getElementsByTagName("body")[0].appendChild(canvas);
    }
    canvas.width = w;
    canvas.height = h;
    ctx = canvas.getContext("2d");
    setColor(127, 127, 127);
    clearCanvas();
}
function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
function setColor(r, g, b) {
    ctx.strokeStyle = "rgb("+r+", "+g+", "+b+")";
    ctx.fillStyle = "rgb("+r+", "+g+", "+b+")";
}
function drawLine(x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}
function fillCircle(x, y, r) {
    ctx.beginPath();
    ctx.arc(x, y, r, 0, 2*Math.PI);
    ctx.closePath();
    ctx.fill();
}
function fillRect(x, y, w, h) {
    ctx.fillRect(x, y, w, h);
}
function loadImage(key, src) {
    img = document.createElement("IMG");
    img.src = src;
    loaded[key] = img;
}
function drawImage(key, x, y) {
    img = loaded[key];
    ctx.drawImage(img, x, y);
}
function drawImageClip(key, x0, y0, w0, h0, x1, y1, w1, h1) {
    img = loaded[key];
    ctx.drawImage(img, x0, y0, w0, h0, x1, y1, w1, h1);
}
function drawText(txt, x, y, size) {
    ctx.font = "" + size + "px sans-serif";
    ctx.textBaseline = "top";
    ctx.textAlign = "left";
    ctx.fillText(txt, x, y);
}
function drawTextCentered(txt, x, y, size) {
    ctx.font = "" + size + "px sans-serif";
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillText(txt, x, y);
}
function loadAudio(key, src) {
    audio = document.createElement("AUDIO");
    audio.src = src;
    loaded[key] = audio;
}
function playAudio(key, loop) {
    audio = loaded[key];
    audio.loop = loop;
    audio.play();
}
function pauseAudio(key) {
    audio = loaded[key];
    audio.pause();
}
function doAlert(message) {
    alert(message);
    invokeExternal("dialog true");
}
function doConfirm(message) {
    ans = confirm(message);
    invokeExternal("dialog " + ans);
}
function doPrompt(message) {
    ans = prompt(message, "");
    invokeExternal("dialog " + ans);
}
function fixKey(k) {
    if (k=="Left" || k=="Up" || k=="Right" || k=="Down") k = "Arrow"+k;
    else if (k==" " || k=="Spacebar") k = "Space";
    else if (k=="Esc") k = "Escape";
    else if (k=="Del") k = "Delete";
    return k;
}
function mainLoop(fps) {
    document.onkeydown = function(e) {
        var k = fixKey(e.key);
        if (keyPressed[k]) return;
        keyPressed[k] = true;
        invokeExternal("keydown " + k);
    };
    document.onkeyup = function(e) {
        var k = fixKey(e.key);
        if (keyPressed[k]) keyPressed[k] = false;
        invokeExternal("keyup " + k);
    };
    document.onmousedown = function(e) {
        if (0 <= e.button && e.button < 3) {
            invokeExternal("keydown " + mouseCodes[e.button]);
        }
    };
    document.onmouseup = function(e) {
        if (0 <= e.button && e.button < 3) {
            invokeExternal("keyup " + mouseCodes[e.button]);
        }
    };
    document.onmousemove = function(e) {
        var rect = canvas.getBoundingClientRect();
        var x = Math.round(e.clientX - rect.left);
        var y = Math.round(e.clientY - rect.top);
        invokeExternal("mousemove " + x + " " + y);
    };
    document.onfocus = function(e) {
        keyPressed = {};
    };

    if (typeof timerId !== "undefined") {
        clearInterval(timerId);
        delete timerId;
    }
    if (fps >= 0) {
        timerId = setInterval(function(e) {
            invokeExternal("update");
        }, 1000/fps);
    }
}
function closeCanvas() {
    if (typeof timerId !== "undefined") {
        clearInterval(timerId);
        delete timerId;
    }
    if (typeof canvas !== "undefined") {
        clearCanvas();
        /*canvas.parentNode.removeChild(canvas);
        delete canvas;*/
    }
}
`

func init() {
    rand.Seed(time.Now().UnixNano())
}

func ToInt(text string) int {
    val := 0
    fmt.Sscan(text, &val)
    return val
}

func ToFloat(text string) float64 {
    val := 0.0
    fmt.Sscan(text, &val)
    return val
}

func RandInt(min, max int) int {
    return rand.Intn(max-min+1) + min
}

func SetColor(c Color) {
    doJs("setColor(%d, %d, %d)", c.R, c.G, c.B)
}

func ClearCanvas() {
    doJs("clearCanvas()")
}

func DrawLine(pt1, pt2 Point) {
    doJs("drawLine(%d, %d, %d, %d)", pt1.X, pt1.Y, pt2.X, pt2.Y)
}

func FillCircle(center Point, r int) {
    doJs("fillCircle(%d, %d, %d)", center.X, center.Y, r)
}

func FillRect(r Rect) {
    doJs("fillRect(%d, %d, %d, %d)", r.X, r.Y, r.W, r.H)
}

func LoadImage(src string) string {
    if _, err := os.Stat(src); err != nil {
        src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/" + src
        //fmt.Println(src)
    }
    key := fmt.Sprintf("%x", sha1.Sum([]byte(src)))
    doJs("loadImage('%s', '%s')", key, src)
    return key
}

func DrawImage(image string, p Point) {
    doJs("drawImage('%s', %d, %d)", image, p.X, p.Y)
}

func DrawImageClip(image string, clip Rect, r Rect) {
    doJs("drawImageClip('%s', %d, %d, %d, %d, %d, %d, %d, %d)",
        image, clip.X, clip.Y, clip.W, clip.H, r.X, r.Y, r.W, r.H)
}

func DrawText(txt string, p Point, size int) {
    doJs("drawText('%s', %d, %d, %d)", txt, p.X, p.Y, size)
}

func DrawTextCentered(txt string, p Point, size int) {
    doJs("drawTextCentered('%s', %d, %d, %d)", txt, p.X, p.Y, size)
}

func LoadAudio(src string) string {
    if _, err := os.Stat(src); err != nil {
        src = "https://raw.githubusercontent.com/tomamic/fondinfo/master/examples/" + src
    }
    key := fmt.Sprintf("%x", sha1.Sum([]byte(src)))
    doJs("loadAudio('%s')", key, src)
    return key
}

func PlayAudio(audio string, loop bool) {
    doJs("playAudio('%s', %t)", audio, loop)
}

func PauseAudio(audio string) {
    doJs("pauseAudio('%s')", audio)
}

func HandleEvents(update func(), keyFuncs ...func(string)) {
    usrUpdate, usrKeydown, usrKeyup = update, nil, nil
    if len(keyFuncs) >= 2 {
        usrKeydown, usrKeyup = keyFuncs[0], keyFuncs[1]
    } else if len(keyFuncs) == 1 {
        usrKeydown = keyFuncs[0]
    }
}

func MousePosition() Point {
    return mousePos
}

func UpdateCanvas() {
    if inited {
        code := strings.Join(jss, "")
        //fmt.Println(code)
        evalJs(code)
        jss = make([]string, 0)
    }
}

func MainLoop(fps ...int) {
    fps_ := 60
    if len(fps) > 0 {
        fps_ = fps[0]
    }
    doJs("mainLoop(%d)", fps_)
    UpdateCanvas()
    waitDone()
}

func CloseCanvas() {
    HandleEvents(nil, nil, nil)
    doJs("closeCanvas()")
    UpdateCanvas()
    terminate()
}

func doJs(cmd string, a ...interface{}) {
    jss = append(jss, fmt.Sprintf(cmd+";\n", a...))
}

func handleData(data string) {
    //fmt.Println(data)
    args := strings.Split(data, " ")
    if args[0] == "mousemove" {
        mousePos.X, mousePos.Y = ToInt(args[1]), ToInt(args[2])
    } else if args[0] == "keydown" && usrKeydown != nil {
        usrKeydown(args[1])
        UpdateCanvas()
    } else if args[0] == "keyup" && usrKeyup != nil {
        usrKeyup(args[1])
        UpdateCanvas()
    } else if args[0] == "update" && usrUpdate != nil {
        usrUpdate()
        UpdateCanvas()
    } else if args[0] == "dialog" {
        ans := strings.SplitN(data, " ", 2)[1]
        dialogs = append(dialogs, ans)
    } else if args[0] == "load" {
        inited = true
    }
}