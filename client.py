import socket
import base64

def decode_message(encoded_message):
    decoded_bytes = base64.b64decode(encoded_message)
    decoded_message = decoded_bytes.decode('ascii')
    return decoded_message

def start_client():
    server_address = ('IP', 2023) # put your IP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(server_address)
    print(f"Connected to {server_address}")

    for i in range(0,20):
        received_data = client.recv(1024).decode().strip()
        
        if not received_data:
            break 

        print(f"Received encoded message: {received_data}")

        decoded_message = decode_message(received_data)
        print(f"Decoded message: {decoded_message}")

        client.send(decoded_message.encode())
    client.close()

if __name__ == "__main__":
    start_client()
