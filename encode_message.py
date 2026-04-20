# THE SECRET MESSAGE ENCODER

def gathering_user_inputs():
    """Collecting user secret message and shift number."""
    # User secret message
    user_message = input("\nEnter your message: ").lower().strip()

    # Shift number
    shift = input("Enter your shift number: ").strip()
    shift_num = int(shift) if shift.isdigit() else 3

    return user_message, shift_num

def encode_message():
    # Empty string to store the encode message
    secret_message = ""
    
    print("\n========== WELCOME ==========")

    # 1. DEFINING a string containing all the alphabet letters
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # 2. COLLECTING user Inputs
    user_message, shift_num = gathering_user_inputs()

    # Transformation Process
    for char in user_message:
        if char in alphabet:
            current_position = alphabet.index(char)

            # CALCULATING NEW POSITION
            # (CURRENT POSITION + SHIFT NUMBER) % 26
            new_position = (current_position + shift_num) % 26
            secret_message += alphabet[new_position]
        else:
            secret_message += char      # Handle non-letters
    print(f"Here's your secret message: {secret_message}")



if __name__ == "__main__":
    encode_message()