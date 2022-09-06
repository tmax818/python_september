/* 
  Given an array of strings
  return the number of times each string occurs (a frequency / hash table)
*/
// a : 3
const arr1 = ["a", "a", "a"];
const expected1 = {
  a: 3,
};
// a : 2
// b : 1
// c : 3
// B : 1
// d : 1
const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
const expected2 = {
  a: 2,
  b: 1,
  c: 3,
  B: 1,
  d: 1,
};

const arr3 = [];
const expected3 = {};

/**
 * Builds a frequency table based on the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string>} arr
 * @returns {Object<string, number>} A frequency table where the keys are items
 *    from the given arr and the values are the amnt of times that item occurs.
 */
function makeFrequencyTable(arr) {
  // create the object to hold the records
  const obj = {}
  // loop over the array
  for(let i = 0; i < arr.length; i++){
    // have I seen this character: 
    // if yes, I have seen it: increment my count for that character
    if(obj[arr[i]]){
      obj[arr[i]] += 1
      // if no, create a new record for that character and set the number to 1
    } else {
      obj[arr[i]] = 1
    }
  }
  console.log(obj)
  return obj
// how do you get to the 'a' inside a loop?????

}

makeFrequencyTable(arr1)
makeFrequencyTable(arr2)
makeFrequencyTable(arr3)




