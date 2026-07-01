#Given a list of numbers, find the largest number in that list recursively.
# nums = [1,2,5,4,7,2,3,10,12,15]
# def largest(list,i):
#     if i == (len(list)-1):
#         return list[i]
#     biggest = largest(list,i+1)
#     if list[i] > biggest:
#         return list[i]
#     else:
#         return biggest
nums = [1,2,5,4,7]
def largest(list):
    if len(list)==1:
        return list[0]
    return max(list[0],largest(list[1:]))
print(largest(nums)) 
    # if biggest<list[i]:
    #     biggest = list[i]
    # i+=1
    # print(biggest)
    # largest(list,i,biggest)
    # return biggest