from google.appengine.ext import ndb
import json
from datetime import datetime, date, time


class JSONEncoder(json.JSONEncoder):

    def default(self, o):
        if isinstance(o, ndb.Key):
            o = ndb.Key.get(o)
        if isinstance(o, ndb.Model):
            return dict(ndb.Model.to_dict(o), **dict(id=o.key.id()))
        elif isinstance(o, (datetime, date, time)):
            return str(o)
        return json.JSONEncoder.default(self, o)