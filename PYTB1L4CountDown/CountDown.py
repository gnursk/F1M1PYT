import time 
import webbrowser

def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
	

	webbrowser.open('https://www.youtube.com/watch?v=d7qYhAFj0FE')



t = 1000

countdown(int(t)) 
