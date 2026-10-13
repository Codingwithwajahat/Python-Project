from pathlib import Path

folder_path = Path("document")


def search_files():
    user_input = input("Enter extension to search (.txt, .pdf): ").lower()

    if folder_path.exists():
        found = False

        for item in folder_path.rglob("*" + user_input):
            file_size = item.stat().st_size
            file_kb = file_size / 1024

            print(f"{item} - {file_kb:.2f} KB")
            found = True

        if not found:
            print("File not found")

    else:
        print("Documents folder not found.")


def read_files():
    user_input = input("Enter the name of file which you want to read: ")

    if folder_path.exists():
        found = False

        for item in folder_path.rglob("*"):
            if item.is_file() and item.name == user_input:
                data = item.read_text(encoding="utf-8")

                print("File content:")
                print(data)
                found = True
                break

        if not found:
            print("File not found")

    else:
        print("Documents folder not found.")


def write_files():
    if folder_path.exists():
        file_name = input("Enter the name of file which you want to create: ")
        file = folder_path / file_name

        if file.exists():
            return "File name already exist. Please write a diff name"

        file_content = input("Enter the content to write on a file: ")
        file.write_text(file_content, encoding="utf-8")

        return "Your file created successfully"

    else:
        return "Documents folder not found."


def rename_file():
    if folder_path.exists():
        file_name = input("Enter the existed name of file which you want to replace: ")
        file = folder_path / file_name

        if not file.exists():
            return "File is not existed. Please write a diff name"

        replace_name = input("Write a name which you want to replace: ")
        replace_file = folder_path / replace_name

        if replace_file.exists():
            return "File name already exist"

        file.rename(replace_file)

        return "Your file rename successfully"

    else:
        return "Documents folder not found."


while True:
    print("\n--- Document Manager ---")
    print("1. Search Files")
    print("2. Read Files")
    print("3. Write Files")
    print("4. Rename Files")
    print("0. Exit")

    user_input = input("Enter your option: ")

    if user_input == "1":
        search_files()

    elif user_input == "2":
        read_files()

    elif user_input == "3":
        print(write_files())

    elif user_input == "4":
        print(rename_file())

    elif user_input == "0":
        print("Program End")
        break

    else:
        print("Enter valid option")