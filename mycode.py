import pyttsx3
import os

print()
print("press 1 for chrome")
print("press 2 for notepad")
print("press 3 for media player")

print()

p=("enter your chioce: ",end="")

p= input()
os.system(p)
if(int(p)==1):
	os.system("chrome")
elif(int(p)==2):
	os.system("notepad")
elif(int(p)==3):
	os.system("wmplayer")
else:
	pyttsx3.speak("you are not choose number in this list soo don't support")
