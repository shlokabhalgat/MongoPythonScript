# MongoPythonScript
Script to kill all long running queries which exceed a certain threshold of time as given by user. The script works on admin database as it has the db commands permissions required for killing the processes.

## To run this script-

`python main.py (1) (2) (3) (4)`

Give the command line parameters in this order:
- Database name (1)
- Host name (2)
- Port name(3)
- Threshold time in seconds (4)

## To verify the termination of the query-

Query the collection adding the sleep function

`db.collection_name.find( { $where: function() { return sleep(600) || true }}).pretty();`

