# Hum online account banate wakt bahot jagah password set karte hain. 
# Jaise aapne slack aur gmail ka account banate hue bhi apne passwords set kare honge. 
# Humare accounts ke passwords secret hote hain jo kisi ko pata nahi lagna chaiye. 
# Yeh jitne complex honge kisi aur ke liye guess karna utna mushkil ho jayega. 
# Jaise'rahulverma' ko guess karna aasan hai, lekin 'rahul$%verma12!' ko guess karna mushkil hai. 
# Iss vajah se aap jab bhi online account banaoge toh ek acha sakht password set karna important hota hai. 
# Hum iss program mein ek password checker banayenge jo yeh sunchit karega ki humara password strong hai. 
# * Pehle user se ek password ka string input lijiye.
# Fir check kariye ki user ka password sakht hai ya nahi. 
# Ek sakht password ko yeh sab rule follow karne chaiye:
    #Kam se kam uski length 6 honi chaiye
    #Jada se jada length 16 se jyada na ho
    #Kam se kam ek dollar ka sign ($) hona chaiye
    #Kam se kam password mein 2 ya 8 hona chaiye
    #Password mein capital A ya capital Z hona chaiye
# Agar password yeh rules follow kar raha hai toh "Strong Password" print karo, 
# nahi toh "Weak Password" type karo

pinput=input("Enter password:\n")
lnum=len(pinput)
if lnum>=6:
    if lnum<=16:
        if "$" in pinput:
            if "2" in pinput or "8" in pinput:
                if "A" in pinput or "Z" in pinput:
                    print("Strong password!Well done.")
                else:
                    print("Please include capital 'a' or 'z'")
            else:
                print("Please include '2' or '8'")
        else:
            print("Please include a dollar sign($)")
    else:
        print("Maximum length should be 16")
else:
    print("Minimum length should be 6")