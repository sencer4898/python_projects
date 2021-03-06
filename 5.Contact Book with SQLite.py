import random
import sqlite3

# Contact Book

# id, Name, Adress, Phone Number, Email

# Add, Find, Update, Delete, List



class ContactBookClass():
    con = sqlite3.connect("ContactBook.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Contact_Book(id INT, name TEXT, adress TEXT, phone TEXT, email TEXT)")


    idList = list(range(1,100))   # 1 2    100

    def finder(self,nameIn):
        rowWithName = list(self.cursor.execute("SELECT id FROM Contact_Book WHERE name = ?",(nameIn,)))
        if len(rowWithName)==0:
            return 0
        else:
            for index in rowWithName:
                return index[0]
            

    def addContact(self,nameIn,adressIn,phoneIn,emailIn):
        id = random.choice(self.idList)
        self.idList.remove(id)
        self.cursor.execute("INSERT INTO Contact_Book VALUES(?,?,?,?,?)",(id,nameIn,adressIn,phoneIn,emailIn))
        self.con.commit()
        print("Contact added.")
    def findContact(self,nameIn):
        id = self.finder(nameIn)
        if id:
            a = list(self.cursor.execute("SELECT * FROM Contact_Book Where id =?",(id,)))
            print("Id: ",a[0][0])
            print("Name:",a[0][1])
            print("Adress:",a[0][2])
            print("Phone Number:",a[0][3])
            print("Email Adress:",a[0][4])
        else:
            print("There is no such person in your contacts.")
    def deleteContact(self,nameIn):
        id = self.finder(nameIn)
        if id:
            self.cursor.execute("DELETE FROM Contact_Book WHERE id = ?",(id,))
            self.con.commit()
            self.idList.append(id)
            print("Contact deleted.")
        else:
            print("There is no such person in your contacts.")
    def updateContact(self,nameIn,changeColumn,newInfo):
        id = self.finder(nameIn)
        if changeColumn == 'name':
            self.cursor.execute("UPDATE Contact_Book SET name = ? WHERE name = ?",(newInfo,nameIn))
            self.con.commit()
            print("Contact updated.")
        elif changeColumn == 'adress':
            self.cursor.execute("UPDATE Contact_Book SET adress = ? WHERE name = ?",(newInfo,nameIn))
            self.con.commit()
            print("Contact updated.")
        elif changeColumn == 'phone':
            self.cursor.execute("UPDATE Contact_Book SET phone = ? WHERE name = ?",(newInfo,nameIn))
            self.con.commit()
            print("Contact updated.")
        elif changeColumn == 'email':
            self.cursor.execute("UPDATE Contact_Book SET email = ? WHERE name = ?",(newInfo,nameIn))
            self.con.commit()
            print("Contact updated.")
        else:
            print("Wrong input.")
        
    def listContacts(self):        
        a = list(self.cursor.execute("SELECT * FROM Contact_Book"))
        for index in a:
            print(index[0],index[1],index[2],index[3],index[4])
            

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
          changeColumn = input("What do you want to change? ")
          newInfo = input("What would you want it to be? ")
          myContacts.updateContact(name,changeColumn,newInfo)
       else: 
          print("There is no such contact in your book.")
    elif action=='5':
        myContacts.listContacts()
    elif action=='6':
        quit = True
    else:
        print("Please enter a valid command.")
print("Thanks for choosing us. See you next time.")
