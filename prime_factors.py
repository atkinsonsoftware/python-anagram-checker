import argparse

def returnPrimeFactors(num):
    if type(num) != int:
        raise TypeError("Int required for prime factor list")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("value", type=int)

    args = parser.parse_args()
    value = args.value

    print(value)
    factors = []
    for i in range(2, value):
        if (value % i == 0):
            print("Testing i: %d" % i)
            if len(factors) > 1:
                for f in factors[:]:
                    if (i % f == 0):
                        print(" not adding i %d" % i)
                        print(" because factor f %d already counted" % f)
                        break
                    else:
                        factors.append(i)
                        break
            else:
                factors.append(i)

    print("%d's factors are: %s" % (value, factors))
