# -------------------
# Install PyPDF2 library using below command
# pip3 install 'PyPDF2<3.0'

# Dictionary Attack
# --------------------

import PyPDF2 as pd


def main():
    # Get the target file path from the user and use strip() method and store it in filename variable
    

    # Call open() function and pass it filename and 'rb', store result in file variable
    
    # Call pd.pdfFilereader(file) to read pdf and store it in pdfReader variable
    

    attempts = 0

    # Add if condition to checks if the file is password encrypted
    
        # Print 'The file is not password protected! You can successfully open it!'
        
    # Else:
    
        # Use open() function to read wordlist.txt and store result in wordListFile
        
        # USe read() and lower() method on wordListFile to convert each character to lowercase and store result in body variable
        
        # Use split('\n') method on body to get words and store the list in words variable
        
        
        # loop through each index in words list
        
            # get words[i] in word
        
            # Print f'Trying to decode password by: {word}'
        
           
            # Use pdfReader.decrypt(word) to get the result
        
            # Check if result is 1
        
                # Print f"Congratulations!!! The password is {word}."
        
                # break the loop
        
        
            # Else check if result is 0
        
                # Increment attempts variable by 1
        
                # Print f'Passwords attempts: {str(attempts)}'
        
                # Continue to next iteration of the loop
        
        
main()
