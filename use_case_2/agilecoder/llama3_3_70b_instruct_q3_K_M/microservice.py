'''
The Microservice class that represents a microservice.
'''
from service1 import Service1
from service2 import Service2
from service3 import Service3
class Microservice:
    def __init__(self, db):
        self.service1 = Service1(db)
        self.service2 = Service2(db)
        self.service3 = Service3(db)
    def start(self):
        pass
    def stop(self):
        pass