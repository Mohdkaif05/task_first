function to recieve money from costumer
def payment():
    print("we accept on ₹10,₹20,₹50,₹100,₹500 rupee notes" )
    total=int(input("Number of ₹500 notes"))*500
    total+=int(input("Number of ₹100 notes"))*100
    total+=int(input("Number of ₹50 notes"))*50
    total+=int(input("Number of ₹20 notes"))*20
    total+=int(input("Number of ₹10 notes"))*10
    return total