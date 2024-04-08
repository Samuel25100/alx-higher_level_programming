#!/usr/bin/node
/* Print the addition of two integer */
function add (a, b) {
  return (a + b);
}
if (!isNaN(process.argv[2]) && !isNaN(process.argv[3])) {
  const a = Number(process.argv[2]);
  const b = Number(process.argv[3]);
  const result = add(a, b);
  console.log(result);
} else {
  console.log('NaN');
}
