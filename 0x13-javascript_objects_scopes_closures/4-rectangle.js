#!/usr/bin/node
/* defines a class rectangle */
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let line = '';
    for (let j = 0; j < this.width; j++) {
      line += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(line);
    }
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
