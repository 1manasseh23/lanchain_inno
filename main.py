from dotenv import load_dotenv
from agents.react_agent import ReActAgent
from tools.calculator import multiply_tool
from tools.text_processing import get_text_length
from prompts.react_prompt import ReActPrompt
from langchain.agents import Tool

load_dotenv()  # Load environment variables

if __name__ == "__main__":
    print("Starting the ReAct Chatbot...")
    
    # Define tools
    tools = [
        Tool(name="multiply_tool", func=multiply_tool, description="Multiply two numbers."),
        Tool(name="get_text_length", func=get_text_length, description="Get text length.")
    ]
    
    # Load the ReAct agent with tools and prompt
    agent = ReActAgent(tools=tools, prompt=ReActPrompt.template)
    
    # Example query
    query = "What is the length of the word 'LangChain'?"
    response = agent.process_query(query)
    print(f"Chatbot Response: {response}")
