#!/usr/bin/node
/* prints a message depending of the number of arguments passed */
if (process.argv.length <= 2) {
  console.log('undefine is undefine');
} else if (process.argv.length === 3) {
  console.log(process.argv[2], ' is undefine');
} else if (process.argv.length >= 4) {
  console.log(process.argv[2], 'is', process.argv[3]);
}
