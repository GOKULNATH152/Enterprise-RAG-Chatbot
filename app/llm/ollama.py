from langchain_ollama import ChatOllama


class OllamaLLM:

    def __init__(self):

        self.model = ChatOllama(
            model="llama3.1",
            temperature=0
        )


    def generate(self, prompt):

        response = self.model.invoke(prompt)

        return response.content