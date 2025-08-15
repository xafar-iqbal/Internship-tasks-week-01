# --- Simple Interest Calculator --- 
 
principal = float(input("Enter the principal amount (P): ")) 
 
rate = float(input("Enter the annual interest rate (R%): ")) 
 
time = float(input("Enter the time in years (T): ")) 
 
# Calculate simple interest 
simple_interest = (principal * rate * time) / 100 
 
print(f"\nSimple Interest = {simple_interest:.2f}") 
