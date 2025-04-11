def is_odd(value: int):
    """
    Checks to see if a value is odd. Returns True if odd, else False.
    """
    return value % 2 == 1

def main():
    result = []
    for i in range(10, 20):
        if is_odd(i):
            result.append(f"{i} odd")
        else:
            result.append(f"{i} even")


    print(" ".join(result))

if __name__ == '__main__':
    main()
