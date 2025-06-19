try:
    a = int (input("Enter a number: "))
    output = 10/a
    print(f"The output of user data is:{output} ")
except Exception:
    print("Invalid number!")
# finally = code ma error awyani na awyani teyo chai run hunxas
finally:
    print("Thank you for using our code.")