shift = 5
esentence = input("please enter a sentence: ")
encryption = ""
for ch in esentence:
    if ch.isalpha():
        position = ord(ch)
        positionindex = position - ord('a')
        newindex = (positionindex + shift) % 26
        newtext = newindex + ord('a')
        newchar = chr(newtext)
        encryption = encryption + newchar
print ("the printed sentence is: ", encryption) 
