# repositories/advanced_search_repository.py
from typing import Dict, List
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']

async def search_by_criteria(collection_name: str, criteria: Dict) -> List[Dict]:
    collection: Collection = db[collection_name]
    results = collection.find(criteria)
    return list(results)