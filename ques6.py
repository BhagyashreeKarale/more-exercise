# Socho aapko paas ek list hai jisme kuch values baar baar aa rahi hain. 
# Ek aisa code likho jisse aap ek nayi list banayein jisme iss list ki items ek ek baar hi aaye. 
# Jaise:

# string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
# Aapke code ko iss string_list se ek nayi list banani chaiye jo yeh hogi:

# new_list = ["Rishabh", "Abhishek", "Divyashish"]
# Yeh list dekhiye isme saare naam ek ek baar aa rahe hain. Farak nahi padta ki pichli list mein kitne baar aa rahe the. Samajhne ke liye ek aur example padho

# string_list = ["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai']
# Isse aapke code ko yeh nayi list banani hogi:

# new_list = ["Delhi", "Mumbai", "Chennai"]
# Iss nayi list mein sirf saare shehron ka naam sirf ek baar aa raha hai. Yeh rahi aapki pehli items repeat hone waali list:

string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", "Humble", "Humble"]
# Iss upar di gayi list ka use kar code likho.
new_list=[]
for i in string_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)