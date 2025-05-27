const fs = require("fs");
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const input = fs.readFileSync(filepath).toString().trim().split(' ');
const score = Number(input[0]);


if(score>=90 && score<=100){
    console.log("A");
} else if(score<=89 && score>=80){
    console.log("B");
} else if(score<=79 && score>=70){
    console.log("C");
} else if(score<=69 && score>=60){
    console.log("D");
} else{
    console.log("F");
}