import argparse

def returnPrimeFactors(num):
    if type(num) != int:
        raise TypeError("Int required for prime factor list")

    factors = []
    # Prime numbers begin with 2, and entered number itself could be a prime
    for i in range(2, num + 1):
        if (num % i == 0):
            # If there are existing prime factors, check that this is not
            # a multiple of any
            if not any(i % f == 0 for f in factors[:]):
                factors.append(i) # First prime factor
    return factors

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=int)

    args = parser.parse_args()
    value = args.value

    print("%d's prime factors are: %s" % (value, returnPrimeFactors(value)))
