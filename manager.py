from paho.mqtt.client import Client
import paho.mqtt.subscribe as subscribe
from multiprocessing import Process

class Seller:
    def __init__(self, number_items, broker = 'localhost', auth = None):
        self.number_of_items = number_items
        self.auth = auth
        self.client = Client()
        self.client.connect(broker)

    def sell(self, update = False):
        self.client.publish('Available items', '1 2 3')
        while update:
            self.client.publish('Available items', '1 2 3')
            time.sleep(3*random.random())
        


def on_message_mngr(client, userdata, msg):
    print(userdata, msg.topic, msg.payload)

class Manager:
    def __init__(self, broker = 'localhost', auth = None):
        self.broker = broker
        self.auth = auth

def on_message_pb(client, userdata, msg):
    #print(userdata, msg.topic, msg.payload)
    client.publish('results', msg.payload)

def results_publisher():
    client = Client()
    #client.username_pw_set("publisher", "publisherpassword")
    client.connect('test.mosquitto.org')
    client.on_message = on_message_pb
    client.subscribe('items/#')
    client.loop_forever()

def manager_view():
    client = Client()
    #client.username_pw_set("manager", "managerpassword")
    client.connect('test.mosquitto.org')
    client.on_message = on_message_mngr
    #client.subscribe('items/#')
    client.subscribe('results')
    client.loop_forever()

    
if __name__ == '__main__':
    BROKER = 'test.mosquitto.org'
    
    seller = Seller(2, BROKER)
    seller.sell()

    Process(target = manager_view, args = ()).start()
    Process(target = results_publisher, args = ()).start()
    



