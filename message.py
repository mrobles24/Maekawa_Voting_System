import json

class Message(object):
    def __init__(self, msg_type=None, src=None, dest=None, ts=None, data=None):
        self.msg_type = msg_type
        self.src = src
        self.dest = dest
        self.ts = ts
        self.data = data

    def __json__(self):
        return dict(msg_type=self.msg_type, 
                    src=self.src, 
                    dest=self.dest, 
                    ts=self.ts, 
                    data=self.data)

    def set_type(self, msg_type):
        self.msg_type = msg_type

    def set_src(self, src):
        self.src = src

    def set_dest(self, dest):
        self.dest = dest

    def set_ts(self, ts):
        self.ts = ts

    def set_data(self, data):
        self.data = data

    def to_json(self):
        obj_dict = dict()
        obj_dict['msg_type'] = self.msg_type
        obj_dict['src'] = self.src
        obj_dict['dest'] = self.dest
        obj_dict['ts'] = self.ts
        obj_dict['data'] = self.data
        return json.dumps(obj_dict)
