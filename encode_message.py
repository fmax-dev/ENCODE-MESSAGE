import os
import json
import user_profile

# Filename to store user encoded messages
DATA_FILE = "saved_encoded_messages.json"

def save_encoded_message(message, shift_num):
    """Save an encoded message and its shift to the data file."""
    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)

    data.append({"message": message, "shift": shift_num})

    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# DISPLAY A MENU
def view_encoded_message(username, password, profile):
    """Allow users to view their encoded messages."""
    if user_profile.login_user(username, password, profile):
        if not os.path.exists(DATA_FILE):
            print("\nNo encoded messages found.")
            return

        with open(DATA_FILE, 'r') as file:
            data = json.load(file)

        if not data:
            print("\nNo encoded messages found.")
            return

        print("\n--- All Encoded Messages: ---")
        for i, entry in enumerate(data, start=1):
            print(f"    {i}. {entry['message']}")
        print("---------------------")
    else:
        print("Please login first")

# 2. COLLECTING user Inputs
def gathering_user_inputs():
    """Collecting user secret message and shift number."""
    # User secret message
    user_message = input("\nEnter your message: ").lower().strip()

    # Shift number
    shift = input("Enter your shift number: ").strip()
    shift_num = int(shift) if shift.isdigit() else 3

    return user_message, shift_num

def create_encode_message(user_message, shift_num):
    """Create the encode message"""
     # 1. DEFINING a string containing all the alphabet letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Empty string to store the encode message
    secret_message = ""

    for char in user_message:
        if char in alphabet:
            current_position = alphabet.index(char)

            # CALCULATING NEW POSITION
            # (CURRENT POSITION + SHIFT NUMBER) % 26
            new_position = (current_position + shift_num) % 26
            secret_message += alphabet[new_position]
        else:
            secret_message += char      # Handle non-letters
    print(f"\nHere's your secret message: {secret_message}")
    return secret_message

# Authentication flow
def auth():
    """Allow users to create or login into their account."""

    print("\nCreate or login into your account to get started")

    profile = user_profile.load_user_profile()

    while True:
        print("\n1. Create account")
        print("2. login")
        auth_choice = input("\nSelect an option: ").strip()

        if auth_choice == "1":
            profile = user_profile.register_user(profile)
        
        elif auth_choice == "2":
            while True:
                username = input("\nEnter username: ").lower().strip()
                password = input("Enter password: ").lower().strip()
                if user_profile.login_user(username, password, profile):
                    break
                else:
                    print("\n❌ Invalid credentials. Try again.")
                
            print(f"\n✅ Welcome back, {username}!")
            break
        else:
            print("\nError: Please select a valid option.")
        
    return username, password, profile

def decode_message():
    """Allow users to decode an encoded message."""
    if not os.path.exists(DATA_FILE):
        print("\nNo encoded messages found to decode.")
        return

    with open(DATA_FILE, 'r') as file:
        data = json.load(file)

    if not data:
        print("\nNo encoded messages found to decode.")
        return

    print("\n--- All Encoded Messages: ---")
    for i, entry in enumerate(data, start=1):
        print(f"    {i}. {entry['message']}")
    print("-----------------------------")

    choice = input("\nSelect a message to decode: ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(data)):
        print("\nError: Invalid selection.")
        return

    entry = data[int(choice) - 1]
    shift_num = entry["shift"]

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded = ""
    for char in entry["message"]:
        if char in alphabet:
            current_position = alphabet.index(char)
            new_position = (current_position - shift_num) % 26
            decoded += alphabet[new_position]
        else:
            decoded += char

    print(f"\nDecoded message: {decoded}")


def main():
    
    print("\n========== WELCOME ==========")

    # AUTH
    username, password, profile = auth()

    # MENU
    while True:
        print("\nAll available options:")
        print(" 1. Encode a new message")
        print(" 2. View encoded messages")
        print(" 3. Decode a message")
        print(" 4. Logout")

        user_choice = input("\nSelect an option: ").strip()

        # ROUTING LOGIC
        if user_choice == "1":
            user_message, shift_num = gathering_user_inputs()
            secret_message = create_encode_message(user_message, shift_num)
            save_encoded_message(secret_message, shift_num)

        elif user_choice == "2":
            view_encoded_message(username, password, profile)
        elif user_choice == "3":
            decode_message()
        elif user_choice == "4":
            print("\n✅ Successfully logged out")
            break
        else:
            print("\nError: Please select a valid option")


if __name__ == "__main__":
    main()