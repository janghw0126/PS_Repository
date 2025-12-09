function checkAdult(age) {
  switch (true) {
    case age >= 18:
      return '성인입니다.';
    default:
      return '미성년자입니다.';
  }
}

//예시 실행
console.log(checkAdult(20));
