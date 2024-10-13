# PROGRAMMING FOR COFFEE MACHINE SYSTEM


#pricing and ratio of ingredient

data={                            #primary dictionary for coffee names
    "cappuccino":{                #secondary dict for ingredient and price 
        "ingredient":{            #tertiary dict for required ratio
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


# Availability of stock
stock={
    "water":1000,
    "milk":1000,
    "coffee":500
}

profit=0 #in INR

#function to check if stack is sufficient or not
def check_if_avail(input):
    for item in input:
        if(stock[item]>=input[item]):
             return True
        else:
            return False

#function to recieve money from costumer
def payment():
    a,b,c,d,e  =map(int,input("enter currency notes in following sequence:₹500,₹100,₹50,₹20,₹10   ").split())
    total=a*500+b*100+c*50+d*20+e*10
    return total



#function to update stack after each serving
def updating_stock(input):
    for item in input:
        stock[item]-=input[item]
        
    return True    



on=True
while on:
    print("                             ****WELOME TO THIS AMAZING COFFEE MACHINE****")
    choice=input("What do you like to have?(cappuccino/latte/americano/expresso/report)")

    if choice=="report":
        password=input("enter the password:")
        if(password=="chai"):
            print("water : ",stock["water"],"ml")
            print("milk  : ",stock["milk"],"ml")
            print("coffee : ",stock["coffee"],"gm")
            print("net profit :₹",profit)

        else:
            print("YOU CAN'T ACCESS REPORT")    

        
    elif choice=="off":
        on=False 
    else:
        drink=data[choice]  
        if(check_if_avail(drink["ingredient"])==0):
            print("currently we are unable to serve you.\nsorry for inconvenience")
            on=False
        else:
            print("your drink costs ₹",drink["cost"])
            # recieving money from user
            amt_recieve=int(payment())
            cost=drink["cost"]


            if(amt_recieve>=cost):
                #calculating left amount returning back to customer
                
                amt_return=amt_recieve-cost
                print("amount to be return ",amt_return)    

                print("transaction is successful")

                #calculating total profit
                profit+=amt_recieve-amt_return

                print("Prepairing Your Coffee \n Thank You Waiting")
                updating_stock(drink["ingredient"])
                print("Here Is Your Drink \n Have A Nice Day(:")

            else:
                print("transaction fail!")
                print("money refunded :",amt_recieve)    