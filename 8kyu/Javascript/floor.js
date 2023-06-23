function getRealFloor(n) {
  if (n === 0) {
    return 0;
  } else if (n < 0) {
    return n;
  } else if (n > 0 && n <= 13) {
    return n-1;
  } else {
    return n-2;
  }
}

console.log("Real floor is: " + getRealFloor(-2))
console.log("Real floor is: " + getRealFloor(0))
console.log("Real floor is: " + getRealFloor(5))
console.log("Real floor is: " + getRealFloor(18))
