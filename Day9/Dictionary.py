dictionary={"Bug":"An error in program",
            "Function":"A peice of code to reuse when need",
            "Loop":"The action of doing something repeatedly"}
    

### To add new key:value########################################3#######
dictionary["Debug"]="To run and test the code"
print(dictionary)



#### to get specific value based on key############################
print(dictionary["Bug"])



## to edit any key value###############################################3


## the old loop 
print(dictionary["Loop"])
dictionary["Loop"]="Recursion until some condition"
### after assigning new value to existing key
print(dictionary["Loop"])


##Looping through dicitonary#####################################


for things in dictionary:   #### things is basicalyy key in dictionary
    print(things)
    ## to get values of those keys just
    print(dictionary[things])




#To make dictionary empty############################################ 
dictionary={}
print(dictionary)


