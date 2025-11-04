from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
# Load environment variables (make sure HUGGINGFACEHUB_API_TOKEN is in your .env file)
load_dotenv()
# Initialize the HuggingFace Chat model
# Popular models: "gpt-4o-mini", "gpt-4o", "mistral-7b-instruct-v0.1", "gemma-7b-it"


llm = ChatHuggingFace(model_name="gpt-4o-mini")