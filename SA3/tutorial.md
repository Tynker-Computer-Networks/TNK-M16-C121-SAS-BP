Dictionary Attack.
======================


In this activity, you will learn to crack a password using Brute Force Dictionary attack.


<img src= "https://s3.amazonaws.com/media-p.slid.es/uploads/1525749/images/10963574/ezgif.com-gif-maker__13_.gif" width = "50%" height = "auto">




Follow the given steps to complete this activity:
1. Dictionary Attack.


* Open the file main.py.


* Fetch the target pdf file and read the file as a binary object.
```
filename = input('Path to the file: ')
filename = filename.strip()
   
file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)
```


* Check if the file is password protected or not.


```
if not pdfReader.isEncrypted:
print('The file is not password protected! You can successfully open it!')


else:
      # perform Dictionary attack


```


* Read the list of common words from the Dictionary.
 
```
wordListFile = open('wordlist.txt', 'r', errors='ignore')
body = wordListFile.read().lower()
words = body.split('\n')
```  
* Loop through each of the word and try to unlock the pdf.
```
for i in range(len(words)):
    word = words[i]
    print(f'Trying to decode passowrd by: {word}')
    result = pdfReader.decrypt(word)
```
* Display the message as per the result for each word.
```
if result == 1:
   print(f"Congratulations!!! The password is {word}.")
   break
elif result == 0:
   attempts += 1
   print(f'Passwords attempts: {str(attempts)}')
   continue


```
   


* Save and run the code to check the output.
