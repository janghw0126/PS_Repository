fs = require("fs");
filePath = process.platform === "linux" ? "/dev/stdin" : "test.txt";

let input = Number(fs.readFileSync(filePath).toString());
let n = 1;

while (n < 10) {
  console.log(`${input} * ${n} = ${input * n}`);
  n++;
}