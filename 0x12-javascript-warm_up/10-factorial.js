#!/usr/bin/node

let x = parseInt(process.argv[2]);

function factorial(x) {

    if (x === 1 || isNaN(x)) {
        return 1;
    } else {
        return x * factorial(x - 1);
    }
}

let y = 1;
y = factorial(x);
console.log(y);
