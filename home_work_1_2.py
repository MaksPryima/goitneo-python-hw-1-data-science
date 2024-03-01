def parse_input(user_input):
    """
    🔷 ПАРСІНГ INPUT. Розбирає введення користувача на команду та аргументи.
    """
    if not user_input.strip():  # Перевіряємо, чи рядок не є пустим або не містить лише пробіли
        return None
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    🔷 ДОДАВАННЯ КОНТАКТУ  
    """
    try:
        name, phone = args
        if name in contacts:
            return "This name already exist. If you want update contact, use command 'change' {Name} {New Phone}"
        else:
            contacts[name] = phone 
            return "Contact added."
    except:
        return "Enter correct data: add {Name} {New Phone}"

def change_contact(args, contacts):
    """
    🔷 ЗМІНА ДАННИХ КОНТАКТУ
    """
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated." #                  
        else:
            return "This name wasn't found. If you want add new contact ,use command 'add' {Name} {New Phone}"
    except:
        return "Enter correct data: change {Name} {New Phone}"

def show_phone(args, contacts):
    """
    🔷 ПОКАЗАТИ ТЕЛЕФОН
    """
    name = args[0]
    try:
        if name in contacts:
            return contacts[name]
        else:
            return "This name wasn't found."
    except:
        return "Enter correct data: phone {Name}"

def show_all(contacts):
    """
    🔷 ПОКАЗАТИ ВСІ ДОДАНІ КОНТАКТИ
    """
    if contacts:
        all_contacts = ""
        for key, value in contacts.items():
            all_contacts += f"{key}: {value}\n"
        return all_contacts.rstrip("\n")
    else:
        return "You don't have any contact yet"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    try:
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)
            if command in ["close", "exit"]:
                # 🔷 ВИХІД. Команда "close" або "exit". Вивід: "Good bye!" та завершення роботи бота
                print("Good bye!")
                break
            elif command == "hello":
                # 🔷 ПРИВІТАННЯ                   
                print("How can I help you?")
            elif command == "add":
                print(add_contact(args, contacts))
            elif command == "change":
                print(change_contact(args, contacts))
            elif command == "phone":
                print(show_phone(args, contacts))
            elif command == "all":
                print(show_all(contacts))
            else:
                # 🔷 КОМАНДИ ЩО НЕ ВІДПОВІДАЮТЬ ФОРМАТАМ. Вивід: "Invalid command."
                print("Invalid command.")
    except Exception as e: 
        print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()