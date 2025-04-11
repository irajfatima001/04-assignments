MAX_TERM_VALUE = 10000

def main():
    curr_term = 0
    next_term = 1  # Doosra number (Fib(1))

    while curr_term <= MAX_TERM_VALUE:
        print(curr_term, end=" ")  # Saath saath print kare line mein
        # Naya term calculate karo (sum of previous two)
        term_after_next = curr_term + next_term
        # Update values for next round
        curr_term = next_term
        next_term = term_after_next

# Function call (zaroori hai jab file run ho)
if __name__ == '__main__':
    main()
