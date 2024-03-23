def input_error(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError Give me name and phone please."
        except ValueError:
            return "ValueError Give me name and phone please."
        except IndexError:
            return "IndexError Give me name to show the phone number"
    return handler


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        raise ValueError
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        name, phone = args
    contacts[name] = phone
    return "Contact updated successfully"

@input_error
def show_contact(args, contacts):
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "No such contact"
    
def show_all(contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()