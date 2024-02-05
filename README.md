# multiple_requests
A small lib to make multiple parallel requests

It's necessary to have requests library
pip install requests

just import multiple_requests from main and use multiple_requests(ListOfData)

Your list of data should follow like the example 

t1 = {"url":'http://example.com', "headers":{'Authorization': 'test1'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
t2 = {"url":'http://example.com', "headers":{'Authorization': 'test2'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
t3 = {"url":'http://example.com', "headers":{'Authorization': 'test3'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
t4 = {"url":'http://example.com', "headers":{'Authorization': 'test4'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
result = multiple_requests([t1,t2,t3,t4])

and the result will always be awaited.

*obs, it accepts any additional parameter from requests.
