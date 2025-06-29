from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent_logic import process_user_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat_endpoint(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    response = process_user_message(user_message)
    return {"response": response}
