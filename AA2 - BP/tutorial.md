Crack for different type of files.
======================


In this activity, you will write single python code to crack the password for both ( PDF / ZIP ) files.


<img src= "https://media.slid.es/uploads/1525749/images/10963481/image__32_.png" width = "100%" height = "auto">




Follow the given steps to complete this activity:
1. Crack for different type of files.


* Open the file `main.py`.


*  Get the target file type from the user.


```
fileType = input(
        "Select the filetype:\n1.ZIP\n2.PDF\nEnter the Selection: ")


```


*  Add elif block to check is PDF file is encrypted or not.
```
if (not is_zip_encrypted(folderpath) and fileType == "1"):
    print('The zipped file/folder is not password protected! You can successfully open it!')
elif (not is_pdf_encrypted(folderpath) and fileType == "2"):
    print('The PDF file/folder is not password protected! You can successfully open it!')


```


*  Write condition to handle zip files filetype.
```
if (fileType == "1"):
    try:
        with zipfile.ZipFile(folderpath, 'r') as zf:
            guess = guess.encode('utf8').strip()
            zf.extractall(pwd=guess)
            guess = guess.decode('utf8').strip()
            result = 1
            endtime = time.time()
            break
    except:
        pass
```


* Write condition to handle pdf files filetype..
```
if (fileType == "2"):
    try:
          file = open(folderpath, 'rb')
          pdfReader = pd.PdfFileReader(file)
          passwordChecker = pdfReader.decrypt(guess)
          if (int(passwordChecker) == 1):
              result = 1
              endtime = time.time()
              break
          except:
              pass
```




* Save and run the code to check the output.
