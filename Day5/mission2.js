const products = [
  { id: 1, name: "모니터", price: 300000, stock: 12 },
  { id: 2, name: "키보드", price: 50000, stock: 5 },
  { id: 3, name: "노트북", price: 1200000, stock: 3 }
];

const [,secondProduct] = products;
const {name,stock} = secondProduct;

console.log(`${name}의 재고는 ${stock}개입니다.`)
