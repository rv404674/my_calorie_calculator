
# give show ingredients available
from constants import Constants
from collections import defaultdict

def util(amount, item):
    # 300, milk
    # milk-300": [9.45, 15.3, 18, 261]
    for key,val in Constants.NUTRIENTS_DICT.items():
        if item in key:
            key_amount = int(key.split('-')[1])
            return [amount*1.0*val[0]/key_amount, amount*1.0*val[1]/key_amount,
            amount*1.0*val[2]/key_amount, amount*1.0*val[3]/key_amount]

# 32g-oats, 300ml-milk, 2-banana, 33g-whey protein,
# kaju + badam, 2-eggomellete, 2-bread, 20g-peanut butter
def calculate():
    print("Enter the food")
    input_list = input().split(", ")

    track_all = defaultdict(int)

    for i in input_list:
        amount_str, item = i.split('-')
        # now find the amount from the str
        temp_str = ""
        for j in amount_str:
            if j.isdigit():
                temp_str+=j
        
        # util() will return [protien, carbs, fat, calories]
        p,c,f,cal = util(int(temp_str), item)

        track_all['protien'] += p
        track_all['carbs'] += c
        track_all['fat'] += f
        track_all['calories'] += cal

    print("Details\n")
    for key,val in track_all.items():
        print("{} - {}".format(key,round(val,1)))
    print("\n")

while 1:
    print("1. See the food Items.")
    print("2. Calculate the calories")
    print("3. Exit\n")

    choice = int(input())
    if choice == 1:
        print(Constants.NUTRIENTS_DICT)
        print("\n")
    elif choice == 2:
        calculate()
    else:
        break



