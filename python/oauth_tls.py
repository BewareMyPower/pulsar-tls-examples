import os
import pulsar

if __name__ == '__main__':
    service_url = os.environ['PULSAR_SERVICE_URL']
    topic = os.environ['PULSAR_TOPIC']
    issuer_url = os.environ['PULSAR_ISSUER_URL']
    private_key = os.environ['PULSAR_PRIVATE_KEY']
    audience = os.environ['PULSAR_AUDIENCE']

    auth = pulsar.AuthenticationOauth2(f'''{{
        "issuer_url": "{issuer_url}",
        "private_key": "{private_key}",
        "audience": "{audience}"
    }}''')

    client = pulsar.Client(service_url,
                           authentication=auth,
                           tls_allow_insecure_connection=False,
                           tls_validate_hostname=True)
    producer = client.create_producer(topic)
    msg_id = producer.send('hello'.encode())
    print(f'Sent to {msg_id}')
    producer.close()
    client.close()
