// Return the nth triangular number
function triangular(n) {
  let sum = 0;
  if (n <= 0) {
    sum = 0;
  } else {
    for (i = 0; i < n; i++) {
      sum += i + 1;
    }
  }
  return sum;
}

console.log(triangular(11207))
console.log(triangular(-6))
console.log(triangular(22452))
console.log(triangular(6))
console.log(triangular(47))
