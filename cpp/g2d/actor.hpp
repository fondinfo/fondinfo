/**
 * @author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
 * @license This software is free - http://www.gnu.org/licenses/gpl.html
 */

#ifndef ACTOR_HPP
#define ACTOR_HPP

#include <algorithm>
#include <vector>
#include <ctime>

namespace g2d {

struct Point { int x, y; };
struct Size { int w, h; };
struct Rect { int x, y, w, h; };
struct Color { int r, g, b; };

class Actor {
public:
    virtual void move() = 0;
    virtual void collide(Actor* other) = 0;
    virtual Rect position() = 0;
    virtual Rect symbol() = 0;
    virtual ~Actor() {}
};

class Arena {
private:
    Size size_;
    std::vector<Actor*> actors_;
public:
    Arena(Size size) { size_ = size; }
    void add(Actor* a) {
        auto pos = find(begin(actors_), end(actors_), a);
        if (pos == end(actors_)) {
            actors_.push_back(a);
        }
    }
    void remove(Actor* a) {
        auto pos = find(begin(actors_), end(actors_), a);
        if (pos != end(actors_)) {
            actors_.erase(pos);
        }
    }
    void move_all() {
        auto acts = actors();
        reverse(begin(acts), end(acts));
        for (auto a : acts) {
            a->move();
            for (auto other : acts) {
                if (other != a && check_collision(a, other)) {
                    a->collide(other);
                    other->collide(a);
                }
            }
        }
    }
    bool check_collision(Actor* a1, Actor* a2) {
        auto r1 = a1->position();
        auto r2 = a2->position();
        return (r2.y < r1.y + r1.h && r1.y < r2.y + r2.h
            && r2.x < r1.x + r1.w && r1.x < r2.x + r2.w);
    }
    std::vector<Actor*> actors() { return actors_; }
    Size size() { return size_; }
    ~Arena() {
        while (!actors_.empty()) {
            delete actors_.back();
            actors_.pop_back();
        }
    }
};

bool randomized = false;

int randint(int min, int max) {
    if (!randomized) {
        srand(time(nullptr));
        randomized = true;
    }
    return min + rand() % (1 + max - min);
}

}

#endif // ACTOR_HPP
