let numbers = [1,2,3,4,5, -5];

// tell if there are negatives:
let result = numbers.filter(n => n < 0);
console.log(result);

let hasNegative = numbers.some(n => n <0);
console.log(hasNegative);