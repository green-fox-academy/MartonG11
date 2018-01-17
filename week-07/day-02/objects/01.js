'use strict';

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

// create a function that takes a list of students and logs: 
// - how many candies are owned by students

// create a function that takes a list of students and logs:
// - Sum of the age of people who have lass than 5 candies

function Candies_owned(input_list) {
    let sum_candies = 0;
    input_list.forEach(function(item) {
      sum_candies += item.candies;
    })
    console.log('The students have ' + sum_candies + ' candies.');
  }
  
  function Age_sum(input_list) {
    let sumOfAge = 0;
    input_list.forEach(function(item) {
      sumOfAge = (item.candies < 5) ?  sumOfAge + item.age : sumOfAge;
    })
    console.log('The sum of the age of people who have less than 5 candies is ' + sumOfAge + '.');
  }
  
  Candies_owned(students);
  Age_sum(students);