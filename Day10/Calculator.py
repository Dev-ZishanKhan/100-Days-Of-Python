def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2

operation={
     "+":add,
     "-":sub,
     "*":mul,
     "/":div
}

def calculator():
    start=True
    firstNum=float(input("Whats the first number?: "))

    while start:
        for i in operation:
            print(i)
        choice=input("pick an operations: ")
        nextNum=float(input("What's the next number?: "))

        result=operation[choice](firstNum,nextNum)
        print(f"{(firstNum)} {choice} {(nextNum)}={result}")

        choice2=input(f"Type 'y' to continue wiht this {result} or type 'n' to start new calculate: ").lower()
        if choice2=='y':
            firstNum=result

        else: 
            start=False
            calculator()

calculator()
                



    
        

