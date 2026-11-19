import datetime

today = datetime.date.today()
text = today.strftime("%d-%m-%Y")
#strftime -> returns in string (text)

print ("Hello, Welcome to the Expense Tracker!")

expenses = []


def create_dictionaries (item, price, expenses, text):
 
  calc_ID = len(expenses) + 1
  expense = {"Date": text, "ID": calc_ID, "Item": item, "Price":price}
  return expense


def add_expense (expenses):
  item = input("Enter your item: ")
  price = float(input("Enter the item price (RM): "))
  new_expense = create_dictionaries(item, price, expenses, text)
  expenses.append(new_expense)

add_expense (expenses)
add_expense (expenses)

print(expenses)

