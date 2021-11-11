import json
import os

from datetime import datetime

from Event import Event


class EventProvider:
    @staticmethod
    def load_events(filename):
        if not isinstance(filename, str):
            raise TypeError('filename must be of type str')
        if not filename.endswith('.json'):
            raise ValueError('invalid json file name')
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                return json.load(f, object_hook=EventProvider.__decode_event)
        else:
            return list()

    @staticmethod
    def __decode_event(dct):
        if 'IT event' in dct:
            return Event(dct['IT event'], dct['id'], dct['standard price'],
                         datetime.strptime(dct['event date'], '%Y-%m-%d').date())
        return dct
