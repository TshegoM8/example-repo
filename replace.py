#save a setence 
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
#now we print it without the !
print(sentence.replace("!"," "))
#now reprint with upper case
print(sentence.replace("!"," ").upper())
#lastly we print in reverse
print(sentence.replace("!"," ").upper()[: : -1])
