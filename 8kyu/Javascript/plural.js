function plural(n) {
  if (n === 1) {
    return false;
  } else {
    return true;
  }
}

console.log(plural(0))
console.log(plural(1))
console.log(plural(100))
console.log(plural("Infinity"))
