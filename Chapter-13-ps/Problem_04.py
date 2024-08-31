def divisible5(n):
    if(n%5==0):
        return True
    return False

a = [12,3,4,6,7,9,9,2,5,16,4,52,52,5,56,4,86,85,55]

f = list(filter(divisible5,a))
print(f) 