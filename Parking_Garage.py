
class Parking_Metropolis():

   
    def __init__(self):
       self.currentTicket = {}
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

               
    def leaveGarage(self):
      ticket_number = int(input(f"What is your ticket number? "))
      if self.currentTicket[ticket_number]["paid"] == False:
         print("There is no free parking here. You must pay before leaving.")
         return False
         
      else:
         self.currentTicket[ticket_number]["vacant"] = True
         print(" Thank you for enjoying reliable parking at your Parking Metropolis!! \n Now scram. ")


   #=============Calling class ================= Wrong number ===== Ha Ha =========

def run():
   my_parking_spot = Parking_Metropolis() 
 
   while True:
      print()
      response = input("\tWhat would you like to do?: Take ticket, Pay, Leave, Exit: ").upper().strip()
      if response == 'TAKE TICKET':
         my_parking_spot.takeTicket()
      elif response == 'PAY':
         my_parking_spot.payForParking()
      elif response == 'LEAVE':
         my_parking_spot.leaveGarage()
      elif response == 'EXIT':
         print("Thank you. Please come again.")
         break
      else:
         print("Error. Not a valid response. Try again a hundred more times before freaking out.")

run()