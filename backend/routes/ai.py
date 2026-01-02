from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class FollowUpRequest(BaseModel):
    name: str
    company: str | None = None
    status: str
    last_contacted: str | None = None
    tone: str = "friendly"   # friendly | formal | short

@router.post("/followup")
def generate_followup(data: FollowUpRequest):
    """
    This is an AI-style follow-up generator.
    Later, we will plug Antigravity here.
    """

    if data.tone == "formal":
        message = (
            f"Dear {data.name},\n\n"
            f"I hope this message finds you well. "
            f"I am following up regarding our previous discussion. "
            f"Please let me know a convenient time to continue.\n\n"
            f"Best regards"
        )

    elif data.tone == "short":
        message = (
            f"Hi {data.name}, just checking in on our last conversation. "
            f"Let me know your thoughts."
        )

    else:  # friendly
        message = (
            f"Hi {data.name}! 😊\n"
            f"Just wanted to follow up and see if you had any questions. "
            f"Happy to continue the conversation anytime!"
        )

    return {
        "follow_up_message": message,
        "tone": data.tone
    }
