#### titel function uses to make the stirng in Capsulation format 
def name(fname,lname):
    return f"{fname.title()}{lname.title()}"
print(name("sNoOkEr","pLAYEr"))  ### Snooker King

#####################################


def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                 return True
            else:
                 return False
        else:
                return True
    else:
        return False
print(is_leap_year(2000))
print(is_leap_year(1959))
print(is_leap_year(2003))
print(is_leap_year(2024))