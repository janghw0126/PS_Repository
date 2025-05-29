const fs = require("fs")
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const N = fs.readFileSync(filepath).toString().trim().split(' ');
let Number = 1

while(Number<=N){
    console.log(Number);
    Number +=1;
}