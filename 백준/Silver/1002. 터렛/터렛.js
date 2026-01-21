const fs = require('fs');
const input = fs.readFileSync(0, 'utf-8').trim().split('\n');

const T = Number(input[0]);

for (let i = 1; i <= T; i++) {
  const [x1, y1, r1, x2, y2, r2] = input[i].split(' ').map(Number);

  const dx = x1 - x2;
  const dy = y1 - y2;
  const dist = Math.sqrt(dx * dx + dy * dy);

  if (dist === 0 && r1 === r2) {
    console.log(-1);
  }
  else if (dist > r1 + r2 || dist < Math.abs(r1 - r2)) {
    console.log(0);
  }
  else if (dist === r1 + r2 || dist === Math.abs(r1 - r2)) {
    console.log(1);
  }
  else {
    console.log(2);
  }
}
