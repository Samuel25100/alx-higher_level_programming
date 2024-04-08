#!/usr/bin/node
/* searches the second biggest integer in the list of arguments */
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let arr = process.argv.slice(2).map(Number);
  arr = arr.sort(function (a, b) { return (b - a); });
  console.log(arr[1]);
}
