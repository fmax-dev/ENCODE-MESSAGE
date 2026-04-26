import json
import os
import hashlib

# Filename to store user profile credentials
DB_FILE = "profile.json"

# LOAD FILE SO WE CAN COMPARE SAVED/CREATED USER AGAINST DB
def load_user_profile():
    """Load file so that user can authenticate"""
    if not os.path.exists(DB_FILE):
            return {}
    try:
        with open(DB_FILE, 'r') as file:
            return json.load(file)
    except json.JSONDecodeError:
         print("Could not find user")
         return {}

# SAVE USER TO DB
def save_profile(profile):
     """Save user profile to JSON file."""
     with open(DB_FILE, 'w') as file:
          json.dump(profile, file, indent=4)

# CREATE USER
def register_user(profile):
     """Responsible to get user credentials"""
     username = input("\nEnter username: ").lower().strip()
     password = input("Enter password: ").lower().strip()

     if username and password:
          profile[username] = hashlib.sha256(password.encode()).hexdigest()
          save_profile(profile)
          print(f"\n✅ '{username}' created sucessfully.")
          print("Now, login to your account to get started")
     else:
          print("❌ Username and password cannot be empty")
     
     return profile

# COMPARE USER AGAINST DB
def login_user(username, password, profile):
     """Return True/False"""
     hashed = hashlib.sha256(password.encode()).hexdigest()
     if username in profile and profile[username] == hashed:
          return True
     else:
          return False
     
