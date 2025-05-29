
// const [a, b] = require('fs').readFileSync('/dev/stdin').toString().split(" ").map(Number)

// console.log(Math.abs(a-b))


const fs = require("fs")
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const [a,b] = fs.readFileSync(filepath).toString().trim().split(' ');

console.log(Math.abs(a-b));