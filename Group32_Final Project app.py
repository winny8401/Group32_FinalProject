import openai
import gradio as gr

openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are an AI assistant specialised in psychological diagnosis in charge of classifying people personality into the Big 5 personality traits which are;  openess, neuroticism, etraversion, agreeableness and conscientiousness "},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-4", messages=messages,temperature=0.5,
        )

        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="PersoScan",
             description="Provide Personal CV description",
             theme="compact").launch(share=True)