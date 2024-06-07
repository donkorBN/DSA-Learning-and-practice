print("#------------------------------------------#")
print("#-------INVESTMENT RETURNS CALCULATOR------#")
print("------------------------------------------")

capital = int(input("How much do you aim to invest in a year? (Ghana Cedis/Dollars): "))
print("                                                                                       ")

interest = int(input("Percentage of interest from the bank?: "))
print("                                                                                       ")

time = int(input("For how long? (Years): "))
print("                                                                                       ")

print("Calculating #")

gains = int((capital * time * interest)/100)
print("                                                                                       ")

print(f"With {capital}, You will receive an interest of {gains} over {time} years")
print("                                                                                       ")

total = gains + capital

print(f"Your investment will amount to {total} in 10 years ! ")
print("                                                                                       ")

print("Thank You!")
print("                                                                                       ")

print("#############################################################")
print("end")
