def factorial(n):
    if n==0 :
        return 1
    else :
        return n*factorial(n-1)
k = input("Enter the number ")
print("{0} ! =  {1}".format(k,factorial(k)))
