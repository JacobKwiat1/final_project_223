# Current setup per dm session:
# create instance of DM_Session ( example: dm = DM_Session(sender_username, receiver_username) )
# How to send messages:
# dm.send(message)


import logging
import datetime
import json
from pathlib import Path
    
class ChatJSONFormatter(logging.Formatter):
    def __init__(self):
        pass

    def format(self, record):
        # Log record passed dictionary
        msg_data = record.msg.copy()

        # Message log format
        entry = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "sender": msg_data["sender"],
            "receiver": msg_data["receiver"],
            "message": msg_data["message"]
        }

        return json.dumps(entry)

class DM_Session:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.filename = f"{sender}-{receiver}.txt" if sender < receiver else f"{receiver}?{sender}.txt"

        self.chat_logger = self.chat_logs_setup()
        
    def chat_logs_setup(self, level = logging.INFO):
        # Assign ChatJsonFormatter class object to formatter
        formatter = ChatJSONFormatter()

        # File Handler
        handler = logging.FileHandler(self.get_path())
        handler.setFormatter(formatter)

        # Logger configuration
        logger = logging.getLogger(f"ChatLogs_{self.filename}")
        logger.setLevel(level)
        logger.addHandler(handler)

        # No root logger
        logger.propagate = False

        return logger
        
    def get_path(self):
        # Set directory path
        base_dir = Path(__file__).parent.resolve() / "Logs"

        # Make directory if it doesn't exit
        base_dir.mkdir(exist_ok = True)

        # Resolve the path
        file_path = (base_dir / self.filename).resolve()

        # Path sanitizer for traversal check
        if not file_path.is_relative_to(base_dir):
            raise ValueError("Path traversal detected.")
        else:
            return str(file_path)
        
    def send(self, msg):
        self.chat_logger.info({"sender": self.sender, "receiver": self.receiver, "message": msg})

    def print_msgs(self):
        msg = {}
        with open(self.get_path(), "r") as f:
            for line in f:
                msg = json.loads(line)
                print(f"{msg["sender"]}: {msg["message"]}\n   {msg["timestamp"]}")


