from hashlib import sha256

def login(email, stored_logins, password_to_check):


    if stored_logins[email] == hash_password(password_to_check):
        return True

    return False

# This function hashes the password using SHA256 and returns the hashed value
def hash_password(password):

    return sha256(password.encode()).hexdigest()

def main():
    # stored_logins is a dictionary with emails as keys and hashed passwords as values
    stored_logins = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",  # hash of "password"
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",  # hash of "Karel"
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"  # hash of "123!456?789"
    }

    # Test cases with different login attempts
    print(login("example@gmail.com", stored_logins, "word"))  # Should return False
    print(login("example@gmail.com", stored_logins, "password"))  # Should return True

    print(login("code_in_placer@cip.org", stored_logins, "Karel"))  # Should return True
    print(login("code_in_placer@cip.org", stored_logins, "karel"))  # Should return False (case sensitive)

    print(login("student@stanford.edu", stored_logins, "password"))  # Should return False
    print(login("student@stanford.edu", stored_logins, "123!456?789"))  # Should return True

# Python boilerplate to call the main function
if __name__ == '__main__':
    main()
