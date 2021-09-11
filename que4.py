# input ka use kar ke 3 alag variables mein 3 integers ka input lein. 
# Input lene ke baad inn 3 mein se sabse bade number ko print karo 
# Note: Isme aap loops ka use nahi kar sakte.
n1=int(input("Enter a value"))
n2=int(input("Enter a value"))
n3=int(input("Enter a value"))
if n1 > n2 and n1 > n3:
    print(n1,"is the largest among the entered three numbers")
elif n2 > n1 and n2 > n3:
    print(n2,"is the largest among the entered three numbers")
else:
    print(n3,"is the largest among the entered values")
