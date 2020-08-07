import random

# Contact Book

# Name, Adress, Phone Number, Email

# Add, Find, Update, Delete, List

class ContactBook():
    Book = {}
    a = list(range(0,5))
    def finder(self,name):
        for id in self.Book:
            if self.Book[id][0]==name:                
                return id
        return False
    def addContact(self,name,adress,phone,email):
        exists = self.finder(name)
        if not exists:
            newId = random.choice(self.a)
            self.a.remove(newId)
            self.Book[newId] = [name,adress,phone,email]
            print("Person added.")
        else:
            print("This person already exists.")
    def findContact(self,name):
        exists = self.finder(name)
        if exists:
            print(self.Book[exists])
        else:
            print("There is no such a person in your contacts.")
    def deleteContact(self,name):
        id = self.finder(name)
        del self.Book[name]
        return id
    def updateContact(self,name,nameNew,adressNew,phoneNew,emailNew):
       id = self.deleteContact(name)
       self.Book[id] = [nameNew,adressNew,phoneNew,emailNew]
    def listContacts(self):
        for id in self.Book:
            print(self.Book[id])


myContactBook = ContactBook()

print("Welcome to the ContactBook application.")
quit = False
while not quit:
    action = input("""
    What would you like to perform?
    1. Add a contact
    2. Find a contact
    3. Delete a contact
    4. Update a contact
    5. List all the contacts
    6. Quit the application""")

    if action== '1':
        print("-----Add a new person-----")
        nameIn = input("Name: ")
        adressIn = input("Adress: ")
        phoneIn = input("Phone: ")
        emailIn = input("Email: ")
        myContactBook.addContact(nameIn,adressIn,phoneIn,emailIn)
    elif action== '2':
        nameIn = input("Who would you like to find? ")
        myContactBook.findContact(nameIn)
    elif action== '3':
        nameIn = input("Who would you like to delete? ")
        myContactBook.deleteContact(nameIn)
    elif action== '4':
        nameIn = input("Who would you like to update? ")
        newNameIn = input("New name: ")
        newAdressIn = input("New adress: ")
        newPhoneIn = input("New phone: ")
        newEmailIn = input("New email: ")
        myContactBook.updateContact(nameIn,newNameIn,newAdressIn,newPhoneIn,newEmailIn)
    elif action== '5':
        myContactBook.listContacts()
    elif action == '6':
        quit = True
    else:
        print("Invalid command.")


print("Thanks for choosing us!")
