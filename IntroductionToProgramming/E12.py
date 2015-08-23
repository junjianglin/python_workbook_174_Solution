import math

point1 = map(float,raw_input("please enter the latitude and longitude for first point, sep by ,").split(','))
point2 = map(float,raw_input("please enter the latitude and longitude for second point, sep by,").split(','))

distance = 6371.01 * math.acos(math.sin(math.radians(point1[0])) * math.sin(math.radians(point2[0])) + \
			math.cos(math.radians(point1[0])) * math.cos(math.radians(point2[0])) * math.cos(math.radians(point1[1]-point2[1])))

print "the distance is : ", distance
