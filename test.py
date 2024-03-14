from azure.communication.email import EmailClient
def main():
    try:
        connection_string = "os.environ.get('CONNECTION_STRING')"
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "os.environ.get('SENDER_ADDRESS')",
            "recipients":  {
                "to": [{"address": "daniiagudelom@gmail.com" }],
            },
            "content": {
                "subject": "Correo electrónico de prueba",
                "plainText": "DESDE VS NUEVO.",
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)
main()
