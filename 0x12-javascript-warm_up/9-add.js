#!/usr/bin/node

const first = parseInt(process.argv[2]);
const second = parseInt(process.argv[3]);

function add (a, b) {
  return (a + b);
}

let total = 0;
total = add(first, second);
console.log(total);
