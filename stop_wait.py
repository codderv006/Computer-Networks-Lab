import time

def sender(message):
    print("Sending the message:", message)
    time.sleep(len(message) / 7)
    print('Message sent')
    return message

def receiver(message):
    print("Waiting for the message to receive")
    time.sleep(len(message) / 7)  # Receiver should wait for the same duration as the sender
    print("Received:", message)
    print("Sending acknowledgment")
    time.sleep(len(message) / 7)  # Acknowledgment time should be consistent
    print("Sent the acknowledgment")

message = 'LOL'
acknowledgment = None

while acknowledgment != message:
    acknowledgment = sender(message)
    receiver(acknowledgment)

print("Communication completed.")
