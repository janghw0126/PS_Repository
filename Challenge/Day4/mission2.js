const fruits = ['사과', '바나나', '포도', '사과', '체리', '바나나', '망고'];

// forEach
fruits.forEach((fruit) => {
  console.log(fruit);
});

// includes
if (fruits.includes('망고')) {
  console.log('망고 있음');
} else {
  console.log('망고 없음');
}

// findIndex
const grapeIndex = fruits.findIndex((fruit) => fruit === '포도');
console.log(grapeIndex);

// filter
const apples = fruits.filter((fruit) => fruit === '사과');
console.log(apples);

// slice
console.log(fruits.slice(0, 3));
