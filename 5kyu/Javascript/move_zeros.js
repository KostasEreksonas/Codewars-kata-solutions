function moveZeros(arr) {
  let zeroCount = 0;
  const newArr = [];

  // Count zeroes and append all non-zero values to a new array
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 0) {
      zeroCount += 1;
    } else {
      newArr.push(arr[i]);
    }
  }

  // Append counted zeroes to the end of a new array
  for (let j = 0; j < zeroCount; j++) {
    newArr.push(0);
  }

  return newArr;
}

console.log("Before: " + [1,2,0,1,0,1,0,3,0,1] + " after: " + moveZeros([1,2,0,1,0,1,0,3,0,1]))
