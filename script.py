import socket
import threading
import base64
import random
import string
import time
import logging

logging.basicConfig(filename='/var/log/journal/tcpserver.log', level=logging.INFO)

def encrypt_message(message):
    message_bytes = message.encode('ascii')
    return base64.b64encode(message_bytes).decode()

def handle_client(client_socket):
    TIMEOUT_SECONDS = 1 
    GIFT_MESSAGE = "Congratulations! You responded to all messages in time. Here's your gift : y0urF1v0r1t3CMS\n"
    with open('/root/resources/cyber.txt', 'r') as file:
        lines = file.readlines()
    length = len(lines)

    for i in range(20):
        original_word = lines[random.randint(0, length-1)]
        original_word = original_word.strip()
        encrypted_message = encrypt_message(original_word) + '\n'
        client_socket.send(encrypted_message.encode())

        client_socket.settimeout(TIMEOUT_SECONDS)

        try:
            client_response = client_socket.recv(1024).decode().strip()

            if client_response == original_word:
                test = 0
                logging.info(f"Correct! Original word: {original_word}")
            else:
                client_socket.send(f"Incorrect.\n".encode())
                client_socket.close()
                return
        except socket.timeout:
            logging.info("Timeout. Closing the connection.")
            client_socket.send("Timeout: Response not received in time.\n".encode())
            client_socket.close()
            return

        time.sleep(1)

    client_socket.send(GIFT_MESSAGE.encode())
    client_socket.close()
    return

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 19))
    server.listen(5)
    logging.info("[*] Listening on 0.0.0.0:1234")

    while True:
        client, addr = server.accept()
        logging.info(f"[*] Accepted connection from {addr[0]}:{addr[1]}")
        
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
