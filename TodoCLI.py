import json
from collections import defaultdict
import sys
from itertools import chain

data = defaultdict(dict)
finished = {}


def add_items(data):
    print("Enter your item -> Important Milk")
    user_input = input()

    try:
        key, value = user_input.split(" ", 1)
        data.setdefault(key.strip(), {})[value.strip()] = False
    except ValueError:
        print("Invalid Format. Use: Prority Item")

def showData(data):
    print(data)
    print(finished)
    for x, j in chain(data.items(), finished.items()):
        print(x, j)


def endProgram(data):
    print("Ending Program")
    sys.exit()

def remove_items(data):
    print("Enter the item you want to remove -> Milk")
    remove_input = input()

    for prority, items in data.items():
        if remove_input in items:
            if len(data[prority]) <= 1:
                print(f"Removing {prority} due to {remove_input} is the only item in category")
                del data[prority]
            else:
                print(f"Removing {remove_input} from the {prority} category")
                items.pop(remove_input)
            break
    else:
        print(f"Item {remove_input} cannout be found in any category.")


def update_staus(data):
    print("What item status do you want to update: update status moves items to the finish category -> Gas : Will move gas from the list to the finished list!")
    user_updateInput = input().strip()
    
    for prority, items in data.items():
        if user_updateInput in items:
            finished[user_updateInput] = True
        
            del items[user_updateInput]

            if not items:
                del data[prority]

            print(f"Moved {user_updateInput} to Finished")
            break

    else:
        print(f"{user_updateInput} is not found in any category")


def save(data):
    with open("output.json", "w") as f:
        json.dump({
            "data": data,
            "finished": finished
        }, f, indent=4)

def readJSON():
    with open("output.json", "r") as f:
        print(json.load(f))

def getItem(data):
    print("What Item do you want to find -> Water")
    user_lookup = input().strip()

    for outer_key, inner_dict in data.items():
        keys = list(inner_dict.keys())
        if user_lookup in inner_dict:
            print(f"{user_lookup} is found at {keys.index(user_lookup)} in the category {outer_key}")
            return
    
    finished_keys = list(finished.keys())
    if user_lookup in finished_keys:
        print(f"{user_lookup} is found at {finished_keys.index(user_lookup)} in 'Finished' category")
        return
    
    print(f"{user_lookup} is not found in any categorys")

commands = {
    ",add": add_items,
    ",remove": remove_items,
    ",update" : update_staus,
    ",show" : showData,
    ",quit" : endProgram,
    ",save": save,
    ",get": getItem,
    ",open": readJSON

}

def main():
    while True:
        print("Enter an coommand to start -> [,add] [,remove] [,update] [,show] [,quit] [,save] [,get]")
        userinputcatch = input().strip().lower()

        if userinputcatch in commands:
            commands[userinputcatch](data)
        else:
            print("Unknown Command.")

main()