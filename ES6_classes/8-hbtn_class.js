export class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  // When cast into a Number
  valueOf() {
    return this._size;
  }

  // When cast into a String
  toString() {
    return this._location;
  }
}
