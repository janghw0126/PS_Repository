let x = 1;

function test() {
  console.log(x); // undefined
  var x = 2;
  console.log(x); // 2
}

test();
console.log(x); // 1

// 정답
// undefined
// 2
// 1
