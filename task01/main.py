


from langgraph.graph import StateGraph, START, END

def hello(state):
    return {"message": "Hello, LangGraph!"}

builder = StateGraph(dict)

builder.add_node("hello", hello)
builder.add_edge(START, "hello")
builder.add_edge("hello", END)

graph = builder.compile()

result = graph.invoke({})
print(result)
