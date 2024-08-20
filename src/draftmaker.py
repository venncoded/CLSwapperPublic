name = input("What is your name? ")
town = input("What town do you live in? ")
state=input("State? ")
zipcode=input("Zipcode? ")
mailaddress=input("What is your mailing address? ")
phonenumber=input("What is your phone number? ")
email=input("What is your email? ")

content = ''
with open("draft.txt",'r') as draft:
        content = str(draft.read())
        content=content.replace("?name?",name)
        content=content.replace("?address?",mailaddress)
        content=content.replace("?tsz?",town+" "+state+", " +str(zipcode))
        content=content.replace("?number?",phonenumber)
        content=content.replace("?email?",email)
with open("draft.txt",'w') as draft:
        draft.write(content)