from ollama import chat




def create_response(instruction):
    stream = chat(
        model = "bugspred2", 
        # messages = [{ "role": "user", 
        #              'content': instruction}], 
        messages = instruction,
        stream = True
    )

    return stream