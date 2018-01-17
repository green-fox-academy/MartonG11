'use strict';
// - Create a function called `factorio`
//   that returns it's input's factorial

function factorio(numberToFactor) {
    if (numberToFactor === 0 || numberToFactor === 1)
      return 1;
    for (var i = numberToFactor - 1; i >= 1; i--) {
      numberToFactor *= i;
    }
    return numberToFactor;
    }

console.log(factorio(5));