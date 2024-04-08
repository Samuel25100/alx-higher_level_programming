#!/usr/bin/node
/* prints square x time  */
if (process.argv[2] === undefined) {
  console.log('Missing size');
} else if (!isNaN(process.argv[2])) {
  let y = Number(process.argv[2]);
  let x = Number(process.argv[2]);
  let line = '';
  while (x > 0) {
    line += 'X';
    x--;
  }
  while (y > 0) {
    console.log(line);
    y--;
  }
}
