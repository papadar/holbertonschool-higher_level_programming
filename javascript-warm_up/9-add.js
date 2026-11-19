#!/usr/bin/node
const num0 = parseInt(process.argv[2], 10);
const num1 = parseInt(process.argv[3], 10);

function add (num0, num1) {
  return num0 + num1;
}

console.log(add(num0, num1));
