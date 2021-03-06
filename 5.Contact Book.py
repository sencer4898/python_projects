import random

# Contact Book

# id, Name, Adress, Phone Number, Email

# Add, Find, Update, Delete, List


class ContactBookClass():
    ContactBook = {}

    idList = list(range(0,100))   #0 1 2    100

    def finder(self,nameIn):
        for id in self.ContactBook:
            if self.ContactBook[id][0] == nameIn:
                return id
        return 0


    def addContact(self,nameIn,adressIn,phoneIn,emailIn):
        id = random.choice(self.idList)
        self.idList.remove(id)
        self.ContactBook[id] = [nameIn,adressIn,phoneIn,emailIn]
        print("Contact added.")
    def findContact(self,nameIn):
        id = self.finder(nameIn)
        if id:
            print("Name:",self.ContactBook[id][0])
            print("Adress:",self.ContactBook[id][1])
            print("Phone Number:",self.ContactBook[id][2])
            print("Email Adress:",self.ContactBook[id][3])
        else:
            print("There is no such person in your contacts.")
    def deleteContact(self,nameIn):
        id = self.finder(nameIn)
        if id:
            del self.ContactBook[id]
            self.idList.append(id)
            print("Contact deleted.")
        else:
            print("There is no such person in your contacts.")
    def updateContact(self,nameIn,newNameIn,newAdressIn,newPhoneIn,newEmailIn):
        id = self.finder(nameIn)
        self.ContactBook[id][0] = newNameIn
        self.ContactBook[id][1] = newAdressIn
        self.ContactBook[id][2] = newPhoneIn 
        self.ContactBook[id][3] = newEmailIn
        print("Contact updated.")
    def listContacts(self):        
        for id in self.ContactBook:
            a = self.ContactBook[id]
            print(f"Name: {a[0]} Adress: {a[1]} Phone: {a[2]} Email: {a[3]}")
            

quit = False
myContacts = ContactBookClass()
print("Welcome to the ContactBook application.")
while not quit:
    action = input("""------------------------------
    What would you like to perform?
    1. Add a contact
    2. Find a contact
    3. Delete a contact
    4. Update a contact
    5. List all the contacts
    6. Quit the app
    -----------------------
    Choice: """).strip()

    if action=='1':
        name = input("Enter the name: ")
        if myContacts.finder(name):
            print("This person already exists.")
        else:
            adress = input("Enter the adress: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            myContacts.addContact(name,adress,phone,email)

    elif action=='2':
        name = input("Who would you like to find? ")
        myContacts.findContact(name)
    elif action=='3':
        name = input("Who would like to get out of your contacts? ")
        myContacts.deleteContact(name)
    elif action=='4':
       name = input("Which contact would you like to update? ")
       if myContacts.finder(name):
          newName = input("Enter the new name: ")
          newAdress = input("Enter the new adress: ")
          newPhone = input("Enter the new phone number: ")
          newEmail = input("Enter the new email: ")
          myContacts.updateContact(name,newName,newAdress,newPhone,newEmail)
       else: 
          print("There is no such contact in your book.")
    elif action=='5':
        myContacts.listContacts()
    elif action=='6':
        quit = True
    else:
        print("Please enter a valid command.")
print("Thanks for choosing us. See you next time.")
