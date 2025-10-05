const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

let A = input[0];
let B = input[1];

let reverseA = Number(A.split('').reverse().join(''));
let reverseB = Number(B.split('').reverse().join(''));

if (reverseA > reverseB) {
  console.log(reverseA);
} else {
  console.log(reverseB);
}