#!/usr/bin/node
// Class that defines a Rectangle, take two args and validates there are no equal to 0
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
