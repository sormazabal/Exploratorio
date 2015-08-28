lector.py
import csv

f = open('foursquare_checkins.csv')
csv_f = csv.reader(f)

user = []
latitude =[]
longitude = []
time = []
location = []

for row in csv_f: #user
	
	user.append(row[0])
	
	int user_num = max (user) 
  

print user

for row in csv_f: # latitude and checkin count
	checkin_count = 0
	checkin_count+= 1
	latitude.append(row[1])
	print checkin_count

print latitude

for row in csv_f:
  longitude.append(row[2])

print longitude

for row in csv_f:
  location.append(row[4])

print location