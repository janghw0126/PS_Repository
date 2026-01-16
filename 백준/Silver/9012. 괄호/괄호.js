const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').split('\n');

const T = parseInt(input[0], 10);
let result = [];

for (let i = 1; i <= T; i++) {
  const line = input[i].trim();
  let count = 0;
  let isValid = true;

  for (const li of line) {
    if (li === '(') {
      count++;
    } else if (li === ')') {
      count--;
    }

    if (count < 0) {
      isValid = false;
      break;
    }
  }

  if (isValid && count === 0) {
    result.push('YES');
  } else {
    result.push('NO');
  }
}

console.log(result.join('\n'));
