const fs = require("fs");
const filepath = process.platform === "linux" ? "/dev/stdin" : "./input.txt"; 
const input = fs.readFileSync(filepath).toString().trim().split('\n');

const [N, X] = input[0].split(' ').map(Number);
// 수열 A를 숫자 배열열로 변환함
const A = input[1].split(' ').map(Number);

// filter() ->  배열에서 조건에 맞는 요소들만 골라내는 함수
// A 배열에서 X보다 작은 숫자만 골라 새로운 배열 생성함
const result = A.filter(num => num < X);

// 결과 배열을 공백으로 구분된 문자열로 출력함
console.log(result.join(' '));