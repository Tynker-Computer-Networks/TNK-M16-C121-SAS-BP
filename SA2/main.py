import zipfile
import itertools
import string


def is_zip_encrypted(zipFilePath):
    try:
        with zipfile.ZipFile(zipFilePath, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if zip_info.flag_bits & 0x1:
                    return True
            return False
    except zipfile.BadZipFile:
        return False


def main():
    folderpath = input('Path to the file: ')
    folderpath = folderpath.strip()
    # Get the expected password length from the user in passwordLength variable
    

    if (not is_zip_encrypted(folderpath)):
        print('The zipped file/folder is not password protected! You can successfully open it!')
    else:
        result = 0
        attempts = 0
        print("Brute Force Started...")

        if (result == 0):
            print(
                f"Checking for up to {passwordLength} characters long passwords...")
            # Get the all characters form string library and store them in chars variable
            

            characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                      'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_', '&', ';', '"', '?', '`', "'", '\\']
           
            # Remove these four loops 
            for i in characters:
                for j in characters:
                    for k in characters:
                        for l in characters:
            # Run the loop up to the length of the password the user is looking for...
            
                # Notifies for how much length of password currently programming is checking
                
                # Run loop for each guess in the itertools.product(chars, repeat=length)
                
                            # Remove finding the guess string this way
                            guess = str(i) + str(j) + str(k) + str(l)
                            guess = guess.encode('utf8').strip()
                            # make guess = ''.join(guess), i.e joins elements of a sequence and makes it a string.
                            
                            attempts += 1
                            try:
                                with zipfile.ZipFile(folderpath, 'r') as zf:
                                    zf.extractall(pwd=guess)
                                    guess = guess.decode('utf8').strip()
                                    result = 1 
                                    break     
                            except:
                                pass
                        
                        # Keep one break statement for inner loop  
                        if result == 1:
                            break   
                    if result == 1:
                        break  
                if result == 1:
                    break  

        if (result == 0):
            # Replace 4 by {passwordLength}
            message = f"Sorry, password not found. A total of {attempts} possible combinations tried. Password is not of 4 characters."
            
            print(message)

        else:
            message = f"Congratulations!!! Password found after trying {attempts} combinations.\nThe password is {str(guess)}."
            print(message)

main()
