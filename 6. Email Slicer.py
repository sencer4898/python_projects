
def emailSlicer(email):
    f_a = email.split('@')
    username = f_a[0]
    domain = f_a[1]
    print("Username:",username,"Domain:",domain)

run = False
while run:
    email = input("Enter email: ")
    if email == 'quit':
        quit
    emailSlicer(email)
