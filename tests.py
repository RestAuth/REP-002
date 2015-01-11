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
