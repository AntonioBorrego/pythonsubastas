import paho.mqtt.publish as publish
from paho.mqtt.client import Client
from multiprocessing import Process
import random, time


def buy(items, user):
    usr, pwd = user
    client = Client(userdata = usr)
    #client.username_pw_set(usr, pwd)
    client.connect('test.mosquitto.org')
    client.loop_start()
    for i in range(10):
        for item in items:
            cost = random.randint(1, 20)
            client.publish(str(item), str(cost))
            print('cliente', usr, 'puja', cost, 'por', item)
            time.sleep(2*random.random())


    
if __name__ == '__main__':
    lst = ['items/1', 'items/2',
           'items/3', 'items/4']
    
    

    users_list = [("client1", "client1password"),
                 ("client2", "client2password"),
                 ("client3", "client3password")]
    
    for user in users_list:
        Process(target = buy, args = (lst, user)).start()
        

    
