import random
import sys
random_num=random.randint(1,10)

while(1):
    g_num=int(input("Enter the guessed number "))
    if(g_num==random_num):
        print("Yeahh uhh wonn!!!!")
        sys.exit()
    elif(g_num<random_num):
            print("Entered Number is small Than the actual Number try again best of luck...")
            continue
            print("poleee inka")
    elif(g_num>random_num): 
            print("Entered Number is bigger than the actual Number try agin best of luck....")
            continue
            print("poleee inka")
    
