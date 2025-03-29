from langchain_community.embeddings import OpenAIEmbeddings  # Updated import
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI  # Use this instead of openai.ChatCompletion

class MemoryService:
    def __init__(self):
        # Ensure to pass a valid LLM instance
        self.memory = ConversationSummaryMemory(
            llm=ChatOpenAI(model_name="gpt-4"),  # Updated LLM usage
            return_messages=True
        )
    
    def save_chat(self, user_query, response):
        self.memory.save_context(
            {"input": user_query},
            {"output": response}
        )

    def get_chat_history(self):
        return self.memory.load_memory_variables({})
