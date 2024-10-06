#pricing and ratio of ingredient

data={
    "cappuccino":{
        "ingredient":{
            "water":40,
            "milk":80,
            "coffee":20
        },
        "cost":150
    },
    "latte":{
        "ingredient":{
            "water":40,
            "milk":120,
            "coffee":30
        },
        "cost":200
    },
    "americano":{
        "ingredient":{
            "water":50,
            "milk":100,
            "coffee":30
        },
        "cost":100
    },
    "expresso":{
        "ingredient":{
            "water":100,
            "milk":0,
            "coffee":40
        },
        "cost":80
    }

}

# Availability of stack
stack={
    "water":1000,
    "milk":1000,
    "coffee":500
}

profit=0

on=True
while on:
    print("                             ****WELOME TO THIS AMAZING COFFEE MACHINE****")
    choice=input("What do you like to have?(cappuccino/latte/americano/expresso/report)")

    if choice=="report":
        print("water : ",stack["water"],"ml")
        print("milk  : ",stack["milk"],"ml")
        print("coffee : ",stack["coffee"],"gm")
        print("net profit :INR",profit)

    elif choice=="off":
        on=False    