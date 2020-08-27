import datetime

time = datetime.datetime.now()
year = str(time.year)
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# Welcome Message

print("Welcome To Grocery List App!")
print("Current Date And Time: "+year+"/"+month+"/"+day+"\t"+hour+":"+minute)

# Items in List

print("You currently have Meat and Chesse in your list.\n")

lists = ['Meat', 'Cheese']
lists.append(input("Please enter your next item: ").title().strip())
lists.append(input("Please enter your next item: ").title().strip())
lists.append(input("Please enter your next item: ").title().strip())

# Sorted List

print("\nHere is your grocery list: \n"+str(lists))

lists.sort()
print("Your list has been sorted: \n"+str(lists)+"\n")

# Simulating Grocery Shopping

print("Simulating grocery shopping...\n")

print("Currently, you have "+str(len(lists))+" items in your list")
print("Currently, you have "+str(lists)+" items in your list")
bought = input("Please enter the item you just bought: ").title().strip()
print("Removing "+bought+" from list...")

lists.remove(bought)

print("\nCurrently, you have "+str(len(lists))+" items in your list")
print("Currently, you have "+str(lists)+" items in your list")
bought = input("Please enter the item you just bought: ").title().strip()
print("Removing "+bought+" from list...")

lists.remove(bought)

print("\nCurrently, you have "+str(len(lists))+" items in your list")
print("Currently, you have "+str(lists)+" items in your list")
bought = input("Please enter the item you just bought: ").title().strip()
print("Removing "+bought+" from list...\n")

lists.remove(bought)

print("Now you have "+str(len(lists))+" items in your list. ")
print("You have "+str(lists)+" items in your list")

# Replacing one item

item = input("\nPlease enter the item you want to buy now: ")
item = item.title().strip()
print("\nSorry, "+item+" is unavailable in the grocery\n")

new_item = input("Please input another item in the list instead of "+item+": ")
new_item = new_item.title().strip()
lists.remove(item)

lists.append(new_item)
print("Your new list is: "+str(lists))

# Thanks Message

print("\nThanks For using Aanand's Gorcery List App")
