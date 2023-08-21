
class Parking_Metropolis():

   
    def __init__(self):
<<<<<<< HEAD
       self.currentTicket = {}
=======
       self.tickets = []
       self.parkingSpaces = []
       self.currentTicket = {} 

       # Your parking gargage class should have the following methods:
            #takeTicket
                # - This should decrease the amount of tickets available by 1
                # - This should decrease the amount of parkingSpaces available by 1
    
    def takeTicket(self):
>>>>>>> 8b8628a0c00a508cde04bfa9fd9d225b75aaae9b
       self.tickets = list(range(1,51))
       for t in self.tickets:
          self.currentTicket[t] = {
             "paid" : False, 
             "vacant": True
          }
   

    def takeTicket(self):
      ticket_number = 0
      
      for t in self.currentTicket:
         if self.currentTicket[t]["vacant"] == True:
            self.currentTicket[t]["vacant"] = False
            print(f"Your ticket number is {t}.")
            ticket_number = t
            break
      if ticket_number == 0:
         print("It's a busy day! No parking spaces available.")


    def payForParking(self):
<<<<<<< HEAD
      self.price = 40
      ticket_number = int(input(f"What is your ticket number? "))
      print(f" You owe {self.price} dollars.")
      if self.currentTicket[ticket_number]["paid"] == True:
         print("This ticket has already been paid.")
      else:
         amount_paid = int(input(f"Enter your payment amout here: "))
         if amount_paid == self.price:
            self.currentTicket[ticket_number]["paid"] = True
            
            print("Your ticket has been paid in full. Exit the premises in an orderly manner.")
            return True
         else:
            self.price = self.price - amount_paid
            print(f"You still owe {self.price} dollars. Must pay in full before leaving.")
            return self.price
=======
         while True:
            self.price = 40
            self.payment = int(input(f"{self.price} dollars please: "))
            if self.payment != self.price:
                print("Your ticket has not been paid!")
            else:
                print("Your ticket has been paid and you have 15mins to leave")
                self.currentTicket[self.ticket_number]["paid"] = True
                break



# -leaveGarage
   # - If the ticket has been paid, display a message of "Thank You, have a nice day"
   # - If the ticket has not been paid, display an input prompt for payment
   # - Once paid, display message "Thank you, have a nice day!"
   # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
   # - Update tickets list to increase by 1 (meaning add to the tickets list)
>>>>>>> 8b8628a0c00a508cde04bfa9fd9d225b75aaae9b

               
    def leaveGarage(self):
<<<<<<< HEAD
      ticket_number = int(input(f"What is your ticket number? "))
      if self.currentTicket[ticket_number]["paid"] == False:
         print("There is no free parking here. You must pay before leaving.")
         return False
         
      else:
         self.currentTicket[ticket_number]["vacant"] = True
         print(" Thank you for enjoying reliable parking at your Parking Metropolis!! \n Now scram. ")
=======
       if self.ticket_number == True:
          print("Your ticket has been paid. Have a nice day!")
          self.parking_spaces += 1
          self.tickets += 1
       else:
          print("Please post payment!")
>>>>>>> 8b8628a0c00a508cde04bfa9fd9d225b75aaae9b


   #=============Calling class ================= Wrong number ===== Ha Ha =========

def run():
   my_parking_spot = Parking_Metropolis() 
 
   while True:
<<<<<<< HEAD
      print()
      response = input("\tWhat would you like to do?: Take ticket, Pay, Leave, Exit: ").upper().strip()
=======
      response = input("What would you like to do?: Take ticket, Pay, Leave, Exit: ").upper().strip()
>>>>>>> 8b8628a0c00a508cde04bfa9fd9d225b75aaae9b
      if response == 'TAKE TICKET':
         my_parking_spot.takeTicket()
      elif response == 'PAY':
         my_parking_spot.payForParking()
      elif response == 'LEAVE':
         my_parking_spot.leaveGarage()
      elif response == 'EXIT':
         print("Thank you! Please come again.")
         break
      else:
         print("Error. Not a valid response. Try again a hundred more times before freaking out.")

run()