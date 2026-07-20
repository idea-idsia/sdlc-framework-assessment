from datetime import datetime
import bcrypt

class Message:
    def __init__(self):
        self.id = None
        self.ticket_id = 0
        self.sender_id = 0
        self.receiver_id = 0
        self.content = ""
        self.timestamp = datetime.now()

class MessageHandler:
    @staticmethod
    def send_message(content, receiver_id):
        message = Message()
        message.content = content
        message.sender_id = 1  # Assuming the sender is always user with id 1
        message.receiver_id = receiver_id
        message.timestamp = datetime.now()
        
        return True

    @staticmethod
    def receive_messages(ticket_id):
        messages = []
        # Placeholder for actual data retrieval logic.
        # For demonstration purposes, we will just simulate receiving a list of messages.
        if ticket_id == 1:
            messages.append({"id": 1, "sender_id": 2, "receiver_id": 1, "content": "Hello", "timestamp": datetime(2023, 9, 15, 14, 30)})
            messages.append({"id": 2, "sender_id": 1, "receiver_id": 2, "content": "Hi there!", "timestamp": datetime(2023, 9, 15, 14, 35)})
        return messages

    @staticmethod
    def update_message_status(message_id, new_status):
        # Placeholder for actual data retrieval and updating logic.
        # For demonstration purposes, we will just simulate the status change.
        if message_id == 1:
            MessageHandler.receive_messages(1)  # Simulate receiving messages to update the status
            return True
        
        return False

# Example usage of MessageHandler class methods
if __name__ == "__main__":
    send_status = MessageHandler.send_message("Hello, how are you?", 2)
    print(f"Message sent: {send_status}")

    received_messages = MessageHandler.receive_messages(1)
    for message in received_messages:
        print(message)

    update_status = MessageHandler.update_message_status(1)
    print(f"Status updated: {update_status}")
