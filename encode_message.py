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
def view_encoded_message(DATA_FILE):
    """Allow users to view their encoded messages."""
    with open(DATA_FILE, 'r') as file:
        lines = file.read().splitlines()

    # print("--- ALL ENCODED MESSAGES: ---")
    # print(f" {lines}")
    # print("---------------------")

    print("\n--- All Encoded Messages: ---")
    for i, line in enumerate(lines, start=1):
        print(f"    {i}. {line}")
    print("---------------------")

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

    print("\nAll available options:")
    print("1. Encode a new message")
    print("2. View encoded messages")

    user_choice = input("\nSelect an option: ").strip()

    # Logic
    if user_choice == "1":
        user_message, shift_num = gathering_user_inputs()
        secret_message = create_encode_message(user_message, shift_num)
        append_to_file(secret_message)

    elif user_choice == "2":
        view_encoded_message(DATA_FILE)
    else:
        print("\nError: Please select a valid option")


if __name__ == "__main__":
    encode_message()