# Question 11
# Google jaise bade search engine ek web page pe saare text ko samajhte hain. 
# Fir aap kuch bhi search karo, toh google sahi webpages dikha deta hai. 
# Inn sab kaam ke liye google ko ek page se saare words nikalne padte hain. 
# Hume pehle ek poore paragraph mein se words nikalne hain. 
# Iske liye pehle strings mein se hume words nikalne padenge. 
# Socho aapke paas ek string hai.

sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
# wlist=sentence.split()
# print(wlist)
# Aapne ek break_into_words naam ka function likhna hai, 
# jo ek parameter lega jisme ek string hoga. 
# Isko jab hum ek words ka string denge. 
# Jaise break_into_words(sentence) doge toh usko ek words ki list return karni hai. 
# Jaise aapke break_into_words(sentence) ki output yeh honi chaiye:
# ['NavGurukul', 'is', 'an', 'alternative', 'to', 'higher', 'education', 'reducing', 'the', 'barriers', 'of', 'current', 'formal', 'education', 'system']
#without using split function:
sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
split_list = []
temp = ''
for s in sentence:
   if s == ' ':
       split_list.append(temp)
       temp = ''
   else:
       temp = temp + s
split_list.append(temp)
print(split_list)
###########################################################################################################
#function:
def break_into_words(sentence):
    split_list = []
    temp = ''
    for s in sentence:
        if s == " ":
            split_list.append(temp)
            temp=" "
        else:
            temp= temp + s
    split_list.append(temp)
    print(split_list)#if you dont use return,it will show none after splitting the sentence into words
ui=input("Enter a sentence")
print(break_into_words(ui))
        
