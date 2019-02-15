import schoolopy
import startup
import os

#Change on own device
key = #KEY GOES HERE
secret = #SECRET GOES HERE

sc = schoolopy.Schoology(schoolopy.Auth(key, secret))
sc.limit = 1000000

teacherID = sc.get_user(#TEACHER ID) #Grab teacher ID


fileName = teacherID.name_display + '.txt'

likeNum = 0
totalLike = 0

with open(fileName, 'w+', encoding='utf-8') as file:
	for update in sc.get_feed():
		user = sc.get_user(update.uid)
		
		if user == teacherID:		
			file.write(str(update.body) + "\n")
			likeNum += update.likes
			totalLike+= 1
			
print(likeNum/totalLike)