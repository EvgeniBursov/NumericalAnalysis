def machine_epsilon():
    eps = 1.0
    while (1.0 + eps) > 1.0:
        eps /= 2.0
    return eps * 2.0


def calculate_expression(eps):
    expression = abs(3.0 * (4.0 / 3.0 - 1) - 1)
    corrected_expression = expression - eps
    return expression, corrected_expression


def main():
    eps = machine_epsilon()
    print("Machine Precision  : ", eps)

    expression, corrected_expression = calculate_expression(eps)
    print("\nResult of abs(3.0 * (4.0 / 3.0 - 1) - 1):")
    print("Before using machine epsilon: {}".format(expression))
    print("After correcting with machine epsilon: {}".format(corrected_expression))


if __name__ == '__main__':
    main()

