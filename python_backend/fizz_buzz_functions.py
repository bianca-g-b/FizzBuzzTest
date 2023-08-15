#File that containes function that appends numbers to json list file

#import json, to be able to handle json fizz_buzz_list file
import json

#write function to append numbers to a list
def fizz_buzz_nums(num):
    fizz_buzz_list=[]
    for i in range(1,num+1):
        if (i%3==0 and i%5==0):
            fizz_buzz_list.append("FizzBuzz")
        elif (i%3==0):
            fizz_buzz_list.append("Fizz")
        elif (i%5==0):
            fizz_buzz_list.append("Buzz")
        else:
            fizz_buzz_list.append(i)
    return fizz_buzz_list

#write function to append numbers to json file
#open fizz_buzz_list.json in read and write mode and write the list returned by fizz_buzz_nums function to it
#return the list of numbers and strings
def add_nums_to_json(num):
    with open("fizz_buzz_list.json", "w+") as file:
        json.dump(fizz_buzz_nums(num), file)
    return fizz_buzz_nums(num)

# add_nums_to_json(100)