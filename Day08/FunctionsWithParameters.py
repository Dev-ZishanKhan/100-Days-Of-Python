### SImple Function Defination And Calling


##Definatin
def greet():
    print("how are you?")
    print("Am FIne Nd U?")
    print("Am Good Too..")
##Calling
greet()


### Funtions With variables/parameters defining and calling


###defining 

def multiple(val):
    i = 1
    while i <= 10:
        print(f"{val} x {i} = {val * i}")
        i += 1

# Call the function with converted input
num = int(input("Enter number to get its multiples: "))
multiple(num)
