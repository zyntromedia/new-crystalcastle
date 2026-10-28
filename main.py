from agents.writer_agent import WriterAgent

# นี่คือ LLM Wrapper จริงที่คุณต้องเชื่อมกับ Provider ของ ZyntroAI
def real_llm_func(prompt: str) -> str:
    # return provider.generate(prompt)
    raise NotImplementedError("ต้องเชื่อมกับ LLM Provider จริง")


agent = WriterAgent(
    llm_func=real_llm_func,
    max_iterations=3
)

result = agent.run(
    prompt="เขียน Evergreen Note เกี่ยวกับ Observability for DevOps",
    context_notes=[
        "Observability = Metrics + Logs + Traces",
        "Repair Loop ต้องอาศัย Observability"
    ]
)

print(result.final_output)
