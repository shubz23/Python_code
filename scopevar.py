# def fibonacci(n):
#     fib_seq = [0, 1]
#     for i in range(2, n):
#         fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
#     return fib_seq[:n]

# n = 10
# print(fibonacci(n))
 

# with recursion

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

n = 10
print(fibonacci(n))
