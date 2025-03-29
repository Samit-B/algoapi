from fastapi import APIRouter, HTTPException,FastAPI, Query
from typing import List, Dict, Any
from app.domain.projectApis.project_service_interfaces import ProjectServiceInterface
from app.domain.projectApis.project_service_mongo_implementation import ProjectServiceMongoImplementation

app = FastAPI()
projectApiRouter = APIRouter()
project_service = ProjectServiceMongoImplementation()

# -------------------------------
# 📌 Get All Collection Names
# -------------------------------
 
@projectApiRouter.get("/projects")
async def get_projects(projectIds: str = None):
    return await project_service.GetProjects(projectIds)

@projectApiRouter.post("/projects")
async def create_project(project_data: Dict):
    return await project_service.CreateProject(project_data)

@projectApiRouter.get("/projects/programs")
async def get_projects_by_program(programIds: str):
    return await project_service.GetProjectsByProgram(programIds)

@projectApiRouter.get("/projects/portfolios")
async def get_projects_by_portfolio(portfolioIds: str):
    return await project_service.GetProjectsByPortfolio(portfolioIds)
