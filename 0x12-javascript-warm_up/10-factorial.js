#!/usr/bin/node
/* computes and prints a factorial */
function factorial (a) {
  if (a === 1) {
    return (1);
  }
  return (a * factorial(a - 1));
}
if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(Number(process.argv[2])));
}
