from Add import add
from sub import sub
from mul import mul
from div import div
from table1 import multiplication_table
while True:
    def main():
        print("=== WELCOME TO OLD GENERATION CALCULATOR SYSTEM ===\n")
        print(
            " 1.For Addition \n 2.For Subtraction\n 3.For Multiplication\n 4.For Division\n 5.For Printing Multiplication Table\n 6.For Exit\n")
        user_input = input("Enter your choice: ")
        if user_input == "1":
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            add(a, b)
        elif user_input == "2":
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            sub(a, b)
        elif user_input == "3":
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            result = mul(a, b)
            print(f"The Multiplication of {a} and {b} is {result}")
        elif user_input == "4":
            a = int(input("Enter First Number: "))
            b = int(input("Enter Second Number: "))
            results = div(a, b)
            print(f"The Division of {a} and {b} is {results}")
        elif user_input == "5":
            multiplication_table()
        elif user_input == "6":
            return
        elif user_input == "7":
            return


    if __name__ == "__main__":
        main()