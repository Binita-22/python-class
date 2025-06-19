divisor = int(input("Enter a number: "))
dividend =20
if divisor == 0:
    msg = "donot write worng number or data."
    raise Exception(msg)

result = divisor/ dividend
print(result)
