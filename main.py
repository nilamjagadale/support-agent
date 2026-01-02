from fastapi import FastAPI
import os 
from dotenv import load_dotenv

from models import TicketCreate, Ticket
from services import AIService

load_dotenv()

#if os.getenv()
aiservice = AIService()
tickets_db=[]

app = FastAPI(title = "AI APP")

@app.get("/health") 
def health():
    return {"msg":"Backend is running"}

@app.post("/tickets")
def tickets(ticket:Ticket):
    tickets_id = len(tickets_db)+1

    prompt=f"""
    you are the support agent ,given a problem by user you should answer it politely,clearly,
    consistly.

    user query:
    title: {ticket.title}
    description : {ticket.description}
    """
    

    response=aiservice.generate_reply(prompt)
    new_ticket=Ticket(
       title =ticket.title,
       description=ticket.description,
       id=tickets_id,
       ai_reply=response)
    tickets_db.append(new_ticket)
    return{
        "msg":"Ticket creted succesfully ",
        "ticket":new_ticket

    }
@app.get("/tickets")
def tickets():
    return tickets_db


