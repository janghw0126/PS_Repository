fs = require("fs");
filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";

let input = fs.readFileSync(filePath).toString().trim().split(" ");
let answer = 0;

for (let i = 0; i < input.length; i++) {
  if (input[i] !== "") answer++;
}

console.log(answer);