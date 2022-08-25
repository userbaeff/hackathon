import json

from views import create_new, delete_one, listing_all, retrieve_one, update_one

def main():
    print("\t1 - добавить товар \n\t2 - вывести полный список\n\t3 - Вывести 1 товар\n\t4 - редактировать товар\n\t5 - удаление товара")
    choice = int(input("Выберите действие: "))
    if choice == 1:
        print(create_new())
    elif choice == 2:
        print(listing_all())
    elif choice == 3:
        print(retrieve_one())
    elif choice == 4:
        print(update_one())
    elif choice == 5:
        print(delete_one())


main()