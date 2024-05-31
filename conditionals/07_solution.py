order_size = {"chai" , "coffe" , "Green tea"}

order_list = list(order_size)

print("Order Size : " , order_list)

extra_short = True



order_choice = input("Please Enter Your Order : ")

order_type = str(order_choice).lower()

if extra_short :
  print("Order : " , {order_type} )
else:
  print("No Order")