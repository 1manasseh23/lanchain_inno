
from typing import List, Union
from langchain.schema import AgentAction, AgentFinish
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.agents import Tool
from langchain.output_parsers import ReActSingleInputOutputParser

class ReActAgent:
    def __init__(self, tools: List[Tool], prompt: str):
        self.tools = tools
        self.prompt = PromptTemplate(template=prompt)
        self.llm = OpenAI(model="gpt-4", temperature=0)

    def process_query(self, query: str) -> str:
        intermediate_steps = []
        while True:
            response = self._run_agent(query, intermediate_steps)
            if isinstance(response, AgentFinish):
                return response.return_values
            elif isinstance(response, AgentAction):
                tool = self._find_tool(response.tool)
                observation = tool.func(response.tool_input)
                intermediate_steps.append((response, observation))
    
    def _run_agent(self, query: str, intermediate_steps: list) -> Union[AgentAction, AgentFinish]:
        input_data = {"input": query, "intermediate_steps": intermediate_steps}
        agent = self.prompt | self.llm | ReActSingleInputOutputParser()
        return agent.invoke(input_data)
    
    def _find_tool(self, tool_name: str):
        for tool in self.tools:
            if tool.name == tool_name:
                return tool
        raise ValueError(f"Tool {tool_name} not found.")
