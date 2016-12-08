import json

class IntermittentsDB:
    def __init__(self, db):
        self.intermittents = db


    def query(self, name):
        # In Python 3 filter() is lazy, so we build an array right here so that it can be jsonified
        return [x for x in filter(lambda i: name in i['title'], self.intermittents)]


    def add(self, name, number):
        for i in self.intermittents:
            if i['number'] == number:
                return
        self.intermittents.extend([{'title': name, 'number': number}])

    
    def remove(self, number):
        for idx, i in enumerate(self.intermittents):
            if i['number'] == number:
                self.intermittents.pop(idx)
                return


class AutoWriteDB(IntermittentsDB):
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            IntermittentsDB.__init__(self, json.loads(f.read()))

    def __enter__(self):
        return self

    def __exit__(self, etype, evalue, etrace):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.intermittents))
