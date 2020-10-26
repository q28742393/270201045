ticket_price = 3
age = int(input("how old are you? "))

if (age<6 or age>60):
  print("free")
elif (6<age<18):
  print(ticket_price/2)
else:
  print(ticket_price)  
