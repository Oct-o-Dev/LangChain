from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables (make sure GROQ_API_KEY is in your .env file)
load_dotenv()

# Initialize the Groq Chat model
# Popular models: "mixtral-8x7b-32768", "llama3-8b-8192", "gemma-7b-it"
llm = ChatGroq(model_name="llama-3.1-8b-instant")

# Invoke the model with the prompt
# (Groq will also correct the typo "Chapital" just like OpenAI)
result = llm.invoke("What is the Chapital of India")

# The result from ChatGroq is an AIMessage object.
# To get the text content, you access the .content attribute.
print(result.content)