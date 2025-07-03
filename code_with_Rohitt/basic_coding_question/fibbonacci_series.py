def fiboncci_series (n):
    a,b = 0,1

    series = []

    for _ in range (n):
        series.append(a)
        a,b = b,a+b 
    return series


print(fiboncci_series(10))

    


# ✅ Recursive Version (Less Efficient)

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Generate first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci_recursive(i), end=" ")



# ✅ Generator Version (Memory Efficient)

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
for num in fibonacci_generator(10):
    print(num, end=" ")
