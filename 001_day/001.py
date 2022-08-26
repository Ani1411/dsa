def add_two_num(num1, num2):
    """
    Algorithm 1: Add two numbers entered by the user.
    1. Declare variables num1, num2 and sum
    2. Take input to num1 and num2
    3. Add num1 and num2 and assign the result to sum
    4. Display sum
    """
    return f"Sum of {num1} and {num2}: {num1 + num2}"


print(add_two_num(4, 5))


def largest_number_among_three_numbers(a, b, c):
    statement = f"larget among {a}, {b}, {c} is"
    if a > b > c:
        return f"{statement} {a}"
    elif b < a < c:
        return f"{statement} {c}"
    else:
        return f"{statement} {b}"


print(largest_number_among_three_numbers(14, 99, 27))


def roots_of_quadratic_equation(a, b, c):
    """
    equation: ax2 + bx + c = 0
    """
    d = b ** 2 - 4 * a * c
    state = f"roots of quadratic equation {a}x2 + {b}x + {c} are"
    if d >= 0:
        r1 = (- b + (d ** 0.5)) / 2 * a
        r2 = (- b - (d ** 0.5)) / 2 * a
        return f"{state} {r1}, {r2}"
    else:
        rp = - (b / (2 * a))
        ip = abs(d / (2 * a))
        return f"{state} {rp} + j{ip}', f'{rp} - j{ip}"


print(roots_of_quadratic_equation(1, -10, 25))


def factorial_of_number(num):
    i = 1
    fact = 1
    while i <= num:
        fact = fact * i
        i += 1
    return f"factorial of {num} is {fact}"


print(factorial_of_number(3))


def check_prime(num):
    i = 2
    while i <= num / 2:
        if num % i == 0:
            print(i)
            return f"{num} is Not a prime number"
        i += 1
    return f"{num} is Prime Number"


print(check_prime(999983))


def fibonacci_seq_up_to_(num):
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[len(fib) - 2])
    return f"fibonacci sequence up to {num}: {fib[1:-1]}"


print(fibonacci_seq_up_to_(1000))
