import google_requests as g_r
import os

numItems = 5 #As instructed by 8th Light

if __name__ == '__main__':
	addAnotherItem = True
	append = False
	while(addAnotherItem):
		URL = ''
		isPrevTrue = False
		[skip, confirmedSearchParameters] = g_r.initialRequest()

		if(confirmedSearchParameters[0] or skip):
			[isPrevTrue, URL] = g_r.get_intitle()
		
		if(confirmedSearchParameters[1] and (not skip)):
			[isPrevTrue, URL] = g_r.get_inauthor(isPrevTrue, URL)
		
		if(confirmedSearchParameters[2] and (not skip)):
			[isPrevTrue, URL] = g_r.get_inpublisher(isPrevTrue, URL)
		
		if(confirmedSearchParameters[3] and (not skip)):
			[isPrevTrue, URL] = g_r.get_subject(isPrevTrue, URL)
		
		if(confirmedSearchParameters[4] and (not skip)):
			[isPrevTrue, URL] = g_r.get_isbn(isPrevTrue, URL)

		if(confirmedSearchParameters[5] and (not skip)):
			[isPrevTrue, URL] = g_r.get_lccn(isPrevTrue, URL)
		
		if(confirmedSearchParameters[6] and (not skip)):
			[isPrevTrue, URL] = g_r.get_oclc(isPrevTrue, URL)


		[google_books_data, URL] = g_r.sendGET(URL)

		google_books = g_r.getNItems(numItems, google_books_data)

		google_books_info = g_r.getInfo(numItems, google_books)

		added_books = g_r.addToReadingList(numItems, google_books_info, append)

		append = True
		addAnotherItem = g_r.addAnotherItem()

	print('\nHere is your reading list:')
	os.system('cat reading_list.log')
