class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, requests, *rgs, **kwargs):
        if 'method' in requests and requests['method'] != 'GET':
            return None
        else:
            return self.get(self.func, requests)

    def get(self, func, request, *args, **kwargs):
        return 'GET: ' + func(request)
