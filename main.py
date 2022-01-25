#all are class menuitem,coffeemaker,moneymachine
from menu import Menu, MenuItem 
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#so if its class we will use only class from coffee_maker & money_machine
#creating an object and  we can name our object anything  left side is obj

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu=Menu()
is_on=True
#from moneymachine we have to print report so we call it like object.whatever()

coffee_maker.report()
money_machine.report()

#checking if resource sufficent 
while is_on:
  options=menu.get_items()
  choice=input(f"What would you like ?({options})")
  if is_on =="off":
    is_on=False
  elif choice=="report":
    coffee_maker.report()
    money_machine.report()
  else:
    drink=menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink):
      if money_machine.make_payment(drink.cost):
        print(coffee_maker.make_coffee(drink))


  


