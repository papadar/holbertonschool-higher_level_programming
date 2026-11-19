#!/usr/bin/node
const num = parseInt(process.argv[2], 10);
const char = "X";

if (!Number.isNaN(num) && num > 0) {
  for (let i = 0; i < num; i++) {
    console.log(char.repeat(num)); 
  }
} else {
  console.log('Missing size');
}
