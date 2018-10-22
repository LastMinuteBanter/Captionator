# import facebook
# from tkinter import *
#
# token="EAAHZCAjPO17IBAM6IqGtVyEgzMxnPGiM87yHm72JCu6u5AmhZBkJZBjv9Ix6X6WZBzm4m4wzR1UnmgWJnw0A9XpCF1rorXSmPNp7Ykoxv0ek7mKdJuQZBKN93hO9IZC15Ws1cqljA21CLyiDlapwqhBYhqhDssGCBxa8yxFcfoRwU6hkDbf9abMbKzMuilsPo2MyGCNcB8HgZDZD"
# token2= "EAAHZCAjPO17IBAFrpIJahMtnY6WlQ7S9WQBVMWSl6FPdeq9z1qkz7Cr570z4MZBfAGT6JYCxE0RG5hW4JQbjPJCkjDi9eZAAZBb3LTZBFdVxGrbTtAQmmefUtJPBaVNUWMZCJDGxcvPNuZAO5PjIwrcRVZA4JLivZAkywapwYgmd1DsZAJc3yiSkVgbptW5cvdLHT6XvaVhYagewZDZD"
# fb = facebook.GraphAPI(access_token=token)
# fb2=facebook.GraphAPI(access_token=token2)
#
#
# message = "test"
# fb.put_photo(image=open('test.jpg','rb'),message=message)
# fb2.put_photo(image=open('test.jpg','rb'),message=message)

from tkinter import *
import allinput
root = Tk()
#
# email_list = ["alvinsim00@yahoo.com"]
# password_list = ["1234"]
# enter_email = input("Please enter your email")
# enter_password = input("Please enter your password")

email_label = Label(root, text="Email:")
password_label = Label(root, text="Password:")
email_entry = Entry(root)

email_label.grid(row=0)
password_label.grid(row=1)
#
# allinput.logauth(email_list,password_list,enter_email,enter_password)


root.mainloop()







