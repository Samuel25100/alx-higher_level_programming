#!/usr/bin/node
/* prints 3 lines by using an array of string and a loop */
const line = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let count = 0;
while (line[count] !== undefined) {
  console.log(line[count]);
  count++;
}
