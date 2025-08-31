import os

# Set your diary password
DIARY_PASSWORD = "1234"

# Function to check password
def check_password():
    pwd = input("Enter Diary Password: ")
    return pwd == DIARY_PASSWORD

# Function to add an entry
def add_entry():
    entry = input("Write your diary entry: ")
    with open("diary.txt", "a") as file:
        file.write(entry + "\n")
    print("✅ Entry saved successfully!\n")

# Function to view all entries
def view_entries():
    if os.path.exists("diary.txt"):
        with open("diary.txt", "r") as file:
            content = file.read()
            print("\n📖 Your Diary Entries:\n")
            print(content)
    else:
        print("📂 No entries found yet.\n")

# Main program
def main():
    print("🔒 Welcome to Personal Diary 🔒\n")
    if not check_password():
        print("❌ Wrong password! Access Denied.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Exit")

        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("👋 Goodbye! See you next time.")
            break
        else:
            print("⚠️ Invalid choice, try again!")

# Run the program
if __name__ == "__main__":
    main()
