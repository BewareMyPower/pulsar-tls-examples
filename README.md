# pulsar-tls-examples

Examples for TLS encription. It tested two cases:
1. TLS encryption + JWT authentication
2. TLS encryption + OAuth2 authentication

## Configure the connection info

Before running examples under [python](./python) directory, you should configure some environment variables of the connection info.

For JWT authentication, you should fill the environment variables in [token_env.sh](./token_env.sh) and run:

```bash
source token_env.sh
```

For OAuth2 authentication, you should fill the environment variables in [oauth_env.sh](./oauth_env.sh) and run:

```bash
source oauth_env.sh
```

## Install the Python client

Go to the [python](./python) directory, install the Python client 3.1.0 candidate 3:

```bash
# Choose the wheel according to your OS and Python version
./install.sh https://dist.apache.org/repos/dist/dev/pulsar/pulsar-client-python-3.1.0-candidate-3/linux-glibc-x86_64/pulsar_client-3.1.0-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
```

Then, run:
- `python3 token_tls.py` for JWT authentication
- `python3 oauth_tls.py` for OAuth2 authentication

## Install the Node.js client

Go to the [node](./node) directory, install the Node.js client 1.8.0 candidate 1:

```bash
npm install pulsar-client@1.8.1-rc.1 --pulsar_binary_host_mirror=https://dist.apache.org/repos/dist/dev/pulsar/pulsar-client-node/
```

Then, run:
- `node token_tls.js` for JWT authentication
- `node oauth_tls.js` for OAuth2 authentication

## Test result conclusion

| OS | Authentication | Python | Node.js |
| :- | :- | :- | :- |
| Ubuntu 20.04 | JWT | OK | OK |
| Ubuntu 20.04 | OAuth2 | OK | Failed |
| Windows 10 | JWT | OK | Failed |
| Windows 10 | OAuth2 | OK | Failed |
| macOS Ventura 13.2.1 | JWT | OK | Failed |
| macOS Ventura 13.2.1 | OAuth2 | OK | Failed |

### Test results on Ubuntu 20.04

Python 3.8.10, Node.js v16.19.0.

JWT authentication: both succeeded.

OAuth2 authentication: Python client succeeded, Node.js client failed:

```
[ERROR][AuthOauth2:229] Response failed for getting the well-known configuration <service-url>. Error Code 1: Protocol "pulsar+ssl" not supported or disabled in libcurl
[INFO][ConnectionPool:97] Created connection for <service-url>
[INFO][ClientConnection:388] [172.22.55.227:44116 -> <remote-ip>:6651] Connected to broker
[ERROR][ClientConnection:498] [172.22.55.227:44116 -> <remote-ip>:6651] Failed to establish connection: AuthenticationError
[INFO][ClientConnection:1600] [172.22.55.227:44116 -> <remote-ip>:6651] Connection closed with AuthenticationError
[ERROR][ClientImpl:184] Error Checking/Getting Partition Metadata while creating producer on persistent://public/default/my-topic -- AuthenticationError
[INFO][ClientConnection:269] [172.22.55.227:44116 -> <remote-ip>:6651] Destroyed connection
node:internal/process/promises:279
            triggerUncaughtException(err, true /* fromPromise */);
            ^

[Error: Failed to create producer: AuthenticationError]
```

### Test results on Windows

Python 3.10.9, Node.js v18.12.1.

> **NOTE**:
>
> On Windows, you should replace `python3` with `py` in PowerShell. And you have to set the environment variables manually.

JWT authentication: Python client succeeded, Node.js client failed:

