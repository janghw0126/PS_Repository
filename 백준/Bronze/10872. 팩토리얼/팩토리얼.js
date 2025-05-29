const fs = require("fs")
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const N= fs.readFileSync(filepath).toString().trim().split(' ');
let i = 1;
let result = 1;

while(i<=N){
    result *= i;
    i += 1;
}

console.log(result);