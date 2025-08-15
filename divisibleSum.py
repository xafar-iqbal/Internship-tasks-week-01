limit = int(input("\nEnter the upper limit to sum numbers divisible by 3: ")) 
 
sum_div_by_3 = 0 
for i in range(1, limit + 1): 
    if i % 3 == 0: 
        sum_div_by_3 += i 
 
print(f"Sum of numbers divisible by 3 from 1 to {limit} is: {sum_div_by_3}") 
