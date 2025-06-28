try:
    a = int(input("Enter a number: "))
    output = 10 / a
    print(f"The output of user data is:{output} ")
except ZeroDivisionError:
    # print(e.__class__.__name__)
    print("Invalid number!")
# finally = code ma error awyani na awyani teyo chai run hunxas
finally:
    print("Thank you for using our code.")
# <-----------Note--------------------------------------------------->
# exeception ko type tha huna lai used garinxa  e.__class__.__name__
# where e stand for execption
