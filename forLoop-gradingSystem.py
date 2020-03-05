#Grading system.
#if else
#subject and marks
print("subject and marks")
print("ENTER MARKS AGAINST THE SUBJECTS BELOW")
OOP=int(input("enter marks for OOP;"))
OOSAD=int(input("enter marks for OOSAD;"))
MULTIMEDIA=int(input("enter marks MULTIMEDIA;"))
ETHICS=int(input("enter marks for ETHICS;"))
HCNA=int(input("enter marks for HCNA;"))
print("")
print("OOP=",OOP)
print("OOSAD=",OOSAD)
print("MULTIMEDIA=",MULTIMEDIA)
print("ETHICS=",ETHICS)
print("HCNA=",HCNA)
print("")
#CLACULATING AVERAGE
Avg=(OOP+OOSAD+MULTIMEDIA+ETHICS+HCNA)/5
print("average=",Avg)

#BEGING OF IF ELSE STATEMENT
if Avg >=80 and Avg<=100:
    print("GRADE IS A")
elif Avg>=70 and Avg<=79:
    print("GRADE IS B")
elif Avg>=70 and Avg<=79:
    print("GRADE IS B")
elif Avg>=60 and Avg<=69:
    print("GRADE IS C")
elif Avg>=50 and Avg<=59:
    print("GRADE IS D")
elif Avg>0 and Avg<=49:
    print("GRADE IS Fail")
else:
    print("Marks error, please try again")


    





