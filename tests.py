import unittest

import pymongo

from main import kill_process

import mongomock



def test_kill_process():
    client = pymongo.MongoClient('server.example.com')
    db_name = client.get_database('admin')
    assert kill_process("db_name", "host", "port", "collection_name", "time_in_seconds")

