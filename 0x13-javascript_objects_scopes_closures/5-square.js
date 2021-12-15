#!/usr/bin/node
// Class Square that inherits from Rectangle, and take just one arg for size
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
