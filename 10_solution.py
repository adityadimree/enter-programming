#recursion functions ese functions hote hai jinki definition me hi hum unhe hi call krne lagte hai. Ye thi pehli baat.
#recursion function me exit strategy ke bare me sochna zaroori hai. Ye thi doosri baat.
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(5))