import json
import os
import unittest

import jsonschema

with open('rep-002.json') as fp:
    schema = json.load(fp)


class TestTestdata(unittest.TestCase):
    def test_examples(self):
        for dirpath, dirnames, filenames in os.walk(os.path.join('testdata', 'examples')):
            for filename in filenames:
                path = os.path.join(dirpath, filename)
                with open(path) as fp:
                    data = json.load(fp)

                jsonschema.validate(data, schema)

    def test_success(self):
        for dirpath, dirnames, filenames in os.walk(os.path.join('testdata', 'success')):
            for filename in [f for f in filenames if f.endswith('.json')]:
                path = os.path.join(dirpath, filename)
                with open(path) as fp:
                    data = json.load(fp)

                jsonschema.validate(data, schema)

    def test_error(self):
        for dirpath, dirnames, filenames in os.walk(os.path.join('testdata', 'error')):
            for filename in [f for f in filenames if f.endswith('.json')]:
                print(filename)
                path = os.path.join(dirpath, filename)
                with open(path) as fp:
                    data = json.load(fp)

                jsonschema.validate(data, schema)
