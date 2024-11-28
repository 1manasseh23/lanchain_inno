class ReActPrompt:
    template = """
    Answer the question using the tools provided:
    
    Tools:
    {tools}
    
    Format:
    Question: {input}
    Thought: {thought}
    Action: {action}
    Action Input: {action_input}
    Observation: {observation}
    Final Answer: {final_answer}
    
    Begin!
    Question: {input}
    Thought:
    """
