#!/usr/bin/env python
import pika
import ssl

credentials = pika.PlainCredentials('rabbitmq-admin', 'My-Secret-Password')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def produce():
    #Create Connection channel
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='Some-Remote-Host',virtual_host='/',port=5671,credentials=credentials,ssl_options=pika.SSLOptions(ctx)))
    channel = connection.channel()
    # Publish message onto Queue
    channel.basic_publish(exchange='amq.fanout', routing_key='A-Routing-Key', body=b'{"DevId":"Refrigerator01","Temp":69}')
    print(" [x] Change Temperature for Refrigerator01")
    connection.close()

###
# Program to send temperature telemetry to a fridge
###
if __name__ == '__main__':
    produce()



