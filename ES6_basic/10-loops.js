export default function appendToEachArrayValue(array, appendString) {
    for (const idx of array) {
      var value = array[idx];
      newArray.push(appendString + value);
    }
  
    return newArray;
  }
