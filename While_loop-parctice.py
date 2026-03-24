agestr = input("please enter you data of birth: ")
while agestr.isdigit():
    agelimit = int(agestr)
if agelimit < 18:
    print("You are considerd a minor")
else:
    print("You are allowed to buy alchol")