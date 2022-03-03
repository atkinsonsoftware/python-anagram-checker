def do_operation(operand, operator, second_operand):
    '''Return mathematical result of operand performing operator with
    second_operand'''
    # Ensure incoming parameters are of expected type
    if type(operand) != int != type(second_operand):
        raise TypeError("First and third parameters must be integers")

    # Guard against dividing by zero
    if operator == "/" and second_operand == 0:
        raise ZeroDivisionError

    # Perform operations
    if operator == "+":
        return operand + second_operand
    elif operator == "-":
        return operand - second_operand
    elif operator == "*" or operator == "x":
        return operand * second_operand
    elif operator == "/":
        return operand / second_operand
    # Inform user if operator was not of a supported type
    else:
        raise ValueError(
            "Operation %s not supported. +-/* supported at this time."
            % operator)

if __name__ == "__main__":
    # Tests
    tests = [[4, "+", 3, 7],
             [4, "-", 4, 0],
             [5, "*", 5, 25],
             [6, "/", 3, 2],
             [1, "x", 217, 217],
             [0, "/", 4, 0],
             [1, "/", 0, "ZeroDivisionError"],
             [1, "s", 1, "ValueError"],
    ]
    while (len(tests) > 0):
        print("Top of while. len(tests): %d" % len(tests))
        try:
            first_test = tests[0]
            assert(do_operation(first_test[0], first_test[1], first_test[2]) ==
                   first_test[3])
        except AssertionError as e:
            print("Tests failed: %s" % e)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        except ZeroDivisionError as e :
            print(e)
        except Exception as e:
            print("Unexpected exception %s" % e)

        tests = tests[1:]
        print("Bottom of while. len(tests): %d" % len(tests))
