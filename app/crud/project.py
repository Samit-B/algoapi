from fastapi import HTTPException
from bson import ObjectId
from app.infrastructure.db.mongo_db import db
from typing import Dict, Any, List
from motor.motor_asyncio import AsyncIOMotorDatabase


# ✅ Get all collections
async def get_all_collections() -> Dict[str, List[str]]:
    collections = await db.list_collection_names()
    return {"collections": collections}

# ✅ Get all documents from a collection
async def get_collection_data(collection_name: str) -> List[Dict[str, Any]]:
    collection = db[collection_name]
    documents = await collection.find().to_list(length=None)  # Fetch all documents as a list

    def convert_objectid(doc):
        """ Recursively converts ObjectId to string in nested dictionaries and lists """
        if isinstance(doc, dict):
            return {k: convert_objectid(v) for k, v in doc.items()}
        elif isinstance(doc, list):
            return [convert_objectid(i) for i in doc]
        elif isinstance(doc, ObjectId):
            return str(doc)
        return doc

    return [convert_objectid(doc) for doc in documents]  # Convert all ObjectId occurrences

# ✅ Get a document by ID
async def get_record_by_id(collection_name: str, document_id: str) -> Dict[str, Any]:
    collection = db[collection_name]

    try:
        object_id = ObjectId(document_id)  # Convert string ID to ObjectId
    except Exception:
        return {"error": "Invalid ObjectId format"}  # Handle invalid ObjectId input

    document = await collection.find_one({"_id": object_id})  # Find document by _id

    def convert_objectid(doc):
        """ Recursively converts ObjectId to string in nested dictionaries and lists """
        if isinstance(doc, dict):
            return {k: convert_objectid(v) for k, v in doc.items()}
        elif isinstance(doc, list):
            return [convert_objectid(i) for i in doc]
        elif isinstance(doc, ObjectId):
            return str(doc)
        return doc

    return convert_objectid(document) if document else None  # Convert and return document or None if not found

# ✅ Insert a new document
async def insert_data(collection_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    collection = db[collection_name]
    result = await collection.insert_one(data)
    data["_id"] = str(result.inserted_id)  # Convert `_id` to string
    return data





