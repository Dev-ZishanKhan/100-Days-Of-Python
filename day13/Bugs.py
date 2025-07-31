############ BUgs can be of many types

# it is an error 
# u cant add int into string

# sum=12+"ew"
# print(sum)


# to fix it/ it should be bpth integer or both be string

# you can use try cath block to fix it


try:
    a=int(input("Enter: "))
    sum=12+a
    print(sum)

except ValueError:
    print("You should input only Integer ")
    a=int(input("Enter: "))
    sum=12+a

    
  

