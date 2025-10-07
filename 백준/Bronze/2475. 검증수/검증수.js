const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

let input = fs.readFileSync(filepath).toString().trim().split(" ").map(Number);

function verificationNumber(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i] ** 2; 
  }
  return sum % 10; 
}

console.log(verificationNumber(input));