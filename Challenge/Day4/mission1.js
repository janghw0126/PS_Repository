function Product(name, price) {
  this.name = name;
  this.price = price;
}

const products = [
  new Product('모니터', 300000),
  new Product('키보드', 50000),
  new Product('노트북', 1200000),
];

let maxPriceProduct = products[0];

for (let i = 1; i < products.length; i++) {
  if (products[i].price > maxPriceProduct.price) {
    maxPriceProduct = products[i];
  }
}

console.log(maxPriceProduct.name);
