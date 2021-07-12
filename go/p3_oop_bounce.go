package main

import . "g2d"

type Ball struct {
    arena         *Arena
    x, y, w, h    int
    speed, dx, dy int
}

func NewBall(arena *Arena, pos Point) *Ball {
    a := &Ball{arena, pos.X, pos.Y, 20, 20, 5, 5, 5}
    arena.Add(a)
    return a
}

func (a *Ball) Move() {
    as := a.arena.Size()
    if !(0 <= a.x+a.dx && a.x+a.dx <= as.X-a.w) {
        a.dx = -a.dx
    }
    if !(0 <= a.y+a.dy && a.y+a.dy <= as.Y-a.h) {
        a.dy = -a.dy
    }
    a.x += a.dx
    a.y += a.dy
}

func (a *Ball) Position() Point {
    return Point{a.x, a.y}
}

func (a *Ball) Size() Point {
    return Point{a.w, a.h}
}

func (a *Ball) Symbol() Point {
    return Point{0, 0}
}

func (a *Ball) Collide(other Actor) {
    _, ok := other.(*Ghost)
    if !ok {
        op := other.Position()
        if op.X < a.x {
            a.dx = a.speed
        } else {
            a.dx = -a.speed
        }
        if op.Y < a.y {
            a.dy = a.speed
        } else {
            a.dy = -a.speed
        }
    }
}

type Ghost struct {
    arena      *Arena
    x, y, w, h int
    speed      int
    visible    bool
}

func NewGhost(arena *Arena, pos Point) *Ghost {
    a := &Ghost{arena, pos.X, pos.Y, 20, 20, 5, true}
    arena.Add(a)
    return a
}

func (a *Ghost) Move() {
    as := a.arena.Size()
    dx := RandInt(-1, 1) * a.speed
    dy := RandInt(-1, 1) * a.speed
    a.x = (a.x + dx + as.X) % as.X
    a.y = (a.y + dy + as.Y) % as.Y

    if RandInt(0, 99) == 0 {
        a.visible = !a.visible
    }
}

func (a *Ghost) Position() Point {
    return Point{a.x, a.y}
}

func (a *Ghost) Size() Point {
    return Point{a.w, a.h}
}

func (a *Ghost) Symbol() Point {
    if a.visible {
        return Point{20, 0}
    }
    return Point{20, 20}
}

func (a *Ghost) Collide(other Actor) {
}

type Turtle struct {
    arena         *Arena
    x, y, w, h    int
    speed, dx, dy int
}

func NewTurtle(arena *Arena, pos Point) *Turtle {
    a := &Turtle{arena, pos.X, pos.Y, 20, 20, 2, 0, 0}
    arena.Add(a)
    return a
}

func (a *Turtle) Move() {
    as := a.arena.Size()
    a.x += a.dx
    if a.x < 0 {
        a.x = 0
    } else if a.x > as.X-a.w {
        a.x = as.X - a.w
    }
    a.y += a.dy
    if a.y < 0 {
        a.y = 0
    } else if a.y > as.Y-a.h {
        a.y = as.Y - a.h
    }

}

func (a *Turtle) GoLeft(cmd bool) {
    if cmd {
        a.dx = -a.speed
    } else if a.dx < 0 {
        a.dx = 0
    }
}

func (a *Turtle) GoRight(cmd bool) {
    if cmd {
        a.dx = a.speed
    } else if a.dx > 0 {
        a.dx = 0
    }
}

func (a *Turtle) GoUp(cmd bool) {
    if cmd {
        a.dy = -a.speed
    } else if a.dy < 0 {
        a.dy = 0
    }
}

func (a *Turtle) GoDown(cmd bool) {
    if cmd {
        a.dy = a.speed
    } else if a.dy > 0 {
        a.dy = 0
    }
}

func (a *Turtle) Collide(other Actor) {
}

func (a *Turtle) Position() Point {
    return Point{a.x, a.y}
}

func (a *Turtle) Size() Point {
    return Point{a.w, a.h}
}

func (a *Turtle) Symbol() Point {
    return Point{0, 20}
}

/*
type BounceGame struct {
    arena *Arena
    hero  *Turtle
}

func NewBounceGame() *BounceGame {
    a := NewArena(Point{480, 360})
    t := NewTurtle(a, Point{80, 80})
    NewBall(a, Point{40, 80})
    NewBall(a, Point{80, 40})
    NewGhost(a, Point{120, 80})
    return &BounceGame{a, t}
}

func (a *BounceGame) Hero() *Turtle {
    return a.hero
}

func (a *BounceGame) Arena() *Arena {
    return a.arena
}

var game = NewBounceGame()
*/

var arena = NewArena(Point{480, 360})
var hero = NewTurtle(arena, Point{80, 80})
var ball1 = NewBall(arena, Point{40, 80})
var ball2 = NewBall(arena, Point{80, 40})
var ghost = NewGhost(arena, Point{120, 80})

var sprites = LoadImage("sprites.png")

func tick() {
    if KeyPressed("ArrowUp") {
        hero.GoUp(true)
    } else if KeyReleased("ArrowUp") {
        hero.GoUp(false)
    }
    if KeyPressed("ArrowRight") {
        hero.GoRight(true)
    } else if KeyReleased("ArrowRight") {
        hero.GoRight(false)
    }
    if KeyPressed("ArrowDown") {
        hero.GoDown(true)
    } else if KeyReleased("ArrowDown") {
        hero.GoDown(false)
    }
    if KeyPressed("ArrowLeft") {
        hero.GoLeft(true)
    } else if KeyReleased("ArrowLeft") {
        hero.GoLeft(false)
    }

    arena.MoveAll()
    ClearCanvas()
    for _, a := range arena.Actors() {
        if (a.Symbol() != Point{-1, -1}) {
            DrawImageClip(sprites, a.Symbol(), a.Size() a.Position())
        } else {
            FillRect(a.Position(), a.Size())
        }
    }
}

func main() {
    InitCanvas(arena.Size())
    MainLoop(tick)
}
