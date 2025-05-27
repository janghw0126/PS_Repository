const fs = require("fs");
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const input = Number(fs.readFileSync(filepath).toString().trim().split(' '));


if(input>=90 && input<=100){
    console.log("A");
} else if(input<=89 && input>=80){
    console.log("B");
} else if(input<=79 && input>=70){
    console.log("C");
} else if(input<=69 && input>=60){
    console.log("D");
} else{
    console.log("F");
}