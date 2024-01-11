Crack the 4-letter password
===================


In this activity, you will learn to break the four character password protected zip file.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10961915/sa1.gif" width = "50%" height = "auto">


Follow the given steps to complete this activity:
1. Crack the 4-letter password.


* Open file main.py


* Get the file path from the user and check if the file is password protected or not.
	```
	folderpath = input('Path to the file: ')
folderpath = folderpath.strip()


if (not is_zip_encrypted(folderpath)):
    print('The zipped file/folder is not password protected! You can successfully open it!')


	```




* Define the character array including all numbers, lowercase letters, uppercase letters and special characters.
```
else:


result = 0  
attempts = 0  
characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_', '&', ';', '"', '?', '`', "'", '\\']
```
* Loop through the character array to generate all the possible combinations for a 4 character password.
```
print("Brute Force Started...")
if (result == 0):
   print("Checking for 4 character password...")
   for i in characters:
      for j in characters:
         for k in characters:
            for l in characters:
               guess = str(i) + str(j) + str(k) + str(l)


		```
   
* Try the combination to extract the zip and break the loops once the password is found.
 	```
     	            guess = guess.encode('utf8').strip()
            attempts += 1
            try:
                with zipfile.ZipFile(folderpath, 'r') as zf:
                    zf.extractall(pwd=guess)
                    guess = guess.decode('utf8').strip()
                    result = 1
                    break
            except:
                pass
        if result == 1:
            break  
    if result == 1:
        break
if result == 1:
    break


 		``` 


 
* Print the message stating the result whether password is found or not.
 ```
 if (result == 0):
     message = f"Sorry, password not found. A total of {attempts} possible combinations tried. Password is not of 4 characters."


else:
     message = f"Congratulations!!! Password found after trying {attempts} combinations.\nThe password is {guess}."
           
print(message)


 	``` 
* Save and run the code to check the output.
