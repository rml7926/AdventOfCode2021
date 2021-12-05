#setup
forward_count = 0
down_count = 0
up_count = 0

input_file = open('DivePuzzleInput.txt','r')
movements = input_file.readlines()

#part 1
for movement in movements:
    command_fragments = movement.split()
    direction = command_fragments[0]
    distance = int(command_fragments[1])
    if direction == "forward":
        forward_count = forward_count + distance
    elif direction == "down":
        down_count = down_count + distance
    else:
        up_count = up_count + distance

total_movement = forward_count * (down_count - up_count)
print (total_movement)