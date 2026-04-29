# Current setup per dm session:
# filename = f"{userA}?{userB}" if userA < userB else f"{userB}?{userA}"
# logger = chat_logs_setup(filename)
# Current way to send message:
# logger.info({"sender": sender, "message": msg})


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
            "timestamp": datetime.datetime.fromtimestamp(record.created).isoformat(),
            "sender": msg_data["sender"],
            "message": msg_data["message"]
        }

        return json.dumps(entry)

def chat_logs_setup(filename, level = logging.INFO):
    # Assign ChatJsonFormatter class object to formatter
    formatter = ChatJSONFormatter()

    # File Handler
    handler = logging.FileHandler(get_path(filename))
    handler.setFormatter(formatter)

    # Logger configuration
    logger = logging.getLogger(f"ChatLogs_{filename}")
    logger.setLevel(level)
    logger.addHandler(handler)

    # No root logger
    logger.propagate = False

    return logger
    
def get_path(filename):
    # Set directory path
    base_dir = Path(__file__).parent.resolve() / "Logs"

    # Make directory if it doesn't exit
    base_dir.mkdir(exist_ok = True)

    # Resolve the path
    file_path = (base_dir / filename).resolve()

    # Path sanitizer for traversal check
    if not file_path.is_relative_to(base_dir):
        raise ValueError("Path traversal detected.")
    else:
        return str(file_path)
