from langchain.callbacks.base import BaseCallbackHandler

class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(self, serialized, prompts, **kwargs):
        print(f"LLM started with prompt: {prompts[0]}")
    
    def on_llm_end(self, response, **kwargs):
        print(f"LLM response: {response.generations[0][0].text}")
