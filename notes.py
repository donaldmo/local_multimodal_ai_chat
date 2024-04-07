from langchain_community.llms import CTransformers

# llm = CTransformers(model="marella/gpt-2-ggml")
llm = CTransformers(model="./models/mistral-7b-instruct-v0.1.Q3_K_M.gguf")
# ./models/mistral-7b-instruct-v0.1.Q3_K_M.gguf

print(llm("AI is going to"))