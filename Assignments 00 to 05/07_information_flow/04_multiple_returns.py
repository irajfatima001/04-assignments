def get_user_info():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email_address = input("What is your email address?: ")

    return first_name, last_name, email_address



def main():
    user_data = get_user_info()
    print("\n✅ Received the following user data:")
    print(user_data)

if __name__ == "__main__":
    main()
