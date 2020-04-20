import google_requests as g_r
import mock
import json

numItems = 5 #As instructed by 8th Light

# The first test is based around an example from the Google Books API site
# GET https://www.googleapis.com/books/v1/volumes?q=flowers&orderBy=newest&key=yourAPIKey is the query intended by this test
# https://developers.google.com/books/docs/v1/using#request

def initial_input_test():
	with mock.patch('builtins.input', return_value="1,2"):
		test_output = g_r.initialRequest()
		assert test_output == [False, [True, True, False, False, False, False, False]]
	return test_output

def get_intitle_test():
	with mock.patch('builtins.input', return_value="flowers"):
		test_output = g_r.get_intitle()
		assert test_output == [True, 'flowers']
	return test_output

def get_inauthor_test(isPrevTrue, URL):
	with mock.patch('builtins.input', return_value="keyes"):
		test_output = g_r.get_inauthor(isPrevTrue, URL)
		assert test_output == [True, 'flowers+inauthor:keyes']
	return test_output

def sendGET_test(URL_PARAMS):
	test_output = g_r.sendGET(URL_PARAMS)
	return test_output


def addToReadingList_test(data):
	with mock.patch('builtins.input', return_value="1,2"):
		data = g_r.getNItems(numItems, data)
		info = g_r.getInfo(numItems,data)
		test_output = g_r.addToReadingList(numItems,info,False)
	print('\nThe selected choices are:\n')
	print(test_output)


if __name__ == '__main__':
    [skip, params]  = initial_input_test()
    [isPrevTrue, URL] = get_intitle_test()    
    [isPrevTrue, URL] = get_inauthor_test(isPrevTrue, URL)
    [data, URL] = sendGET_test(URL)
    addToReadingList_test(data)

   