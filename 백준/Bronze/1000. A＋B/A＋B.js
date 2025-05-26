const fs = require("fs");
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const input = fs.readFileSync(filepath).toString().trim().split(' ');
console.log(Number(input[0])+Number(input[1]));