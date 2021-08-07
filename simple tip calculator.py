print("Welcome to the tip calculator\n")
val3=float(input("What was your total bill?"))
val=int(input("What percentage tip would you like to give?10,20,30 "))
count=int(input(f"How many people to split a bill"))
tipamount=val/100
# billperson=totalbill/count
totaltipamount=tipamount*val3
totalbill=totaltipamount+val3
billperson=totalbill/count
finalamount=round(billperson,2)
print(f"Each person should pay : {finalamount}")
