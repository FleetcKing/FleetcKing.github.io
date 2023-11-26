email = input("enter your email: ")

find = email.find("@")
name = email[:find]
mail = email[find+1:]
print(name)
print(mail)
#another way to do this
name = email[:email.find("@")]
mail = email[email.find("@")+1:]
print(name)
print(mail)