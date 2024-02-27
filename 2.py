def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def upd_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def get_contact(args, contacts):
    name = ''.join(args)
    phone = contacts[name]
    return f"Phone is: {phone}"

def all_contact(contacts):
    for u,p in contacts.items():
        print(f'{u} {p}')

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
            print(upd_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "all":
            print(all_contact(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()