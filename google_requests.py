# importing the requests library 
import requests 

# This function asks the user if they would like to search with additional parameters that Google Books provides
def initialRequest():
	initialRequest = "\nWhich search parameters do you know?\n"
	initialRequest += "Please enter digits followed by commas, do not use spaces\n"
	initialRequest += "If you want to just search by Title(1) press Enter\n"
	initialRequest += "1, intitle: Returns results where the text following this keyword is found in the title.\n"
	initialRequest += "2, inauthor: Returns results where the text following this keyword is found in the author.\n"
	initialRequest += "3, inpublisher: Returns results where the text following this keyword is found in the publisher.\n"
	initialRequest += "4, subject: Returns results where the text following this keyword is listed in the category list of the volume.\n"
	initialRequest += "5, isbn: Returns results where the text following this keyword is the ISBN number.\n"
	initialRequest += "6, lccn: Returns results where the text following this keyword is the Library of Congress Control Number.\n"
	initialRequest += "7, oclc: Returns results where the text following this keyword is the Online Computer Library Center number.\n\n"
	#Command Line Search
	searchParameters = input(initialRequest)
	skip = (searchParameters == '')
	confirmedSearchParameters = [False,False,False,False,False,False,False]
	if(skip == False):
		splitSearchParameters = searchParameters.split(',')
		for i in range(len(splitSearchParameters)):
			if(splitSearchParameters[i] in ['1', '2', '3', '4', '5', '6', '7']):
				confirmedSearchParameters[int(splitSearchParameters[i])-1] = True
	return [skip, confirmedSearchParameters]


# Returns results where the text following this keyword is found in the title.
def get_intitle():
	URL = input("\nWhat is the title you are looking for? \n") 	
	isPrevTrue = True
	return [isPrevTrue, URL]

# Returns results where the text following this keyword is found in the author.
def get_inauthor(isPrevTrue, URL):
	inauthor = input("\nDoes your title have a specific author? \n") 
	#If the previous selection was chosen, add a + char to add another search parameter
	if(isPrevTrue):
		URL += "+"	
	URL += "inauthor:"
	URL += inauthor
	isPrevTrue = True
	return [isPrevTrue, URL]

# Returns results where the text following this keyword is found in the publisher.
def get_inpublisher(isPrevTrue, URL):
	inpublisher = input("\nDoes your title have a specific publisher?\n") 
	#If the previous selection was chosen, add a + char to add another search parameter
	if(isPrevTrue):
		URL += "+"	
	URL += "inpublisher:"
	URL += inpublisher
	isPrevTrue = True
	return [isPrevTrue, URL]

# Returns results where the text following this keyword is listed in the category list of the volume.
def get_subject(isPrevTrue, URL):
	subject = input("\nWhat keywords can be used to describe the subject of your title?\n")
	#If the previous selection was chosen, add a + char to add another search parameter
	if(isPrevTrue):
		URL += "+"	
	URL += "subject:"
	URL += subject
	isPrevTrue = True
	return [isPrevTrue, URL]

# Returns results where the text following this keyword is the ISBN number.
def get_isbn(isPrevTrue, URL):
	isbn = input("\nDo you have your title's ISBN Number?\n")
	#If the previous selection was chosen, add a + char to add another search parameter
	if(isPrevTrue):
		URL += "+"	
	URL += "isbn:"
	URL += isbn
	isPrevTrue = True
	return [isPrevTrue, URL]

# Returns results where the text following this keyword is the Library of Congress Control Number.
def get_lccn(isPrevTrue, URL):
	lccn = input("\nDo you have your title's Library of Congress Control Number?\n")
	#If the previous selection was chosen, add a + char to add another search parameter
	if(isPrevTrue):
		URL += "+"	
	URL += "lccn:"
	URL += lccn
	isPrevTrue = True
	return [isPrevTrue, URL]

# Returns results where the text following this keyword is the Online Computer Library Center Number.
def get_oclc(isPrevTrue, URL):
	oclc = input("\nDo you have your title's Online Computer Library Center Number?\n ")
	#If the previous selection was chosen, add a + char to add another search parameter
	if(isPrevTrue):
		URL += "+"	
	URL += "oclc:"
	URL += oclc
	isPrevTrue = True
	return [isPrevTrue, URL]


