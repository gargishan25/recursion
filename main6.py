# A Python program called phone-keypad.py 
# that uses a recursive function combinations(digits, current) 
# to generate and print every possible letter combination from a sequence of phone keypad digits
# — just like T9 texting on old Nokia phones. 
# Entering "23" prints all 9 combinations; entering "322" prints all 27.
phone_keypad = {2: "ABC", 3: "DEF", 4: "GHI", 5: "JKL", 6: "MNO", 7: "PORS", 8: "TUV", 9: "WXYZ"}
inp = 23
def letters(dict, numbers):
    if len(phone_keypad[int(str(numbers)[len(str(numbers))-1])])*
    return phone_keypad[int(str(numbers)[len(str(numbers))-1])]


print(letters(phone_keypad, inp))