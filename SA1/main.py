import zipfile

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
    # Get the target file path from the user in folderpath variable
    

    # Checks if the file is password encrypted
    
        # Notifies if the zipped file/folder is not password encrypted
        

    # Else:
    
        # Initialize a variable result with zero. '0' will indicate Failure, while '1' will indicate Success
        
        # Initialize a variable attempts to keep the count of passwords tried
        
        
        # Uncomment to build a character array including all numbers,lowercase letter, uppercase letters and special characters. Total 10+26+26+33 = 95 characters
        # characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        #               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        #               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        #               '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_', '&', ';', '"', '?', '`', "'", '\\']

        print("Brute Force Started...")

        # Check if result is 0  
        
            # Print Checking for 4 character password...
            
            # Loop through each character in characters to create loop for 4th position
            
                # Create an inner loop to loop through characters to create loop for 3rd position
                
                    # Create an inner loop to loop through characters to create loop for 2nd position
                    
                        # Create an inner loop to loop through characters to create loop for 1st position
                        
                            # Concatenate characters from the array to make a 4 character password combination and store it in variable guess
                            
                            # Encodes the password combination and store it back in guess
                            
                            # Increment the attempts by 1
                            
                            # Add try block
                            
                                # Access the zipfile in folderpath in read mode
                                
                                    # Use extractall() method on zipfile and pass guess string as pwd 
                                    
                                    # Decode the guess string
                                    
                                    # Set result variable to 1 on success
                                    
                                    # Break the loop as correct guess is found 
                                    
                            # Except block    
                            
                                # Pass the loop iteration
                                
                        # If the password is found break from j for loop   
                        

                    # If the password is found break from k for loop
                    

                # If the password is found break from l for loop
                


        # Finally, if the password is not found even after applying all possible combination of characters upto 4 character length, notify the user as below, else print congratulations
        
        



        

main()
