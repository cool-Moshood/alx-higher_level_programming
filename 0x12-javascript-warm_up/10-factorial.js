#!/usr/bin/node

let x = parseInt(process.argv[2]);

if (isNaN(x)) {
    console.log(1);
} else {
    let y = 1;
    for (let i = 1; i <= x; i++) {
        y *= i;
    }
    console.log(y);
}
