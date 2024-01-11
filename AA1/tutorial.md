Calculate Time Taken
======================


In this activity, you will code to calculate the time it took to crack the password.




<img src= "https://media.slid.es/uploads/1525749/images/10963475/image__31_.png" width = "100%" height = "auto">




Follow the given steps to complete this activity:
1. Calculate Time Taken 


* Open the file `main.py`.


* Declare the variable `starttime` to store the programe starting time after print statement.


```
print("Brute Force Started..."


starttime = time.time()
.
.


```


* Declare the variable starttime to store the programe ending time after result variable and before break.


```
.
.
endtime = time.time()
break


```
*  Declare the variable duration to calculate the total duration of attempts before final If.. else condition.


```
.
.
duration = starttime + endtime: 
	.
	.
	.`
	```


* Modify the print message of If condition.


```
.
.
if (result == 0):
message = f"Sorry, password not found. A total of {attempts} possible combinations tried in {duration} seconds. Password is not of {passwordLength} characters."
 
	.
	.
	.`
	```
* Save and run the code to check the output.
