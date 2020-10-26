gpa = float (input("gpa: "))
lecture = float (input("lecture: "))
if (gpa<2.0):
  if (lecture<47):
    print ("not enough lectures and gpa")
  elif (lecture >= 47):
    print("not enogh gpa")
elif (gpa>=2.0):
   if (lecture < 47):
     print("not enough lecture")
   elif(lecture>=47):
     print("graduated")  
