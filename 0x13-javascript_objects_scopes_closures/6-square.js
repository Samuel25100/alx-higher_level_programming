#!/usr/bin/node
/* define class square */
const Squ = require('./5-square');

class Square extends Squ {
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
