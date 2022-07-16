import pymongo
from main import kill_process


def test_kill_process():
    client = pymongo.MongoClient('server.example.com')
    db = client.get_database('admin')
    # query = db.test.find( { $where: function() { return sleep(600) || true }}).pretty();
    assert kill_process(db, "host", "port", "time_in_seconds")
