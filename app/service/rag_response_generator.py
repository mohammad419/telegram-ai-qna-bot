from config import *

def generate_rag_response(query):

    thread = openai_client.beta.threads.create()

    message = openai_client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=query
        )
    
    run = openai_client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=openai_assistant_id,
        instructions="Please address the user query."
        )
    
    if run.status == 'completed':
        messages = openai_client.beta.threads.messages.list(
            thread_id=thread.id
        )
        extract_ans = list(openai_client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))
        return extract_ans[0].content[0].text.value
    else:
        print(run.status)
