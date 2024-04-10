#!/usr/bin/node
/* define class square */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let line = '';
    for (let j = 0; j < this.width; j++) {
      line += c;
    }
    for (let i = 0; i < this.width; i++) {
      console.log(line);
    }
  }
}
module.exports = Square;
