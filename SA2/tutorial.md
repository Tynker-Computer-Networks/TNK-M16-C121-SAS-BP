Crack any length password
===================


In this activity, you will learn to crack the password of any file.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10951350/sa2__1_.gif" width = "100%" height = "auto">




Follow the given steps to complete this activity:
1. Crack any length password


* Open the file main.py.


* Fetch the maximum password length from the user.
	
	```
 passwordLength = int(
        input("Up to which length you want to check the password: "))
```


* Create the characters array directly from the string library.
	```
chars = string.printable.strip()
	```


* Loop through different length of the passwords from 1 to max length entered.
```
for length in range(1, passwordLength + 1):
    print(f"Checking for length {length}.")
```




* Loop through all the possible combinations for a particular length.
```
for guess in itertools.product(chars, repeat=length):
    attempts += 1
    guess = ''.join(guess)
```


* Remove the additional break statements and change the final message in case of an unsuccessful hack.
```
if (result == 1):
        break
if (result == 0):
message = f"Sorry, password not found. A total of {attempts} possible combinations tried. Password is not of {passwordLength} characters."
```


* Save and run the code to check the output.
