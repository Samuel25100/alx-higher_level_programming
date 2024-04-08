#!/usr/bin/node
/* prints c is fun x time  */
if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (!isNaN(process.argv[2])) {
  let count = Number(process.argv[2]);
  while (count > 0) {
    console.log('C is fun');
    count--;
  }
}
