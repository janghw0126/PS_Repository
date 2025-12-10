let person = {
  name: '효빈',
  sayName() {
    console.log(this.name);
  },
  run: () => person.sayName(),
};

person.run();
