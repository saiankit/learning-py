def Power_Recursion(x,n):
    if n==1:
        return x
    elif n>0:
        return x*Power_Recursion(x,n-1)
base = input("Enter the base")
power = input("Enter the power")
print("{} ^ {} = {}".format(base,power,Power_Recursion(base,power)))
