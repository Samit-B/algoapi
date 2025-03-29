from abc import ABC, abstractmethod
from typing import Dict, List, Optional
from bson import ObjectId
from app.infrastructure.db.mongo_db import db
 
from app.domain.projectApis.project_service_mongo_implementation import ProjectServiceInterface

class ProgramServiceMongoImplementation(ProjectServiceInterface):
    async def GetProjects(self, projectIds: Optional[str] = None) -> List[Dict]:
        """
        Implementation of GetProjects to fetch projects from MongoDB.
        If projectIds is None, fetch all projects.
        """
        collection = db["projects"]  # Access the 'projects' collection

        if projectIds:
            # Convert comma-separated IDs into a list of ObjectIds
            project_ids_list = [ObjectId(pid) for pid in projectIds.split(",")]
            # Query MongoDB for projects with matching IDs
            cursor = collection.find({"_id": {"$in": project_ids_list}})
        else:
            # Query MongoDB for all projects
            cursor = collection.find()

        # Convert the cursor to a list of documents
        projects = await cursor.to_list(length=None)

        # Convert ObjectId to string for each project
        for project in projects:
            project["_id"] = str(project["_id"])

        return projects

async def CreateProject(self, project_data: Dict) -> Dict:
        """
        Implementation of CreateProject to insert a new project into MongoDB.
        """
        collection = db["projects"]
        result = await collection.insert_one(project_data)
        project_data["_id"] = str(result.inserted_id)  # Convert ObjectId to string
        return 

async def GetProjectsByProgram(self, programIds: list) -> list:
        """
        Fetch projects associated with specific program IDs.
        """
        collection = db["programs"]
        program_ids_list = [ObjectId(pid) for pid in programIds]
        cursor = collection.find({"programId": {"$in": program_ids_list}})
        projects = await cursor.to_list(length=None)
        for project in projects:
            project["_id"] = str(project["_id"])
        return projects


async def GetProjectsByPortfolio(self, portfolioIds: list) -> list:
    """
    Fetch projects associated with specific portfolio IDs.
    """
    collection = db["prrtfolios"]
    portfolio_ids_list = [ObjectId(pid) for pid in portfolioIds]
    cursor = collection.find({"portfolioId": {"$in": portfolio_ids_list}})
    projects = await cursor.to_list(length=None)
    for project in projects:
        project["_id"] = str(project["_id"])
    return projects


