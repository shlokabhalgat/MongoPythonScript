from pymongo import MongoClient

import mongomock


@mongomock.patch(servers=(('server.example.com', 27017),))
def kill_process(db_name, host, port, time_in_seconds):
    client = MongoClient(host=host, port=port)
    db = client.get_database(db_name)
    # print("Connected!", db_name)
    op_list = db.command({'currentOp': {'allUsers': True, 'localOps': True}, 'secs_running': {'$gte': time_in_seconds}}
                         )
    # print(op_list)
    for op in op_list["inprog"]:
        if op["type"] == "op":
            if op["op"] == "query":
                #      if op["command"]["query"] == collection_name:
                # print(op["opid"], op["command"]["insert"])
                # print(op["opid"], op["command"]["read"])
                # print('db.command({"killOp": 1, "op": ' + str(op["opid"]) + '})')
                db.command({"killOp": 1, "op": op["opid"]})
                print('Killed process' +' '+ str(op["opid"]) + ' ' + ' with Operation Type: ' + op["op"])


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('db_name', help='This is the db name', type=str)
    parser.add_argument('host', help='This is the host name', type=str)
    parser.add_argument('port', help='This is the port name', type=int)
    parser.add_argument('time_in_seconds', help='This is the threshold time for any running query', type=int)
    args = parser.parse_args()
    kill_process(args.db_name, args.host, args.port, args.time_in_seconds)


if __name__ == '__main__':
    main()

    # db.command({'killOp': 1, 'op': query['opid']})
    # response = db.command("currentOp", {"secs_running": {"$gt": 5}})
    # print(op_list)
