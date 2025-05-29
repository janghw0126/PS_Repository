const fs = require("fs")
const filepath = process.platform === "linux" ? "dev/stdin" : './input.txt';
let input = fs.readFileSync(filepath).toString().trim().split('\n');

while(input[0][0]!=0){
    const num = input.shift().split(" ");
    console.log(Number(num[0])+Number(num[1]));
}