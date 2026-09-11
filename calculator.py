import sys
while(1):
    num1=int(input("Enter number1 "))
    num2=int(input("Enter number2 "))
    op_num=int(input("1.Addition\n2.SUbtartion\n3.Multiplication\n4.Division\n5.Remainder\n6.power\n7.Exit\nEnter your choice  "))    
    match op_num:
        case 1:result=num1+num2
        case 2:result=num1-num2
        case 3:result=num1*num2
        case 4:result=num1/num2  if num2!=0 else "cant be divided by 0"                 
        case 5:result=num1%num2
        case 6:result=num1**num2
        case 7:sys.exit()
    print(f"The Result is {result} \n")