from fastapi.encoders import jsonable_encoder
import json
import time

"""
WARNING: This code will be deprecated! Please using avoid!
"""


class Util():
    def __init__(self):
        self.start_time = time.time()

    # encode success as json
    def success(message):
        return jsonable_encoder({
            "success": {
                "time": int(time.time()),
                "message": message
            }
        })

    # encode error as json
    def error(code, message):
        return jsonable_encoder({
            "error": {
                "time": int(time.time()),
                "code": code,
                "message": message
            }
        })

    # encode text ocmpletion as json
    def completion(text):
        return jsonable_encoder({
            "completion": {
                "text": text,
                "time": int(time.time())
            }
        })

    # Logs output to the console with timestamp from self.start_time
    # Format: [timestamp] module: message
    def log(self, module, message):
        timestamp = time.time() - self.start_time
        print('[{:.4f}] {}: {}'.format(timestamp, module, message))

    # Returns formatted timestamp date with hour, minutes, and seconds as string
    def timestamp_date(self):
        timestamp = time.time() - self.start_time
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))