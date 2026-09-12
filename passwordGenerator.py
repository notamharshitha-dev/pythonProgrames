import random
import string
#char_set=[string.ascii_letters,string.ascii_uppercase,string.ascii_lowercase,string.digits,string.punctuation]
number_set=string.digits
#print(number_set)
uppercase_set=string.ascii_uppercase
lowercase_set=string.ascii_lowercase
splchar_set=string.punctuation
p_length=int(input("Enter the length of the password "))
p_set=""
while(len(p_set)<=p_length):
    p_set+=random.choice(number_set)
    p_set+=random.choice(uppercase_set)
    p_set+=random.choice(lowercase_set)
    p_set+=random.choice(splchar_set)
#print("The generated password is ",p_set)
print("The generated password is ",p_set[0:p_length+1])
    