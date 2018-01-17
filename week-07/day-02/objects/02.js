'use strict';

var students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 4},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

// create a function that takes a list of students and logs:
// - Who has got more candies than 4 candies

// create a function that takes a list of students and logs: 
//  - how many candies they have on average

function candy_counter(input_list) {

    let student_names = []
    input_list.forEach(function(item) {
        if (item.candies > 4) {
            student_names += (" ") + item.name
        }
    })
    console.log(student_names + " has/have more candies than 4.")
}

function average_candies(input_list) {

    let totalcandies = 0;
    input_list.forEach(function(item) {
        totalcandies += item.candies;
    })
    
    console.log("Students have average " + totalcandies / students.length +" candies.")
}

candy_counter(students);
average_candies(students)
