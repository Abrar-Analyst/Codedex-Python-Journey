peso_rate = 3696.80
sol_rate = 3.38 
real_rate = 5.26

def calculate_usd():
 co = float(input("What do you have left in pesos? "))
 pe = float(input("What do you have left in soles? "))
 br = float(input("What do you have left in reais? "))

 pesos_in_usd = co / peso_rate
 soles_in_usd = pe / sol_rate
 reais_in_usd = br / real_rate

 total_in_usd = pesos_in_usd + soles_in_usd + reais_in_usd

 print("Total_in_usd =", total_in_usd)
calculate_usd()
