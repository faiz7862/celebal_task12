def revString(iString):
    
    rString = ""
    for char in iString:
        rString = char + rString
    return rString

def main():
    
    try:
        user_input = input("Enter a string: ")
        
        rString = revString(user_input)
        
        print("Reversed string:", rString)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
