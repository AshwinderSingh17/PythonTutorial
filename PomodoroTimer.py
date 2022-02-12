# import the time module
import time
from datetime import date, datetime
import os

today = date.today()

print("Pomodoro Timer \n\n")

if os.path.exists("PomodoroRecords.txt") == False:
    f = open("PomodoroRecords.txt", "a")
    f.write("TaskName,TodaysDate,StartTime,endTime,hours:minutes:seconds"+"\n")
    f.close()




# define the countdown func.
def countdown(t):
	print("\n")
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print("Timer - "+timer, end="\r")
		time.sleep(1)
		t -= 1
	
	

TaskName = input("Enter Task you will be working on: ")

# input time in seconds
tf = input("Enter the time in format (Hours:Minutes:Seconds)- ")
t= tf.split(":")
hours_inSeconds=int(t[0])*3600
minutes_inSeconds=int(t[1])*60
Seconds=int(t[2])

totalSeconds= hours_inSeconds + minutes_inSeconds + Seconds

TodaysDate = today.strftime("%b-%d-%Y")
now = datetime.now()
StartTime = now.strftime("%I:%M:%S %p")
print("\nStart Time: "+StartTime)

# function call

countdown(int(totalSeconds))
now = datetime.now()
endTime = now.strftime("%I:%M:%S %p")
print("End Time: "+endTime)

print('\n\nGood Work, Keep it up!!\n\n')

TaskRecord = TaskName+","+TodaysDate+","+StartTime+","+endTime+","+tf

#print(TaskRecord)



f = open("PomodoroRecords.txt", "a")
f.write(TaskRecord+"\n")
f.close()
