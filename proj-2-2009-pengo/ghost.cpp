/**
 * Example used in programming courses at University of Parma, IT.
 * Author: Michele Tomaiuolo - <tomamic@ce.unipr.it> - 2009
 *
 * This software is free: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License, version 3 or
 * later. See <http://www.gnu.org/licenses/>.
 */

#include "ghost.h"
#include "penguin.h"
#include "ice.h"
#include <cstdlib>

Ghost::Ghost(Game* game, int y, int x) :
    Actor(game, y, x),
    turn(0)
{
}

char Ghost::getSymbol()
{
    return SYMBOL;
}

bool Ghost::isEnemy()
{
    return true;
}

bool Ghost::isPlayer()
{
    return false;
}

void Ghost::move()
{
    ++turn;
    if (alive && (turn % WAIT == 0)) {
        int direction = rand() % DIRECTIONS.size();
        int newY = y + DIRECTIONS[direction][DY];
        int newX = x + DIRECTIONS[direction][DX];

        if (game->isInside(newY, newX)) {
            Actor* other = game->get(newY, newX);
            // don't touch anybody... but players
            if (other != NULL && other->isPlayer()) {
                other->touchedBy(this);
            }
            // if the cell is free, eventually, move there
            if (alive && game->get(newY, newX) == NULL) {
                y = newY;
                x = newX;
            }
        }
    }
}

void Ghost::touchedBy(Actor* other)
{
    // if a player touches a ghost, the player dies
    // otherwise, the ghost dies
    if (other->isPlayer()) {
        other->touchedBy(this);
    } else {
        alive = false;
    }
}