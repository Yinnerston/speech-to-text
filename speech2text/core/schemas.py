from ninja import Schema, Field


class ChatGPTSchema(Schema):
    text: str = Field(example="Text to be sent to the AI assistant")
