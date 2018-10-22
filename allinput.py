
def logauth(email_list ,password_list ,enter_email ,enter_password):

    while True:
        if enter_email in email_list and enter_password in password_list:
            print("Successful")
            break
        elif enter_email in email_list and enter_password not in password_list:
            print("Invalid password")
            enter_email = input("Please enter your email")
            enter_password = input("Please enter your password")
            continue
        elif enter_email not in email_list and enter_password in password_list:
            print("Invalid email")
            enter_email = input("Please enter your email")
            enter_password = input("Please enter your password")
            continue
        else:
            print("Email and password are inavlid")
            enter_email = input("Please enter your email")
            enter_password = input("Please enter your password")
            continue





