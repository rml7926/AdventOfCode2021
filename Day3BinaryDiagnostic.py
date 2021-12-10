#setup
input_file = open('BinaryDiagnosticPuzzleInput.txt', 'r')
bits = input_file.readlines()

#part 1
ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeroes = [0,0,0,0,0,0,0,0,0,0,0,0]
for bit in bits:
    for column in range(0,12):
        digit = bit[column:column+1]
        if digit == "1":
            ones [column] += 1
        elif digit == "0":
            zeroes [column] += 1
        else:
            print ("error")
gamma = ""
epsilon = ""
for comparison in range (0,12):
    if ones[comparison] > zeroes[comparison]:
        gamma += "1"
        epsilon += "0"
    elif ones[comparison] < zeroes[comparison]:
        gamma += "0"
        epsilon += "1"
    else:
        print ("error")
print ("gamma",gamma)
print ("epsilon:",epsilon)
dec_gamma = int(gamma, 2)
dec_epsilon = int(epsilon, 2)
print (dec_gamma*dec_epsilon)



#loop over all the rows
#count the number of ones and zeroes in the index'th column
def count_ones_and_zeroes(rows, index):
    count_one = 0
    count_zero = 0
    for row in rows:
        digit = row[index:index+1]
        if digit == "1":
            count_one += 1
        elif digit == "0":
            count_zero += 1
        else:
            print ("error")
    return [count_zero, count_one]

#loop over the rows, creating a new array whose enteries have keep value
#in the index'th column
def select_rows(rows, keep_value, index):
    result = []
    for row in rows:
        digit = row[index:index+1]
        if keep_value == digit:
            result.append (row)
    return result

"""
start with all readings
start with the first digit
loop all readings for the current digit
count all the 1's and 0's
examine if there are more 1's or 0's for that digit
discard rows that do not contain the common digit
if one row left: stop
otherwise move on to next digit and repeat until all digits are complete
"""

digit_number = 0
oxygen_rows = bits
co2_rows = bits
while len(oxygen_rows) > 1:
    counts = count_ones_and_zeroes(oxygen_rows, digit_number)
    if counts[0] <= counts[1]:
        keep_value = "1"
    else:
        keep_value = "0"
    oxygen_rows = select_rows(oxygen_rows, keep_value, digit_number)
    digit_number += 1
oxygen_reading = int(oxygen_rows[0], 2)
print (oxygen_reading)

digit_number = 0
while len(co2_rows) > 1:
    counts = count_ones_and_zeroes(co2_rows, digit_number)
    if counts [0] <= counts [1]:
        keep_value = "0"
    else:
        keep_value = "1"
    co2_rows = select_rows(co2_rows, keep_value, digit_number)
    digit_number += 1
co2_reading = int(co2_rows[0], 2)
print (co2_reading)

life_support = co2_reading * oxygen_reading
print (life_support)
