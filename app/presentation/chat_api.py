from fastapi import FastAPI, APIRouter, Request
from app.application.orchestrator.use_cases import Orchestrator
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
chatRouter = APIRouter()

# Fetch Groq API Key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize Groq LLM
llm = ChatGroq(model="llama3-8b-8192", api_key=GROQ_API_KEY, temperature=0)

# Global memory storage (LangChain's Memory)
memory = {}


@chatRouter.get("/query")
async def query_handler(userChatQuery: str):

    # Process user query using Orchestrator
    orchestrator = Orchestrator(userChatQuery)
    response = await orchestrator.route_query()
    return {
        "response": response,
    }


app.include_router(chatRouter)
