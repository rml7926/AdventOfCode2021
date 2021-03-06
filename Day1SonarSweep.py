#set up
depth_increase = 0

input_file = open('SonarSweepPuzzleInput.txt','r')
readings = input_file.readlines()

#part 1
reading1 = 500
for reading in readings:
    reading2 = int(reading)
    if reading2 > reading1:
        depth_increase += 1
    reading1 = reading2

print ("The number of times the readings increased is:", depth_increase)

#part 2
depth_increase = 0
for i in range (0, len(readings)-3):
    exiting = int(readings[i])
    entering = int(readings[i+3])
    if exiting < entering:
        depth_increase += 1

print ("The total times the sliding window increased was:", depth_increase)