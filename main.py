from datetime import datetime, timedelta
from collections import UserDict
from classes import Field, Name, Phone, Birthday, Record, AddressBook
from getbirthday import get_birthdays_per_week

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except (KeyError, IndexError):
            return "Invalid input. Check your data."
        except Exception as e:
            return f"An error occurred: {str(e)}"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error    
def add_contact(args, address_book):
    if len(args) >= 2:
        name = args[0]
        # Combine the remaining elements in args to form the phone number
        phone = ' '.join(args[1:])
        record = Record(name)
        record.add_phone(phone)
        address_book.add_record(record)
        return "Contact added."
    else:
        return "Invalid command. Please provide both name and phone number."

def hello():
    return "How can I help you?"

@input_error
def change_contact(address_book, name, new_phone):
    record = address_book.find(name)
    if record:
        record.edit_phone(record.phones[0].value, new_phone)
        return "Contact updated."
    else:
        return "Contact not found."

@input_error
def show_phone(address_book, name):
    record = address_book.find(name)
    return record.phones[0].value if record else "Contact not found."

@input_error
def show_all(address_book):
    if address_book.data:
        return "\n".join([str(record) for record in address_book.data.values()])
    else:
        return "No contacts available."
    
@input_error
def add_birthday(address_book, name, birthday):
    record = address_book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    else:
        return "Contact not found."
    
@input_error
def show_birthday(address_book, name):
    record = address_book.find(name)
    return record.show_birthday() if record else "Contact not found."

@input_error
def print_birthdays_per_week(address_book):
    users = [{"name": name, "birthday": record.show_birthday()} for name, record in address_book.data.items()]
    return get_birthdays_per_week(users)

def main():
    address_book = AddressBook()
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print(hello())
        elif command == "add" and len(args) >= 2:
            print(add_contact(args, address_book))
        elif command == "change" and len(args) == 2:
            print(change_contact(address_book, args[0], args[1]))
        elif command == "phone" and len(args) == 1:
            print(show_phone(address_book, args[0]))
        elif command == "all" and not args:
            print(show_all(address_book))
        elif command == "add-birthday" and len(args) == 2:
            print(add_birthday(address_book, args[0], args[1]))
        elif command == "show-birthday" and len(args) == 1:
            print(show_birthday(address_book, args[0]))
        elif command == "birthdays" and not args:
            results = print_birthdays_per_week(address_book)
        else:
            print("Invalid command.")
        
if __name__ == "__main__":
    main()


