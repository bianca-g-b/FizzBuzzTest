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