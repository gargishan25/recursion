# A Python program called stair-climb.py that uses a recursive function ways (stairs) 
# to count and print every distinct path up a staircase of any height — using only 1-step and 2-step moves.
# Running ways(4) returns 5; ways(5) returns 8.
def stair_climb(stairs,list):
    if stairs == 0:
        print(list)
        return 1
    
    if stairs < 0:
        return 0
    return stair_climb(stairs - 1,list + [1]) + stair_climb(stairs - 2,list + [2])
print(stair_climb(5,[]))