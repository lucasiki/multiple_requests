import requests
from threading import Thread
from time import time

class TemplateRequest:
    
    def __init__(self, url, headers, data, method='GET', **kwargs):
        self.method = method
        self.url = url
        self.headers = headers
        self.payload = data
        self.kwargs = kwargs
            
    @property
    def data(self):
        return {'method': self.method, 'url': self.url, 'headers': self.headers, 'data': self.payload, **self.kwargs}
    
    def prepare_thread(self):
        data = requests.request(**self.data)
        self.result = data
        
    def run_thread(self):
        self.thread = Thread(target=self.prepare_thread)
        self.thread.start()
        
    def join(self):
        self.thread.join()

        

def multiple_requests(data: list):
    
    data = [TemplateRequest(**each) for each in data]
    
    thread = [each.run_thread() for each in data]
    [each.join() for each in data]
    return [each.result for each in data]


if __name__ == '__main__':
    time1 = time()
    t1 = {"url":'http://example.com', "headers":{'Authorization': 'test1'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
    t2 = {"url":'http://example.com', "headers":{'Authorization': 'test2'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
    t3 = {"url":'http://example.com', "headers":{'Authorization': 'test3'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
    t4 = {"url":'http://example.com', "headers":{'Authorization': 'test4'}, "data":{'test': 'test'}, "method": 'POST', "timeout":10}
    result = multiple_requests([t1,t2,t3,t4])
    print(result)
    
    time2 = time()
    
    data = [TemplateRequest(**each) for each in [t1,t2,t3,t4]]
    
    result = []
    for each in data:
        result.append(requests.request(**each.data))
    print(result)
    
    time3 = time()
    
    print(f"First groups of requests took {time2-time1} seconds and the second group of requests took {time3-time2}")
        
