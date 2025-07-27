
####

computer={
    "intel":{
        "core-i3":{
            "gen":"11",
            'speed':"3.6ghz",
            "clock":[2.3,6.2,2.3,4.2,4]
        },
        "core-i5":{
            "gen":"10",
            'speed':"3.4ghz"
        }
    },
    "amd":{
        "ryzen-5":{
            "gen":"3",
            'speed':"3.2ghz"
        }
    }

}

print(computer["intel"]["core-i3"]["clock"][-3])






