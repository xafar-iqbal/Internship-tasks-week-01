text = input("Enter a word or sentence: ") 
 
 
 
text = text.lower() 
vowels = "aeiou" 
 
vowel_count = 0 
consonant_count = 0 
for char in text: 
    if char.isalpha():   
        if char in vowels: 
            vowel_count += 1 
        else: 
            consonant_count += 1 
print(f"\nVowels: {vowel_count}") 
print(f"Consonants: {consonant_count}") 
