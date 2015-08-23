height_us = map(float,raw_input("please input your height with feet and inches, sep by ,").split(','))
print "your height in cm is", 2.54*(height_us[0]*12+height_us[1])
