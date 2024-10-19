# Program #4: Coordinates
# Write a distance function that will take two 3-dimensional coordinates (as input) 
# and will return (as output) the distance between those points in space.  
# The 3-dimensional coordinates must be stored as tuples.
import math

def distance(p1,p2):
    dBetweenPoints = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2 + (p2[2]-p1[2])**2)
    return dBetweenPoints

def main():
    try:
        x1 = int(input('What would you like the x coordinate to be? '))
        y1 = int(input('What would you like the y coordinate to be? '))
        z1 = int(input('What would you like the z coordinate to be? '))
        firstSet = (x1, y1, z1)

        x2 = int(input('What would you like the x coordinate to be? '))
        y2 = int(input('What would you like the y coordinate to be? '))
        z2 = int(input('What would you like the z coordinate to be? '))
        secondSet = (x2, y2, z2)
    except ValueError:
        print ('ERROR: input must be a number')
    finalResult = round(distance(firstSet,secondSet),4)
    print(finalResult)

main()
# Now write a mainline that has the user enter the two tuples.  
# The mainline calls the distance function and stores the distance in a variable.  The mainline then displays the distance.  
# Also include exception handling to deal with faulty input.
# The distance between two points (x1,y1,z1) and (x2, y2, z2) is 
#    given by:   sqrt ((x2-x1)^2 + (y2 - y1)^2 + (z1 - z2)^2)


