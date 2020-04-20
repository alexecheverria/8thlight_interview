import google_requests as g_r
import requests
import mock
import json

def initial_input_test():
	with mock.patch('builtins.input', return_value="1,2"):
		test_output = g_r.initialRequest()
		assert test_output == [False, [True, True, False, False, False, False, False]]
	return test_output

def get_intitle_test(isPrevTrue, URL):
	with mock.patch('builtins.input', return_value="flowers"):
		test_output = g_r.get_intitle(isPrevTrue, URL)
		assert test_output == ['flowers', True]
	return test_output

def get_inauthor_test(isPrevTrue, URL):
	with mock.patch('builtins.input', return_value="keyes"):
		test_output = g_r.get_inauthor(isPrevTrue, URL)
		assert test_output == ['flowers+inauthor:keyes', True]
	return test_output

def sendGET_test(URL_PARAMS):
	test_output = g_r.sendGET(URL_PARAMS)
	return test_output


if __name__ == '__main__':
    init_test_out = initial_input_test()
    skip = init_test_out[0]
    params = init_test_out[1]
    get_intitle_test_out = get_intitle_test(False, '')
    URL = get_intitle_test_out[0]
    prevTrue = get_intitle_test_out[1]
    get_inauthor_test_out = get_inauthor_test(prevTrue, URL)
    URL = get_inauthor_test_out[0]
    prevTrue = get_inauthor_test_out[1]
    sendGET_test_out = sendGET_test(URL)
    URL = sendGET_test_out[0]
    data = sendGET_test_out[1]
    data = g_r.getNItems(5, data)
    info = g_r.getInfo(5,data)
    g_r.printInfo(5, info)
    print(g_r.addToReadingList(5,info,False))

    #for i in range(10):
    #	print(data['items'][i]['volumeInfo']['title'])