#setup
input_file = open('BinaryDiagnosticPuzzleInput.txt', 'r')
bits = input_file.readlines()
print ("hello world")

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
