def main():
    year = int(input("Please input a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}? Wah bhai wah! Yeh to LEAP year nikla! 🎉")
    else:
        print(f"{year}? Oops! Yeh leap year nahi hai. 😢")

if __name__ == '__main__':
    main()
