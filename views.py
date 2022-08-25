import json

json_file = 'data.json'

def json_data():
    with open(json_file) as f:
        return json.load(f)

data = json_data()

def open_for_write():
    with open(json_file, 'w') as f:
        return json.dump(data, f)
        


def create_new():
    global data
    new_laptop = {
        
        "brand": input("Enter brand: "),
        "model": input("Enter model: "), 
        "year": int(input("Enter manufacture year: ")), 
        "description": input("Enter description: "), 
        "price": round(float(input("Enter price: ")), 2)
    }
    data.append(new_laptop)
    open_for_write()
    return "SAVED"

def listing_all():
    return json_data()

def retrieve_one():
    global data
    name = input("Enter brand: ")
    brand = list(filter(lambda x: x['brand'] == name, data))
    if brand:
        return brand[0]
    else: 
        return "UNKNOWN BRAND"

def update_one():
    flag = False 
    global data
    name = input("Enter brand: ")
    brand = list(filter(lambda x: x['brand'] == name, data))
    if not brand:
        return "UNKNOWN BRAND"
    index_ = data.index(brand[0])
    choice = input("\t1 - change brand\n\t2 - change model\n\t3 - change manufacture year\n\t4 - description\n\t5 - price\nEnter your command:")
    if choice == '1':
        brand[index_]['brand'] = input("Enter new brand: ")
        flag = True
    elif choice == "2":
        brand[index_]['model'] = input("Enter new model: ")
        flag = True
    elif choice == "3":
        brand[index_]['manufacture_year'] = int(input('Enter new manufacture year: '))
        flag = True
    elif choice == "4":
        brand[index_]['description'] = input("Enter new description: ")
        flag = True
    elif choice == "5":
        brand[index_]['price'] = round(float(input('Enter a new price: ')), 2)
        flag = True
    else:
        print('UNKNOWN COMMAND')
    open_for_write()
    if flag:
        return "UPDATED"
    else:
        return "NOT UPDATED"


def delete_one():
    global data
    name = input("Enter brand: ")
    brand = list(filter(lambda x: x['brand'] == name, data))
    if not brand:
        return "UNKNOWN BRAND"
    index_ = data.index(brand[0])
    data.pop(index_)
    json.dump(data, open(json_file, 'w'))
    return "DELETED"











