# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

# By the end of this project each group/student should be able to:
# - Explain and/or demostrate using Git and Github for collaboration
# - Explain and/or demostrate creating classes
# - Explain and/or demostrate creating class methods
# - Explain and/or demostrate class instantiation


# When the project is completed, commit the final changes, sync all pull requests, and each member should submit their respective GitHub links(though the code in each should be the same)




class Parking_Metropolis():

     # Attributes
   
#   def __init__(): # Delete? What is this doing?

    def __init__(self):
       self.tickets = []
       self.parkingSpaces = []
       self.currentTicket = {} 

       # Your parking gargage class should have the following methods:
            #takeTicket
                # - This should decrease the amount of tickets available by 1
                # - This should decrease the amount of parkingSpaces available by 1
    
    def takeTicket(self):
       self.tickets = list(range(1,51))
       self.parkingSpaces = self.tickets 
       self.ticket_number = self.tickets.pop()
       self.parking_spaces = self.parkingSpaces.pop()
       self.currentTicket[self.ticket_number]["paid"] = False

# - payForParking
   # - Display an input that waits for an amount from the user and store it in a variable
   # - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
   # - This should update the "currentTicket" dictionary key "paid" to True

    def payForParking(self):
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

    def leaveGarage(self):
       if self.ticket_number == True:
          print("Your ticket has been paid. Have a nice day!")
          self.parking_spaces += 1
          self.tickets += 1
       else:
          print("Please post payment!")



   #=============Calling class ================

def run():
   my_parking_spot = Parking_Metropolis() 
 
   while True:
      response = input("What would you like to do?: Take ticket, Pay, Leave, Exit: ").upper().strip()
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
         print("Error. Not a valid response.")

run()