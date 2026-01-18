let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

for (const line of input) {
  if (line === '0') break;
  let totalSum = 2;

  for (const char of line) {
    if (char === '1') totalSum += 2;
    else if (char === '0') totalSum += 4;
    else totalSum += 3;
  }

  totalSum += line.length - 1;
  console.log(totalSum);
}
