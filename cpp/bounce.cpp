/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#include "bounce.hpp"
#include "g2d/canvas.hpp"
#include <iostream>

auto arena = new Arena{{320, 240}};
auto b1 = new Ball{arena, {40, 80}};
auto b2 = new Ball{arena, {80, 40}};
auto g = new Ghost{arena, {120, 80}};
auto turtle = new Turtle{arena, {80, 80}};
auto sprites = load_image("sprites.png");

void tick() {
    if (key_pressed("ArrowUp")) {
        turtle->go_up();
    } else if (key_pressed("ArrowDown")) {
        turtle->go_down();
    } else if (key_pressed("ArrowLeft")) {
        turtle->go_left();
    } else if (key_pressed("ArrowRight")) {
        turtle->go_right();
    } else if (key_released("ArrowUp") ||
               key_released("ArrowDown") ||
               key_released("ArrowLeft") ||
               key_released("ArrowRight")) {
        turtle->stay();
    }

    arena->move_all();
    clear_canvas();
    for (auto a : arena->actors()) {
        draw_image_clip(sprites, a->symbol(), a->position());
    }
}

int main() {
    init_canvas(arena->size());
    main_loop(tick);
}

int main_console() {
    auto arena = new Arena{{320, 240}};
    new Ball{arena, {40, 80}};
    new Ball{arena, {80, 40}};
    new Ghost{arena, {120, 80}};
    auto turtle = new Turtle{arena, {80, 80}};

    for (std::string line; std::getline(std::cin, line);) {
        if (line == "w") turtle->go_up();
        else if (line == "a") turtle->go_left();
        else if (line == "s") turtle->go_down();
        else if (line == "d") turtle->go_right();
        else if (line == " ") turtle->stay();

        arena->move_all();
        for (auto a : arena->actors()) {
            auto pos = a->position();
            std::cout << pos.x << " " << pos.y << std::endl;
        }
        std::cout << std::endl;
    }
    return 0;
}
