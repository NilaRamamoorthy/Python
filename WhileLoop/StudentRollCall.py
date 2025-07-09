#1. Student Roll Call System
entry=1
while entry<11:
       student=input("Enter Your Name: ").strip()   
       if student=="":
         continue
       else:
          entry+=1
        
else:
    print("Attendance Completed!")
