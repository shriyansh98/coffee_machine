#from data import resources_updated , resources, MENU
# from make_coffee import 
def resource_update():
    pass

def resource_check(order):
    order_data = MENU[f"{order}"]
    water = order_data['ingredients']['water']
    milk = order_data['ingredients']['milk']
    coffee = order_data['ingredients']['coffee']
    #print(water,milk,coffee)
    if water >= resource_update[water] and milk >= resource_update[milk] and coffee >= resource_update[coffee] :
        return True
    else:
        print(f"Not enough resources availbale to make {order}")
        order_something_else = input("order something else(Y/N)").lower()
        if order_something_else == 'y':
             order = input("what else would you like?")
             
            
        return False
 
    # pass

resources_updated = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,

}
def resource_report(resources_updated):
    for key in resources_updated:
        print(f"{key} : {resources_updated[key]}")

if __name__ == '__main__':
    resource_report()