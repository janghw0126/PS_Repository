function calculate(num1, num2, op) {
  switch (op) {
    case '+':
      return num1 + num2;
    case '-':
      return num1 - num2;
    case '*':
      return num1 * num2;
    case '/':
      return num1 / num2;
    default:
      return '지원하지 않는 연산자입니다.';
  }
}

//예시 실행
console.log(calculate(10, 5, '+')); // 15
console.log(calculate(10, 5, '*')); // 50
