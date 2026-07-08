# A Python program called reverse-lab.py with four experiments. 
# PART 1 scans a number and shows each digit being peeled off using % and //. 
# PART 2 takes a number and reverses it using a recursive function. 
# PART 3 takes a name or word and flips it using recursion. 
# PART 4 tests a list of numbers to see which ones are powers of 4, 
# then lets the student test their own number.
def part1(num):
    while num>0:
        digit = num%10
        print(f"Peeled off {digit}.") 
        num //= 10

def part2(num,num_list):
    num_list.append(num%10)
    if num%10 == num:
        return num_list
    return part2(num//10,num_list)

def part3(word,word_list):
    if len(word) == 0:
        return word_list
    word_list.append(word[-1])
    return part3(word[:-1],word_list)
def part4(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    if num%4 != 0:
        return False
    return part4(num//4)

part1(1234)

print(*part2(1234,[]))

print(*part3("hello",[]))

numbers_list = [1,4,12,16,64,0]
result = {num:part4(num) for num in numbers_list}
print(result)