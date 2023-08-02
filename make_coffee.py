
from money import total_money_inserted, order_money_check , money_slot
from data import MENU, resources

from resources import resource_check , resource_report
coffee_machine_on = True
money_check = False

while coffee_machine_on:
    print("Hello !\nWelcome to blue rock cafe!\nWhat would you like?\n")
    for items in MENU:
        #print(items)
        print(f"{items}....................................{MENU[items]['cost']}") 
    order = input().lower()
    if order == 'openup':
        coffee_machine_on = False
        resource_report()
    
    while money_check == False:
        order_data = MENU[f"{order}"]
        print("please insert coins")
        money_inserted_data = money_slot()
        # total_money_inserted(money_inserted_data)
        money_check = order_money_check(order_data,total_money_inserted(money_inserted_data))
        print(money_check)
    # if resource_check(order)


# rounding off the money inserter
# ability to multi order
#load resources in open up 
#withdraw money (money checkout) with password facility 