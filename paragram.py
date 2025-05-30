j= input("Enter the string")
vowels={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0
}
for i in j:
    if i in vowels:
        vowels[i]+=1
print(vowels)

consanunts={
    "a":0,
    "b":0, "c":0, "d":0, "e":0, "f":0,
    "g":0, "h":0, "i":0, "j":0, "k":0,
    "l":0,
    "m":0, "n":0, "o":0, "p":0, "q":0,
    "v":0, "u":0, "t":0, "s":0, "r":0,
    "w":0,
    "x":0, "y":0, "z":0
}
for i in j:
    if i in consanunts:
        consanunts[i]+=1
print(consanunts)
k= input("Enter a number")

numbers={
    "0":0,
    "1":0,
    "2":0,
    "3":0,
    "4":0,
    "5":0,
    "6":0,
    "7":0,
    "8":0,
    "9":0
}
for i in k:
    if i in numbers:
        numbers[i]+=1
paragram=True
for k in numbers.values():
    if k==0:
        paragram= False
if paragram:
    print("number is a paragram")
else:
    print("number is not a paragram")