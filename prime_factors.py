import argparse

def returnPrimeFactors(num):
    if type(num) != int:
        raise TypeError("Int required for prime factor list")

    factors = []
    for i in range(2, num):
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
