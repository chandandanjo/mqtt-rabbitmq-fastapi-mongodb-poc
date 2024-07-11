from pymongo import MongoClient


class MongoDBClient:
    # For the sake of simplicity I've used only insert_one and aggregate methods

    def __init__(self, uri, db_name, collection_name):
        self._client = MongoClient(uri)
        self._db = self._client[db_name]
        self._collection = self._db[collection_name]
    
    def insert(self, data):
        try:
            self._collection.insert_one(data)
        except Exception as e:
            print(f"Error inserting data: {e}")
    
    def aggregate(self, pipeline):
        return self._collection.aggregate(pipeline)
    


def get_status_count(start_time, end_time, mongo_client):
    # match the data between start_time and end_time inclusive, group by status and count them and finally project the results
    pipeline = [
        {
            '$match': {
                'timestamp': {
                    '$gte': start_time, 
                    '$lte': end_time
                }
            }
        }, {
            '$group': {
                '_id': '$status', 
                'count': {
                    '$sum': 1
                }
            }
        }, {
            '$project': {
                '_id': 0, 
                'status': '$_id', 
                'count': 1
            }
        }
    ]

    result = list(mongo_client.aggregate(pipeline))
    return result