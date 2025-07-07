def multiplication_table():
    m = int(input("Enter the Number: "))
    print(f"The Multiplication Table of {m} is:")
    with open("Multiply.txt",'w')as file:
        file.write("------------ Multiplication Table----------\n")
        i=1
        for i in range(1,11):
            file.write(f"{m}x{i}={m*i}\n")
        print(f"Multiplication Table of {m} is Successfully generated")
