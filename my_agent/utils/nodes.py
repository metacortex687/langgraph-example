from functools import lru_cache
from langchain_xai import ChatXAI
from my_agent.utils.tools import tools
from langgraph.prebuilt import ToolNode


@lru_cache(maxsize=4)
def _get_model(model_name: str):
    if model_name == "grok":
        model = ChatXAI(temperature=0, model_name="grok-2-latest")
    else:
        raise ValueError(f"Unsupported model type: {model_name}")

    model = model.bind_tools(tools)
    return model

# Define the function that determines whether to continue or not
def should_continue(state):
    messages = state["messages"]
    last_message = messages[-1]
    # If there are no tool calls, then we finish
    if not last_message.tool_calls:
        return "end"
    # Otherwise if there is, we continue
    else:
        return "continue"


system_prompt = """Be a helpful assistant"""

# Define the function that calls the model
def call_model(state, config):
    print("DEBUG STATE:", state)
    print("DEBUG CONFIG:", config)
    messages = state["messages"]
    messages = [{"role": "system", "content": system_prompt}] + messages
    # Всегда используем "grok" независимо от config
    model_name = "grok"
    print("DEBUG MODEL_NAME:", model_name)
    model = _get_model(model_name)
    response = model.invoke(messages)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}

# Define the function to execute tools
tool_node = ToolNode(tools)