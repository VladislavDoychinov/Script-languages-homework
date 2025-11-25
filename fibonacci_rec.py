def fibonacci_rec(n):
    if n < 3:
        return 1    
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

print(fibonacci_rec(6)) 
