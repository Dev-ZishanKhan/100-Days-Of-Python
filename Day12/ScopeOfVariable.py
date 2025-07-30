####### local scope Variable

def even_num(num):
    if (num%2)==0:
        even=True        #### this variable can be only accessable in this function not outside the function
        print(even)
even_num(8)



##### Global Scope Variable

age=18                 #### This varialbe can be used everywhere in the code
def adult():
    if age >45:
        print("Adult")
    elif age<30:
        print("Young")
    elif age >18:
        print("teen")
adult()


###### Modifying Global Scope


enemies=2

def find_enemies():
    global enemies
    seen=int(input("How many Enemies are there: "))
    enemies+=seen

    print(enemies)

find_enemies()  ###O/P=25
print(enemies)  ###O/P=25   