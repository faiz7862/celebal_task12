def find_max(a,b,c):
    if a>b>c:
        print("The Maximum is: ",a)    
    elif b>c>a:
        print("The Maximum is: ",b)
    else:
        print("The Maximum is: ",c)
    return 0

def main():
    try:
        
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        largest = find_max(num1, num2, num3)
        
        
        print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

main()