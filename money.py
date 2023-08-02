
from data import resources_updated ,money_count
def money_slot():
    quaters =  int(input("no of quaters(0.25): "))
    dimes = int(input("no of dimes(0.10): "))
    nickles =int(input("no of nickles(0.05): "))
    pennies = int(input("mo of pennies(0.01): "))
    money_inserted = [0.25*quaters,0.10*dimes,0.05*nickles,0.01*pennies]
    print(money_inserted)
    return money_inserted



def total_money_inserted(money_inserted):
    total_money = sum(money_inserted)
    money_count.append(total_money)
    return total_money

def order_money_check(order,total_money):
    if total_money >= order["cost"]:
        change(money_count[-1],order)
        


        return True
    else:
        print("money not enough insert coins")
        not_order = input("Do you want to order later(Y/N)").lower()
        if not_order == 'y':
            return True
        else:
            money_short = order["cost"]- total_money 
            print(f"Enter the money again? you are short :${money_short}")
            new_money = money_slot()
            new_total_money = total_money + total_money_inserted(new_money)
            money_count.append(new_total_money)
            order_money_check(order,new_total_money)
            return False
    
    #     #money_slot()


def change(customer_money,order):
    if customer_money > order['cost']:
        print(f"here is your order : {order} change: $ {customer_money-order['cost']}\n have a great day")
    else:
        print(f"here is your order : {order} \n have a great day")



    


    

