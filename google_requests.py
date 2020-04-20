# importing the requests library 
import requests 


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



def get_intitle(isPrevTrue, URL):
	# Returns results where the text following this keyword is found in the title.
	intitle = input("\nWhat is the title you are looking for? \n") 
	URL += intitle
	isPrevTrue = True
	return [URL, isPrevTrue]

def get_inauthor(isPrevTrue, URL):
	# Returns results where the text following this keyword is found in the author.
	inauthor = input("\nDoes your title have a specific author? \n") 
	if(isPrevTrue):
		URL += "+"	
	URL += "inauthor:"
	URL += inauthor
	isPrevTrue = True
	return [URL, isPrevTrue]

def get_inpublisher(isPrevTrue, URL):
	# Returns results where the text following this keyword is found in the publisher.
	inpublisher = input("\nDoes your title have a specific publisher?\n") 
	if(isPrevTrue):
		URL += "+"	
	URL += "inpublisher:"
	URL += inpublisher
	isPrevTrue = True
	return [URL, isPrevTrue]

def get_subject(isPrevTrue, URL):
	# Returns results where the text following this keyword is listed in the category list of the volume.
	subject = input("\nWhat keywords can be used to describe the subject of your title?\n")
	if(isPrevTrue):
		URL += "+"	
	URL += "subject:"
	URL += subject
	isPrevTrue = True
	return [URL, isPrevTrue]

def get_isbn(isPrevTrue, URL):
	# Returns results where the text following this keyword is the ISBN number.
	isbn = input("\nDo you have your title's ISBN Number?\n")
	if(isPrevTrue):
		URL += "+"	
	URL += "isbn:"
	URL += isbn
	isPrevTrue = True
	return [URL, isPrevTrue]

def get_lccn(isPrevTrue, URL):
	# Returns results where the text following this keyword is the Library of Congress Control Number.
	lccn = input("\nDo you have your title's Library of Congress Control Number?\n")
	if(isPrevTrue):
		URL += "+"	
	URL += "lccn:"
	URL += lccn
	isPrevTrue = True
	return [URL, isPrevTrue]

def get_oclc(isPrevTrue, URL):
	# Returns results where the text following this keyword is the Online Computer Library Center Number.
	oclc = input("\nDo you have your title's Online Computer Library Center Number?\n ")
	if(isPrevTrue):
		URL += "+"	
	URL += "oclc:"
	URL += oclc
	isPrevTrue = True
	return [URL, isPrevTrue]



def sendGET(URL_PARAMS):
	# api-endpoint 
	URL = "https://www.googleapis.com/books/v1/volumes?q="
	URL += URL_PARAMS
	#Add API key to the URL
	API_KEY= "AIzaSyAClCV8tsH1Y_zrVPKmTxu8eiOnMiSCG-A"
	URL += "&key="
	URL += API_KEY
	# sending get request and saving the response as response object 
	r = requests.get(url = URL)  
	# extracting data in json format 
	data = r.json() 
	return [URL, data]


def getNItems(n,data):
	return data['items'][:n]

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

	return info

def printInfo(n, info):
	print('Search Results')
	list_type = type(info)
	for i in range(n):
		search_result = '\n'
		search_result += str(i+1)
		search_result += '. Title: '
		if(type(info[i][0]) == list_type):
			search_result += ', '.join(info[i][0])
		else:
			search_result += info[i][0]

		search_result += '\n   Author(s): '
		if(type(info[i][1]) == list_type):
			search_result += ', '.join(info[i][1])
		else:
			search_result += info[i][1]
		search_result += '\n   Publisher: '
		if(type(info[i][2]) == list_type):
			search_result += ', '.join(info[i][2])
		else:
			search_result += info[i][2]
		print(search_result)


def addToReadingList(n, info):
	select_input = "\nWhich selection would you like to add to your reading list? \n"
	select_input += "Please enter digits followed by commas with no spaces\n"
	selection = input(select_input)
	confirmedSelections = [0]*n

	selection = selection.split(',')
	print(selection)
	for i in range(len(selection)):
		if(selection[i] in ['1','2','3','4','5']):
			confirmedSelections[int(selection[i])-1] = info[int(selection[i])-1]
	return confirmedSelections




