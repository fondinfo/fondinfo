## Programming lab @ UniPR

http://tomamic.github.io/fondinfo/

Python and C++ examples

Copyleft (ɔ) 2008-2020 Michele Tomaiuolo - http://sowide.unipr.it/tomamic <br>
This software is free - License: http://www.gnu.org/licenses/gpl-3.0.txt

---

## g2d

### Installing

- Copy `g2d.py` from `examples` into the same folder containing your scripts; this will draw into a *PyGame window*
- Alternatively, copy `g2d_web.py` in that location and rename the file as `g2d.py`; this will draw into a *browser window*

### Basic structs

- A `point` or a `size` is a tuple `(x, y)`
- A `color` is a tuple `(r, g, b)`

### Canvas functions

- **`init_canvas`** `(size: (int, int))` : Initialize the drawing canvas
- **`main_loop`** `(tick=None, fps=30)` : Start the event loop, accepting an optional `tick` function, which will be called periodically
- **`clear_canvas`** `()` : Clear the canvas
- **`close_canvas`** `()` : Close the canvas and exit the main loop

### Drawing functions

- **`set_color`** `(color: (int, int, int))` : Set the drawing color
- **`draw_line`** `(pt1: (int, int), pt2: (int, int))` : Draw a line from `pt1` to `pt2`
- **`fill_circle`** `(center: (int, int), radius: int)` : Fill a circle, given `center` and `radius`
- **`fill_rect`** `(pos: (int, int), size: (int, int))` : Fill a given rectangle, given left-top position and size
- **`draw_text`** `(txt: str, pos: (int, int), size: int)` : Draw a text, given left-top position and font px size
- **`draw_text_centered`** `(txt: str, pos: (int, int), size: int)` : Draw a centered text, given center and font px size

### Images and sounds

- **`load_image`** `(src: str) -> str` : Load an image and return a name for it
- **`draw_image`** `(src: str, pos: (int, int))` : Blit a whole image, given its name and the position
- **`draw_image_clip`** `(src: str, pos: (int, int), clip_pos: (int, int), clip_size: (int, int))` : Blit a portion of an image
- **`load_audio`** `(src: str) -> str` : Load a sound and return a name for it
- **`play_audio`** `(src: str, loop: bool)` : Play a sound, possibly in a loop, given its name
- **`pause_audio`** `(src: str)` : Stop playing a sound, given its name

### Input and output

- **`mouse_pos`** `() -> (int, int)` : Get current mouse position
- **`mouse_clicked`** `() -> bool` : Check if left mouse button has been clicked
- **`current_keys`** `() -> tuple` : Get all keys that are currently held down
- **`previous_keys`** `() -> tuple` : Get all keys held down at the previous frame
- **`prompt`** `(message: str) -> str` : Show a dialog for entering a line of text
- **`confirm`** `(message: str) -> bool` : Show a dialog for confirming a decision
- **`alert`** `(message: str)` : Show a dialog with a message
