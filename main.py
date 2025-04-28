from activity import fizzbuzz

def main():
    try:
        num = int(input("Enter a number: "))
        print(fizzbuzz(num))
    except ValueError:
        print("Not number")

if __name__ == "__main__":
    main()