
nested_list=['2','3',[4,5,8]]
 
print(nested_list[2][0])

country={
    "Provinces":["KPK","Punjab","Balochistan","Sindh","Gilgit"],
    "Capital":"Islamabad",
    "Ministers":{ 
        "Foreign":"Ayan",
        "Federal":"Afnan",
        "Degence:":"Atif"
    }
}


### print sindh
print(country["Provinces"][3])  
### output will be List of province
print(country["Provinces"])
### output will be minister's dicitionary
print(country["Ministers"]["Federal"])
