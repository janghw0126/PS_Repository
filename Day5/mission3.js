const arr1 = [1, 2];
const arr2 = [3, 4];

// 1) spread 문법을 사용하여 두 배열을 합친 newArr을 만드세요.
const newArr = [...arr1 ,...arr2];

const user = {
  name: "효빈",
  age: 26,
  hobby: "게임"
};

// 2) rest 문법을 사용해 name만 따로 분리하고 나머지를 restUser에 담으세요.
const { name, ...restUser } = user;

console.log(newArr);   // [1, 2, 3, 4]
console.log(name);     // "효빈"
console.log(restUser); // { age: 26, hobby: "게임" }