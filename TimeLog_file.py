#This is a program to log time in a output.txt file
import os
from datetime import datetime
file =open("output.txt",'a') #to open output.txt in append mode
now = datetime.now()
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
#print("date and time:",date_time)
file.write(date_time+'\n')
file.close # to close file