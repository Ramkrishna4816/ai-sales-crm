from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.leads import router as lead_router
from routes.ai import router as ai_router


app = FastAPI(title="AI Sales CRM API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Sales CRM API running"}

app.include_router(lead_router, prefix="/leads", tags=["Leads"])
app.include_router(ai_router, prefix="/ai", tags=["AI"])

