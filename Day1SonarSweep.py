counter = 0
depth_increase = 0
reading1 = int(input())
while counter < 10:
    reading2 = int(input())
    if reading1 < reading2:
        depth_increase += 1
    reading1 = reading2
    counter += 1

print ("There was", depth_increase, "increases of depth in the sonar sweep.")
