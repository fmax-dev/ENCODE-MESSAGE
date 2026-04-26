import user_profile

# Filename to store user encoded messages
DATA_FILE = "saved_encoded_messages.txt" 

def append_to_file(user_message):
    """Save an encoded message to the data file."""
    try:
        with open(DATA_FILE, 'a') as file:
            file.write(user_message + "\n")
        return True  # Indicate success
    except IOError:  # Catch actual file I/O errors
        return False  # Indicate failure

# DISPLAY A MENU
def view_encoded_message(DATA_FILE, username, password, profile):
    """Allow users to view their encoded messages."""
    if user_profile.login_user(username, password, profile):
        with open(DATA_FILE, 'r') as file:
            lines = file.read().splitlines()

        print("\n--- All Encoded Messages: ---")
        for i, line in enumerate(lines, start=1):
            print(f"    {i}. {line}")
        print("---------------------")
    else:
        print("Please login first")

    return

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

def encode_message():
    
    print("\n========== WELCOME ==========")

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


    while True:
        print("\nAll available options:")
        print("1. Encode a new message")
        print("2. View encoded messages")
        print("3. Logout")

        user_choice = input("\nSelect an option: ").strip()

        # Logic
        if user_choice == "1":
            user_message, shift_num = gathering_user_inputs()
            secret_message = create_encode_message(user_message, shift_num)
            append_to_file(secret_message)

        elif user_choice == "2":
            view_encoded_message(DATA_FILE, username, password, profile)
        elif user_choice == "3":
            print("\n✅ Successfully logged out")
            break
        else:
            print("\nError: Please select a valid option")


if __name__ == "__main__":
    encode_message()