```
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:190] [<none> -> <service-url>] Create ClientConnection, timeout=10000
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ConnectionPool:97] Created connection for <service-url>
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:388] [192.168.16.101:2334 -> <remote-ip>:6651] Connected to broker
[ERROR][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:488] [192.168.16.101:2334 -> <remote-ip>:6651] Handshake failed: unregistered scheme (STORE routines)
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:1600] [192.168.16.101:2334 -> <remote-ip>:6651] Connection closed with ConnectError
[ERROR][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientImpl:184] Error Checking/Getting Partition Metadata while creating producer on persistent://public/default/my-topic -- ConnectError
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:269] [192.168.16.101:2334 -> <remote-ip>:6651] Destroyed connection
node:internal/process/promises:288
            triggerUncaughtException(err, true /* fromPromise */);
            ^

[Error: Failed to create producer: ConnectError]
```

OAuth2 authentication: Python client succeeded, Node.js client failed:

```
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:190] [<none> -> <service-url>] Create ClientConnection, timeout=10000
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ConnectionPool:97] Created connection for <service-url>
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:388] [192.168.16.101:2459 -> <remote-ip>:6651] Connected to broker
[ERROR][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:488] [192.168.16.101:2459 -> <remote-ip>:6651] Handshake failed: unregistered scheme (STORE routines)
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:1600] [192.168.16.101:2459 -> <remote-ip>:6651] Connection closed with ConnectError
[ERROR][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientImpl:184] Error Checking/Getting Partition Metadata while creating producer on persistent://public/default/my-topic -- ConnectError
[INFO][D:\a\pulsar-client-cpp\pulsar-client-cpp\lib\ClientConnection:269] [192.168.16.101:2459 -> <remote-ip>:6651] Destroyed connection
node:internal/process/promises:288
            triggerUncaughtException(err, true /* fromPromise */);
            ^

[Error: Failed to create producer: ConnectError]
```

### Test results on macOS

Python 3.10.9, Node.js v16.17.0.

JWT authentication: Python client succeeded, Node.js client failed:

```
[INFO][ClientConnection:190] [<none> -> <service-url>] Create ClientConnection, timeout=10000
[INFO][ConnectionPool:97] Created connection for <service-url>
[INFO][ClientConnection:388] [10.6.103.176:49745 -> <remote-ip>:6651] Connected to broker
[ERROR][ClientConnection:488] [10.6.103.176:49745 -> <remote-ip>:6651] Handshake failed: certificate verify failed (SSL routines, tls_process_server_certificate)
[INFO][ClientConnection:1600] [10.6.103.176:49745 -> <remote-ip>:6651] Connection closed with ConnectError
[ERROR][ClientImpl:184] Error Checking/Getting Partition Metadata while creating producer on persistent://public/default/my-topic -- ConnectError
[INFO][ClientConnection:269] [10.6.103.176:49745 -> <remote-ip>:6651] Destroyed connection
node:internal/process/promises:279
            triggerUncaughtException(err, true /* fromPromise */);
            ^

[Error: Failed to create producer: ConnectError]
```

OAuth2 authentication: Python client succeeded, Node.js client failed:

```
[INFO][ClientConnection:190] [<none> -> <service-url>] Create ClientConnection, timeout=10000
[ERROR][AuthOauth2:229] Response failed for getting the well-known configuration <service-url>. Error Code 1: Protocol "pulsar+ssl" not supported or disabled in libcurl
[INFO][ConnectionPool:97] Created connection for <service-url>
[INFO][ClientConnection:388] [10.6.103.176:49772 -> <remote-ip>:6651] Connected to broker
[ERROR][ClientConnection:488] [10.6.103.176:49772 -> <remote-ip>:6651] Handshake failed: certificate verify failed (SSL routines, tls_process_server_certificate)
[INFO][ClientConnection:1600] [10.6.103.176:49772 -> <remote-ip>:6651] Connection closed with ConnectError
[ERROR][ClientImpl:184] Error Checking/Getting Partition Metadata while creating producer on persistent://public/default/my-topic -- ConnectError
[INFO][ClientConnection:269] [10.6.103.176:49772 -> <remote-ip>:6651] Destroyed connection
node:internal/process/promises:279
            triggerUncaughtException(err, true /* fromPromise */);
            ^

[Error: Failed to create producer: ConnectError]
```
