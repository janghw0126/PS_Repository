const fs = require('fs');

const input = fs.readFileSync(0, 'utf8').trim();
const N = Number(input);

let count = 0;
let divisor = 5;

while (divisor <= N) {
  count += Math.floor(N / divisor);
  divisor *= 5;
}

console.log(count);
