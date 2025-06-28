def multiplication(product, *args):
    for item in args:
        product = product * item
    print(f"The multiplication of given product is : {product}")


multiplication(1, 2, 3, 4)
