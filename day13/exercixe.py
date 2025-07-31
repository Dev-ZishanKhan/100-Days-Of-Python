##1\
def odd_or_even(number):
    if number % 2 ==0:                       # here bug is num%2=0
        return "This is an even number."
    else:
        return "This is an odd number."
    

#2

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:               ## here instead of 400 it is written as 4000
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    

###3

# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:       ## here it was used (or) instead of (and)
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
      

