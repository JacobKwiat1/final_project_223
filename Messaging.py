# Current setup per dm session:
# create instance of DM_Session ( example: dm = DM_Session(sender_username, receiver_username) )
# How to send messages:
# dm.send(message)
# How to print dm log:
# dm.print_msgs()


import logging
import datetime
import json
import os
    
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
    chat_logger = None

    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.filename = f"{sender}-{receiver}.txt" if sender < receiver else f"{receiver}-{sender}.txt"

        if f"ChatLogs_{self.filename}" not in logging.root.manager.loggerDict.keys():
            DM_Session.chat_logger = self.chat_logs_setup()
        
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
        folder = "Logs"

        # Make folder if it does not exist
        os.makedirs(folder, exist_ok=True)

        # Resolve the path
        file_path = os.path.join(folder, self.filename)

        return file_path
        
    def send(self, msg):
        DM_Session.chat_logger.info({"sender": self.sender, "receiver": self.receiver, "message": msg})

    def print_msgs(self):
        msg = {}

        print(f"\n---Messages with {self.receiver}---")
        with open(self.get_path(), "r") as f:
            for line in f:
                msg = json.loads(line)
                print(f"{msg["sender"]}: {msg["message"]}\n   {msg["timestamp"]}")

