#!/usr/bin/node
// Class that defines a Rectangle
// take two args and validates there are no equal to 0
// Instance Method called print, to print the REct with X
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
