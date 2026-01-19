const fs = require('fs');

const input = fs.readFileSync(0, 'utf-8').trim().split('\n');
const N = +input[0];

let people = [];

for (let i = 1; i <= N; i++) {
  const [weight, height] = input[i].split(' ').map(Number);
  people.push([weight, height]);
}

let ranks = [];

for (let i = 0; i < N; i++) {
  let count = 0;
  for (let j = 0; j < N; j++) {
    if (i === j) continue;
    if (people[j][0] > people[i][0] && people[j][1] > people[i][1]) {
      count++;
    }
  }
  ranks.push(count + 1);
}

console.log(ranks.join(' '));
