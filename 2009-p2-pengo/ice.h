#ifndef ICE_H
#define ICE_H

#include "actor.h"

class Ice : public Actor
{
public:
    Ice(Game* game, int y, int x);
    void move();
    bool isEnemy();
    bool isPlayer();
    void touchedBy(Actor* other);
    char getSymbol();
    static const char SYMBOL = '#';
private:
    int direction;
};

#endif // ICE_H
