#lists
dshealter = {"house":1, "apartment":1, "bunker":5}


#Calculations and functions
def food_calf():
    if food_cal == "y":
        cal = int(input("How much food do you have stored in Kcal?: "))
        daily = int(input("How many calories do you use per day? (avg is 1500 -2500): "))
        days = int(cal/daily)
        print("{} days.".format(days))
    else:
        days = int(input("How much food you you have stored in days?: ").strip())
    return days
        

def final_cal ():
    #shealter_score = sheal()
    days = food_calf()
    
    if renew_f and renew_w == "y":
        renew = 100
    elif renew_f or renew_w == "y":
        renew = 50
    else:
        renew = 0

    if group > 4 :
        modify = 0.75
    else:
        modify = 2

    final_score = shealter_score + water + days + renew * modify

    if final_score > days or water:
        survival = water + renew
    else:
        survival = final_score
        
        
    print("Well done {}, you will survive {} days!".format(name,survival))

#loops

while True:
    name = input("Please enter your name: ").strip().lower().capitalize()
    shealter = input("Please enter the type of shealter you have: ").strip().lower()
    if shealter in dshealter:
        shealter_score = dshealter[shealter]
        #print(shealter_score)
    else:
        add = input("Your shealter doesnt appear in my list, would you like to add it (y/n)?: ")
        if add == "y":
            v = input("Please add the survival value (1-5): ")
            dshealter[shealter] = v
            shealter_score = dshealter[shealter]
        else:
            shealter_score = 0
    water = int(input("How much water do you have stored in gallons?: ").strip())
    food_cal = input("Would you like to use the food calculator?(y/n): ").strip()
    group = int(input("What is your group size: ").strip())
    renew_f = input("Do you have renewable food?(y/n): ").strip().lower()
    renew_w = input("Do you have renewable water?(y/n): ").strip().lower()
    final_cal()



#Outputs

