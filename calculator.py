#!/usr/bin/env python3
import sys
import re


def calculate(expression):
    """Evaluate a mathematical expression safely."""
    expression = expression.strip()

    # Only allow numbers, operators, parentheses, and whitespace
    if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
        raise ValueError("Invalid characters in expression")

    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")


def interactive_mode():
    """Run calculator in interactive mode."""
    print("Minimalist CLI Calculator")
    print("Enter expressions or 'q' to quit\n")

    while True:
        try:
            expression = input("> ")

            if expression.lower() in ['q', 'quit', 'exit']:
                break

            if not expression.strip():
                continue

            result = calculate(expression)
            print(f"= {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except EOFError:
            break


def main():
    if len(sys.argv) > 1:
        # Command-line mode: evaluate expression from arguments
        expression = ' '.join(sys.argv[1:])
        try:
            result = calculate(expression)
            print(result)
        except ValueError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()


if __name__ == "__main__":
    main()
