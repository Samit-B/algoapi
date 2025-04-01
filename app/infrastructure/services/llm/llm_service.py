# import groq
# import openai
# from openai import OpenAI


# # Define LLM calling functions
# def call_deepseek(userChatQuery, chat_history):
#     """Call DeepSeek LLM"""
#     return f"DeepSeek Response for: {userChatQuery}"


# def call_gemini(userChatQuery, chat_history):
#     """Call Gemini LLM"""
#     return f"Gemini Response for: {userChatQuery}"


# def call_openai(userChatQuery, chat_history):
#     client = openai.OpenAI(api_key=OPENAI_API_KEY)

#     response = client.chat.completions.create(
#         model="GPT-4o mini Realtime",  # Adjust model as needed
#         messages=[{"role": "system", "content": "You are a helpful assistant."}]
#         + [{"role": "user", "content": msg} for msg in chat_history]
#         + [{"role": "user", "content": userChatQuery}],
#         temperature=0.7,
#     )

#     return response.choices[0].message.content


# def call_openrouter(user_query, chat_history):
#     client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=OPENROUTER_API_KEY)
#     response = client.chat.completions.create(
#         extra_headers={
#             "HTTP-Referer": "https://yourwebsite.com",
#             "X-Title": "YourSiteName",
#         },
#         model="mistralai/mistral-small-24b-instruct-2501:free",
#         messages=[
#             {"role": "system", "content": "You are an AI assistant."},
#             {"role": "user", "content": user_query},
#             {"role": "user", "content": chat_history},
#         ],
#     )
#     return response.choices[0].message.content


# def call_groq(userChatQuery, chat_history):
#     """Call Groq LLM"""
#     client = groq.Client(api_key=GROQ_API_KEY)
#     response = client.chat.completions.create(
#         model="mixtral-8x7b-32768",
#         messages=[
#             {
#                 "role": "system",
#                 "content": "You are an AI assistant providing general advice.",
#             },
#             {"role": "user", "content": userChatQuery},
#             {"role": "user", "content": chat_history},
#         ],
#         temperature=0.7,
#     )
#     return response.choices[0].message.content


# # LLM Mapping Dictionary
# LLM_MAPPING = {
#     "deepseek": call_deepseek,
#     "gemini": call_gemini,
#     "openai": call_openai,
#     "groq": call_groq,
#     "openrouter": call_openrouter,
# }


# def get_llm_response(selected_llm, userChatQuery, chat_history):
#     """Calls the correct LLM based on decision"""
#     llm_function = LLM_MAPPING.get(selected_llm.lower(), call_groq)  # Default to OpenAI
#     return llm_function(userChatQuery, chat_history)
