class My_class:

   def __init__(self, name):
      self.name = name

   def choose_reason(self):
      print("Why is the customer calling?")
      reason_code = int(input("Choose 1 for delivery and 2 for kitchen: "))
      while True:
         if reason_code == 1:
            self.call_delivery()
         elif reason_code == 2:
            self.call_kitchen()
         else:
            print("Please enter a valid value: \n")
            continue

   def call_delivery(self):
      tsp_fail = """
      The delivery did not come, nobody called. Rebooked the delivery and 
      payed the delivery cost to the client.
      """
      tsp_try = """
      The tsp/we called the customer and asked to rebook the delivery.
      Delayed service. Rebooked the order.
      """
      customer_fail = """
      The tsp called the client but could not reach. Rebooked the delivery.
      Customer pays for the new delivery.
      """
      while True:
         user_input = int(input("Please enter the couse: (1,2,3) "
                                "\n"))
         if user_input == 1:
            print(tsp_fail)
            break
         elif user_input == 2:
            print(tsp_try)
            break
         elif user_input == 3:
            print(customer_fail)
            break
         else:
            print("Please enter a valid value")
            continue

   def call_kitchen(self):
      sail_fail = """
      The sail assitant made a misstake in the drawing. Exchange the items.
      """
      ordered_workingtop = """
      The working top is special orderd size. It had been damaged in the 
      delivery. Check the pictures in the link below.
      """
      while True:
         user_input = int(input("Please enter the couse: (1,2) "
                                "\n"))
         if user_input == 1:
            print(sail_fail)
            break
         elif user_input == 2:
            print(ordered_workingtop)
            break
         else:
            print("Please enter a valid value")
            continue


user1 = My_class("Asya")
user1.choose_reason()
# user1.call_kitchen()
