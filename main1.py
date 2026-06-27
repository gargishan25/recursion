#Given a list of numbers, calculate the total sum of all elements.
def sum(a):
    if len(a)==0:
        return 0
    return a[0]+sum(a[1:])
print(sum([1,2,3,4,5,6,7,8,9,10]))