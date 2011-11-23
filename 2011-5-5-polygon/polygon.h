#ifndef POLYGON_H
#define POLYGON_H

#include "point.h"

#include <vector>
#include <iostream>

using namespace std;

class Polygon
{
public:
    Polygon();
    ~Polygon();

    float perimeter();

    void read(istream& in);
    void write(ostream& out);

private:
    vector<Point*> points;
};

#endif // POLYGON_H
