const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";

let input = fs.readFileSync(filepath).toString().trim().split("\n").map(Number);

// 첫 번째 줄 제거
// input.shift();
input = input.slice(1);

// 각 멀티탭은 자기 콘센트 하나를 사용하기 때문에
// 마지막 탭은 제외하고 1 감소
for (let i = 0; i < input.length; i++) {
  if (i !== input.length - 1) {
    input[i]--;
  }
}

// 연결 가능한 총 컴퓨터 수 출력
// console.log(input.reduce((a, b) => a + b, 0));
let sum = 0;
for (let i = 0; i < input.length; i++) {
  sum += input[i];
}
console.log(sum);