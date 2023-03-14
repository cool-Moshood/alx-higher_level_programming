#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
    console.log('Missing size');
} else {
    for (let j = 0; j < x; j++) {
        let y = "";
        for (let i = 0; i < x; i++) {
            y += 'X';
        }
        console.log(y);
    }
}
