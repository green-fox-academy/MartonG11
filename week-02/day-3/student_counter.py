# create a function that takes a list of students and prints: 
# - how many candies are owned by students

# create a function that takes a list of students and prints:
# - Sum of the age of people who have lass than 5 candies


students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1}
]

#def total_candy(in_class):
#    print((sum([student['candies'] for student in in_class])))
    
#total_candy(students)


def people_age(sum_candy):
    for ['age'], ['candies'] in list.items():
        if ['candies'] < 5:
            print(age) 

people_age(students)


def candy_more():
    for i in students:
        if i["candies"] > 4:
            print(i["name"])

candy_more()

def candy_ave():
    candy = 0
    for i in students:
        candy += i["candies"]
    for n in students:
        average = candy / len(students)
    print(average)

candy_ave() 
    




def more_candies(lista):
        whos_got = ' '
        for x in lista:
                if x['candies']>4:
                    whos_got += x['name'] + ' '
        print(whos_got)




    for i in range(0, len(students), 1):
        if students[i]['candies'] > 4:
            print(students[i]['name'])
