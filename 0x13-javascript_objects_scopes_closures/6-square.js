#!/usr/bin/node
const Rectangle = require('./5-rectangle');
class Square extends Rectangle {
  sqPrint (c) {
    let i;
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
