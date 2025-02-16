from fastapi import FastAPI, HTTPException
from backend.db import get_connection
from langchain_community.chat_models import ChatOpenAI # Instead of `from langchain.chat_models import ChatOpenAI`
from langchain.schema import AIMessage, HumanMessage

app = FastAPI()

# LangChain AI Model
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key="your_openai_api_key")

@app.get("/")
def read_root():
    return {"message": "Welcome to Co-Founder AI"}

# Store & Validate Idea
@app.post("/validate-idea/")
def validate_idea(data: dict):
    idea = data.get("idea", "").strip()
    if not idea:
        raise HTTPException(status_code=400, detail="Idea cannot be empty")
    
    # AI Validation using LangChain
    response = llm.predict(f"Validate this startup idea: {idea}")
    
    # Store in MySQL
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO startup_ideas (idea, validation) VALUES (%s, %s)", (idea, response))
        conn.commit()
    finally:
        conn.close()

    return {"idea": idea, "validation": response}

# Fetch All Ideas
@app.get("/get-ideas/")
def get_ideas():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM startup_ideas")
            ideas = cursor.fetchall()
    finally:
        conn.close()

    return {"ideas": ideas}

# AI-Powered Startup Advice
@app.get("/get-startup-advice/")
def get_startup_advice():
    response = llm.predict("Give me 3 startup tips for a solo founder")
    return {"advice": response.split("\n")}
