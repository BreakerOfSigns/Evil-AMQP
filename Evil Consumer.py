import pika, sys, os
import ssl

credentials = pika.PlainCredentials('rabbitmq-admin', 'My-Secret-Password')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def consume():
    #Create Connection channel
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='Some-Remote-Host',virtual_host='/',port=5671,credentials=credentials,ssl_options=pika.SSLOptions(ctx)))
    channel = connection.channel()

    #Set consumption parameters
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)
    channel.basic_consume(queue='Some-Queue-To-Consume', on_message_callback=callback, auto_ack=True)

    #Begin consuming
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
###
# Program to wait on a queue an consume messages
###
if __name__ == '__main__':
    try:
        consume()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)