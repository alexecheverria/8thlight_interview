# Google Books Search and Reading List Creator

This codebase is used to create a local reading list using the Google Books API. The code is meant to retreive user inputted queries from the command line and return 5 search results to add to a local reading list. The list is updated as long as the user is running the program. Following termination, the program will output a reading list file. Users can choose to append to this list if they so choose. 

**The following are potential search parameters a user can specify in order to narrow their search.
1. intitle: Returns results where the text following this keyword is found in the title.
1. inauthor: Returns results where the text following this keyword is found in the author.
1. inpublisher: Returns results where the text following this keyword is found in the publisher.
1. subject: Returns results where the text following this keyword is listed in the category list of the volume.
1. isbn: Returns results where the text following this keyword is the ISBN number.
1. lccn: Returns results where the text following this keyword is the Library of Congress Control Number.
1. oclc: Returns results where the text following this keyword is the Online Computer Library Center number.


Instructions: Run the program by entering **python google_books.py**

You will then be prompted to enter which of the search parameters you would like to select. If you would like to skip this step press enter. If you want to use any of these parameters enter a list of numbers with the selection desired. 

**Example:**

*User Input = 1,2,5,6*

You will then be prompted a question for each parameter. When you type in your answer, press enter. In the example above the user will be prompted to provide the *title, author, isbn, and lccn.*