# n! = n * (n - 1) * (n - 2) * ... * 2 * 1 or 
# n! = n * 1 * 2 * ... * (n - 2) * (n - 1)
def factorial_with_loop(n):
    factorial = n
    
    if n < 0:
        print("Negative nos can't have factorial")
        return -9999
        
    for i in range(n - 1, 1, -1):
        print('factorial', factorial)
        print('i', i)
        print(f"{factorial} * {i} = {factorial * i}")
        factorial = factorial * i
        
    return factorial


def factorial_with_recursion(n):
    print('n:', n)
    if n < 0:
        print("Negative nos can't have factorial")
        return -9999

    if n <= 2:
        return n
    
    return n * factorial_with_recursion(n - 1)

        
# fact5r = factorial_with_recursion(5)
# fact10r = factorial_with_recursion(10)
# fact100 = factorial_with_loop(-100)

print(f"Factorial of 5 using loop is: {factorial_with_loop(5)}")
print(f"Factorial of 10 using loop is: {factorial_with_loop(10)}")
print(f"Factorial of 5 using recursion is: {factorial_with_recursion(5)}")
print(f"Factorial of 10 using recursion is: {factorial_with_recursion(10)}")


#print(f"Factorial of negative number -100 is: {fact100}")

        
         