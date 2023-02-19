#Sean Holbrook
#CIS261
#Wk8Lab2 - Recursive Function Fibonacci



#recursive function to return fibonacci for 16

def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
    

#turn the output into a string using the recursive function
sequence = ", ".join(str(fibonacci(n)) for n in range(16))

#print the output of the fibonacci up to 16
print("The Fibonacci series for 16")
print(sequence)



