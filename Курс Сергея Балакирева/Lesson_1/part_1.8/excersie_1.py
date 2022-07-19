class Server:
    IP = -1
    def __new__(cls):
        cls.IP += 1
        return super().__new__(cls)
    
    def __init__(self):
        self.ip = self.IP
        self.buffer = []
        
    def send_data(self, data):
        if self.ip in Router.servers:
            Router.buffer.append(data)
    
    def get_data(self):
        data = self.buffer.copy()
        self.buffer.clear()
        return data
    
    def get_ip(self):
        return self.ip
    
    
class Router:
    buffer = []
    servers = {}
    @classmethod
    def link(cls, server):
        cls.servers[server.ip] = server
    
    @classmethod
    def unlink(cls, server):
        if server.ip in cls.servers:
            cls.servers.pop(server.ip)
    
    @classmethod
    def send_data(cls):
        for srv in cls.buffer:
            if srv.ip in cls.servers:
                cls.servers[srv.ip].buffer.append(srv)
        cls.buffer.clear()
                
                
    
    
class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
