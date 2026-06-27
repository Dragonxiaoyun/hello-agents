"""
my-fastapi-app — 晓云的 AI Agent 学习项目
Day 2: FastAPI + async/await + LLM 接入
"""
import os
from fastapi import FastAPI
from pydantic import BaseModel
from openai import AsyncOpenAI

app = FastAPI(
    title="晓云的 AI Agent API",
    description="从 FastAPI 到多 Agent 系统——学习实战项目",
    version="0.1.0",
)

client = AsyncOpenAI(
    api_key=os.getenv("LLM_API_KEY", "sk-your-key-here"),
    base_url=os.getenv("LLM_BASE_URL", "https://api.openai.com/v1"),
)


# ========== Models ==========
class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    user_input: str
    reply: str


# ========== Routes ==========
@app.get("/")
def root():
    return {"message": "Hello World, 晓云！今天也要加油 🔥"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """接入 LLM 的对话接口"""
    response = await client.chat.completions.create(
        model=os.getenv("LLM_MODEL_ID", "gpt-4o"),
        messages=[
            {
                "role": "system",
                "content": "你是一个友好的 AI 助手，回复简洁有力。",
            },
            {"role": "user", "content": request.message},
        ],
    )

    reply = response.choices[0].message.content
    return ChatResponse(user_input=request.message, reply=reply)
