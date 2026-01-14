const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(' ');
const M = Number(input[0]);
const N = Number(input[1]);

function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false;
  }
  return true;
}

let result = [];
for (let i = M; i <= N; i++) {
  if (isPrime(i)) result.push(i);
}

console.log(result.join('\n'));