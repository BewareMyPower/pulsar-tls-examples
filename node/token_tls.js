const Pulsar = require('pulsar-client');

(async () => {
    Pulsar.Client.setLogHandler((level, file, line, message) => {
        console.log('[%s][%s:%d] %s', Pulsar.LogLevel.toString(level), file, line, message);
    });

    const auth = new Pulsar.AuthenticationToken({
        token: process.env.PULSAR_TOKEN,
    })

    const client = new Pulsar.Client({
        serviceUrl: process.env.PULSAR_SERVICE_URL,
        authentication: auth,
    });

    const producer = await client.createProducer({
        topic: process.env.PULSAR_TOPIC,
    });

    const msg_id = await producer.send({
        data: Buffer.from(`hello`),
    });
    console.log(msg_id)

    await producer.close();
    await client.close();
})();
