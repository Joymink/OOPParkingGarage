class Parking():
    def __init__(self, tickets, parkingSpaces, currentTicket):
        self.tickets=tickets
        self.parkingSpaces= parkingSpaces
        self.currentTicket=currentTicket
    
    def takeTicket(self):
        del(self.tickets[-1])
        del(self.parkingSpaces[-1])

    def payForParking(self): 
        payment=-15
        left = 15
        if self.currentTicket["paid"]==False:
            while payment <0:
                num= int(input(f"Insert Cash ${left} to pay for parking ticket: "))
                payment+=num
                left-=num
                if payment ==0:
                    print("Thank you for paying the ticket.\nYou have 15 minutes to exit the parking structure")
                    self.currentTicket["paid"]=True
                    break
                elif payment >0:
                    print("Thank you for paying the ticket.\nYou have 15 minutes to exit the parking structure")
                    print(f'Your change is ${payment}')
                    self.currentTicket["paid"]=True
                    break
        else: 
            print("Looks like your ticket is already paid.")
            
    def leaveGarage(self):

        if self.currentTicket["paid"]==True:
            print("Thank you, have a nice day!")
        else:
            self.payForParking()
            print("Thank you, have a nice day!")
        self.parkingSpaces.append("Space")
        self.tickets.append(self.currentTicket)


def fillList(list1, howBig, item):
    for i in range(0,howBig):
        list1.append(item)


tickets=[]
parkingSpaces=[]
ticket ={
    "paid": False,

}
fillList(tickets,10, ticket)
fillList(parkingSpaces,10, "Space")



garage=Parking(tickets, parkingSpaces, ticket)

x=0
while True:
    prompt= input("Would you like to enter the parking garage?")
    if prompt.lower()=="yes":
        if garage.parkingSpaces==[]:
            print("Sorry the Garage is full")
            print("Have a nice day!")
            break
        else: 
            print("---Printing ticket---")
            garage.takeTicket()
            print("You may now enter the garage")
            
            while x==0:
                prompt2= input("Would you like to pay ticket (1) or exit garage (2)?")
                if prompt2.lower()=="2":
                    prompt3=input("Did you pay for your ticket?")
                    if prompt3.lower()=="yes" :   
                        garage.leaveGarage()
                    else:
                        garage.payForParking()
                        garage.leaveGarage()
                    x=1
                elif prompt2.lower()=="1":
                    garage.payForParking()
                else:
                    print("Please Try again")
            break
    else:
        print("Okay Have a nice day!")
        break

                




        

