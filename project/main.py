import os
print ("Starting Face Detector")
os.system("python Drowsiness_Detection.py ")
print ("script1 ended")
print ("Starting Lane Detection")
os.system("python solution.py")
print ("script2 ended")
print ("Starting Vehicle Detection")
os.system("python vehicle_detection.py")
print ("script2 ended")

