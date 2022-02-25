def fibonacci(nth_value):
    '''Iterable O(n) operation for retrieving a fibonacci number'''
    fibs = [0, 1]
    # First two numbers are identified; if request is for one of these,
    # return and eject from function
    if (nth_value < 3):
        return fibs[nth_value - 1]
    # Next numbers must be calculated through addition of previous terms
    for i in range(2, nth_value):
        fibs.append(fibs[i-2] + fibs[i-1])

    # Fail-safe check to ensure fibs array was properly filled before
    # returning a value
    if (len(fibs) == nth_value):
        return fibs[nth_value - 1]
    # Something went wrong. Consider raising exception
    else:
        print("Length of fibonacci list was unable to accomodate request. " +
              "Returning initial value.")
        return(nth_value)

if __name__ == "__main__":
    print("Testing fibonacci inputs")
    print("fib of 1: %d" % fibonacci(1))
    print("fib of 2: %d" % fibonacci(1))
    print("fib of 3: %d" % fibonacci(3))
    print("fib of 4: %d" % fibonacci(4))
    print("fib of 5: %d" % fibonacci(5))
    print("fib of 6: %d" % fibonacci(6))
    print("fib of 7: %d" % fibonacci(7))
    print("fib of 8: %d" % fibonacci(8))
    print("fib of 9: %d" % fibonacci(9))
    print("fib of 10: %d" % fibonacci(10))
    print("fib of 11: %d" % fibonacci(11))
    print("fib of 12: %d" % fibonacci(12))
    print("fib of 100: %d" % fibonacci(100))
    print("fib of 150: %d" % fibonacci(150))
