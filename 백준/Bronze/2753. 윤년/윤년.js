const fs = require("fs");
const filepath = process.platform === 'linux' ? 'dev/stdin' : './input.txt';

const year = fs.readFileSync(filepath).toString().trim().split(' ');
if(year%4==0 && (year%100!=0||year%400==0)){
    console.log(1);
}else{
    console.log(0);
}