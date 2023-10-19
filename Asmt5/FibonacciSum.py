# a function to generate fibonacci numbers using yield
def fibonacci():
    num1, num2 = 0, 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


# gives the maximum fibonacci number which is less than the given number
def get_fib(number):
    fib = fibonacci()
    new = next(fib)
    while new <= number:
        prev = new
        new = next(fib)
    return prev


number = 9
sum = []
diff = number
while diff != 0:  # continue till difference becomes zero
    seq = get_fib(diff) #get the maximum fibonacci number which is less than the given number
    sum.append(seq)  # add the element to the sum list
    diff = diff - seq

print("The given number can be written as a sum of the given numbers: {}".format(sum))
