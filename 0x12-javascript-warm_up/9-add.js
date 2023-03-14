#!/usr/bin/node

let first = parseInt(process.argv[2]);
let second = parseInt(process.argv[3]);

function add(a, b) {
	return (a + b);
}

let total = 0;
total = add(first, second);
console.log(total);

