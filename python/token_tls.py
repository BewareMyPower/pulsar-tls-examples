import os
import pulsar

if __name__ == '__main__':
    service_url = os.environ['PULSAR_SERVICE_URL']
    topic = os.environ['PULSAR_TOPIC']
    token = os.environ['PULSAR_TOKEN']

    auth = pulsar.AuthenticationToken(token)
    client = pulsar.Client(service_url, authentication=auth)
    producer = client.create_producer(topic)
    msg_id = producer.send('hello'.encode())
    print(f'Sent to {msg_id}')
    producer.close()
    client.close()
