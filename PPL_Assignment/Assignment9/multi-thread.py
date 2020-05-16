import threading
import datetime
def hrs (cuurrent):
	h = current.hour
	if (h < 10):
		print ("0", end = "")
	print (h, end = ":")
def minu (current):
	h = current.minute
	if (h < 10):
		print ("0", end = "")
	print (h, end = ":")
def sec (current):
	h = current.second
	if (h < 10):
		print ("0", end = "")
	print (h, end = "\n")
if __name__ == '__main__':
	current = datetime.datetime.now ()
	t1 = threading.Thread (target = hrs, args = [current])
	t2 = threading.Thread (target = minu, args = [current])
	t3 = threading.Thread (target = sec, args = [current])
	t1.start ()
	t2.start ()
	t3.start ()
	t1.join ()
	t2.join ()
	t3.join ()