# This function sends a GET request to Google Books and returns with a search result. The result is then
# parsed in a JSON format
def sendGET(URL_PARAMS):
	# api-endpoint 
	URL = "https://www.googleapis.com/books/v1/volumes?q="
	URL += URL_PARAMS
	#Add API key to the URL
	URL +=  "&key=AIzaSyAClCV8tsH1Y_zrVPKmTxu8eiOnMiSCG-A"
	# sending get request and saving the response as response object 
	request_response = requests.get(url = URL)  
	# extracting data in json format 
	google_books_data = request_response.json() 
	return [google_books_data, URL]

# Function retreives items from Google Books Response data, used for automation in case the user wants
# more than 5 results at a time
def getNItems(n,data):
	return data['items'][:n]

# This function extracts the title, author, and publisher from Google Books data. If a detail is not 
# listed this function adds a note saying the detail could not be extracted
def getInfo(n,data):
	info = [0]*n
	for i in range(n):
		try:
			title = data[i]['volumeInfo']['title']
		except:
			title = "Title not listed for this item"
		try:
			author =  data[i]['volumeInfo']['authors']
		except: 
			author = "Author not found for this item"
		try:	
			publisher = data[i]['volumeInfo']['publisher']
		except:
			publisher = "Publisher not found for this item"

		info[i] = [title, author, publisher]
	printInfo(n,info)
	return info

# This function prints N Google Search Results for the user to choose to add to their Reading List
def printInfo(n, info):
	print('Search Results')
	list_type = type(info)
	info_output = ''
	for i in range(n):
		info_output += '\n'
		info_output += str(i+1)
		info_output += '. Title: '
		if(type(info[i][0]) == list_type): #If Google Books provided a list, remove the '['' ']' chars'
			info_output += ', '.join(info[i][0])
		else:
			info_output += info[i][0]

		info_output += '\n   Author(s): '
		if(type(info[i][1]) == list_type):
			info_output += ', '.join(info[i][1])
		else:
			info_output += info[i][1]
		info_output += '\n   Publisher: '
		if(type(info[i][2]) == list_type):
			info_output += ', '.join(info[i][2])
		else:
			info_output += info[i][2]
		print(info_output)
	


def addToReadingList(n, info, append):
	list_type = type(info)
	select_input = "\nWhich selection would you like to add to your reading list? \n"
	select_input += "Please enter digits followed by commas with no spaces\n"
	selection = input(select_input)
	selection = selection.split(',')
	confirmed_selections = [0]*n	
	added_books = ''

	#Create a list of selections, this ensures a double selection only results in 
	#one added item
	for i in range(len(selection)):
		if(selection[i] in ['1','2','3','4','5']):
			confirmed_selections[int(selection[i])-1] = info[int(selection[i])-1]

	for i in range(n):
		if(confirmed_selections[i] != 0):
			added_books += '---------------------------------------\n'
			added_books += 'Title: '
			if(type(confirmed_selections[i][0]) == list_type):
				added_books += ', '.join(confirmed_selections[i][0])
			else:
				added_books += confirmed_selections[i][0]
			added_books += '\nAuthor(s): '
			if(type(confirmed_selections[i][1]) == list_type):
				added_books += ', '.join(confirmed_selections[i][1])
			else:
				added_books += confirmed_selections[i][1]
			added_books += '\nPublisher: '
			if(type(confirmed_selections[i][2]) == list_type):
				added_books += ', '.join(confirmed_selections[i][2])
			else:
				added_books += confirmed_selections[i][2]
			added_books += "\n"
	if(append):
		reading_list = open("reading_list.log", "a")
	else:
		reading_list = open("reading_list.log", "w")
	reading_list.write(added_books)
	reading_list.close()
	return added_books

def addAnotherItem():
	addAnother = input("\nWould you like to add more items? Please enter 'y' or 'n'\n")
	if(addAnother == 'Y' or addAnother == 'y'):
		return True 
	elif(addAnother == 'n' or addAnother == 'n'):
		return False
	else:
		print("Please select a valid option")
		return addAnotherItem()



