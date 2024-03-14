import os 
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)


# Carga las variables de entorno desde el archivo .env
load_dotenv()

from azure.communication.email import EmailClient

@app.route("/send-email", methods=["POST"])
def send_email():
    #Obtener datos del cuerpo del request
    data = request.json

    #verificar que los datos necesarios estén presentes en el request
    if 'email' not in data or 'subject' not in data or 'body' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        connection_string = os.environ.get('CONNECTION_STRING')
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": os.environ.get('SENDER_ADDRESS'),
            "recipients":  {
                "to": [{"address": data['email']}],
            },
            "content": {
                "subject": data['subject'],
                "plainText": data['body'],
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

        return jsonify("bien")
    
    except Exception as ex:
        return jsonify("MAl")

if __name__ == "__main__":
    app.run(debug=True)