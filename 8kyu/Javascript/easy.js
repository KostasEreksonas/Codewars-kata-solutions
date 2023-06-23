function problem(x){
  if (typeof(x) === 'string') {
    return "Error";
  } else {
    return 50*x+6;
  }
}

console.log(problem(2));
console.log(problem("ABC"));
console.log(problem(5));
console.log(problem(7));
console.log(problem("9"));
