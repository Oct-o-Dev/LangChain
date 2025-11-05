from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq  # Changed from OpenAI to Groq
from dotenv import load_dotenv

load_dotenv()

# Initialize the Groq model
# Note: "llama-3.1-8b-instant" is a fast, capable model on Groq
# Temperature 0 is often the default, but we can set it explicitly if needed.
model = ChatGroq(model_name="llama-3.1-8b-instant", temperature=0)

# The message list works exactly the same way
messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell Me about Langchain"),
]

# The invoke method is the same
result = model.invoke(messages)

# Appending the AIMessage is also the same
messages.append(AIMessage(content=result.content))

# Print the full conversation history
print(messages)