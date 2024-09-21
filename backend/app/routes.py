# app/routes.py
from fastapi import APIRouter, HTTPException
from .models import Conversation, QueryResponse
from .schemas import ConversationCreate, ConversationUpdate
from .database import init_db
from .utils import save_audit  # Import the save_audit function
import openai
import os

router = APIRouter()

# Set your OpenAI API key




@router.post("/conversations/", response_model=Conversation)
async def create_conversation(conversation: ConversationCreate):
    new_conversation = Conversation(history=[])
    await new_conversation.insert()
    return new_conversation

@router.get("/conversations/{conversation_id}", response_model=Conversation)
async def read_conversation(conversation_id: str):
    conversation = await Conversation.get(conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    return conversation

@router.put("/conversations/{conversation_id}", response_model=Conversation)
async def update_conversation(conversation_id: str, update: ConversationUpdate):
    conversation = await Conversation.get(conversation_id)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    conversation.history.append(QueryResponse(**update.dict()))
    await conversation.save()
    return conversation

@router.delete("/conversations/{conversation_id}")
async def delete_conversation(conversation_id: str):
    print("*************^^^^*****************")
    conversation = await Conversation.get(conversation_id)
    print("*************^^^^*****************")
    print(openai.api_key)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    await conversation.delete()
    return {"detail": "Conversation deleted"}

@router.post("/conversations/{conversation_id}/prompt")
async def send_prompt(conversation_id: str, prompt: str):
    conversation = await Conversation.get(conversation_id)
    print("*************^^^^*****************")
    print(openai.api_key)
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    # Construct the full conversation history
    messages = [{"role": "user", "content": h.query} for h in conversation.history]
    messages.append({"role": "user", "content": prompt})
    
    try:
        # Call the OpenAI API using the new method
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        answer = response['choices'][0]['message']['content']
        
        # Update the conversation history
        conversation.history.append(QueryResponse(query=prompt, response=answer))
        await conversation.save()

        # Store the anonymized query/response for auditing
        # (assume a function save_audit exists to handle this)
        save_audit(prompt, answer)

        return {"response": answer}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
