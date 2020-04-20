This codebase is used to create a local reading list using the Google Books API. The code is meant to retreive user inputted queries from the command line and return 5 search results to add to a local reading list. The list is updated as long as the user is running the program. Following termination, the program will output a reading list file. Users can choose to append to this list if they so choose. 

The following are potential search parameters a user can specify in order to narrow their search.

intitle: Returns results where the text following this keyword is found in the title.
inauthor: Returns results where the text following this keyword is found in the author.
inpublisher: Returns results where the text following this keyword is found in the publisher.
subject: Returns results where the text following this keyword is listed in the category list of the volume.
isbn: Returns results where the text following this keyword is the ISBN number.
lccn: Returns results where the text following this keyword is the Library of Congress Control Number.
oclc: Returns results where the text following this keyword is the Online Computer Library Center number.


Instructions: Run the program using python ____.py

You will then be prompted to enter which of the search parameters you would like to select. If you would like to skip this step press enter. If you want to use any of these parameters enter a list of numbers with the selection desired. Ex:

1,2,5,6

You will then be prompted a question for each parameter. When you type in your answer, press enter. 