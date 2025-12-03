import random
import time
import os

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end="")
        time.sleep(delay)
    print()

def banner():
    print("===================================")
    print("|           CALCULATOR            |")
    print("|---------------------------------|")
    print("|   Just goes from left to right  |")
    print("|     2 + 3 * 4 - 5 / 2           ║")
    print("|  Type 'exit' to quit            ║")
    print("╚═════════════════════════════════╝\n")

def calculate(expr):
    expression = []
    value = 0
    try:
        temp = ''
        for pos, x in enumerate(expr):
            if x in '*+-/':
                expression.append(temp)
                expression.append(x)
                temp = ''
                continue

            if pos == len(expr) - 1:
                temp += x
                expression.append(temp)
                break

            temp += x

        value = int(expression[0])
        typeof = ''

        for x in expression:
            if x in '*+-/':
                typeof = x
                continue

            #if item is not a type of operation, then it is usable
            match typeof:
                case '*':
                    value *= int(x)
                case '+':
                    value += int(x)
                case '-':
                    value -= int(x)
                case '/':
                    value /= int(x)
    except Exception as e:
        print(e)

    return value



def loading_animation():
    for frame in ['\\', "|", "/", "⎯⎯"]:
        print("\rCalculating " + frame, end="")
        time.sleep(0.3)
    print("\r" + " " * 20, end='')

def main():
    banner()
    while True:
        slow_print("Enter expression")
        expr = input("> ")

        if expr.lower() == "exit":
            slow_print("\nExiting calculator...")
            break

        for x in range(random.randint(1, 3)):
            loading_animation()

        result = calculate(expr)
        print("\n" + "=" * 40 + "\n")
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
