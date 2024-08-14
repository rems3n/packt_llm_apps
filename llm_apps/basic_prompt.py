import os
import openai

system_message = """
You are a Python expert who produces Python code as per the user's request.
===>START EXAMPLE
---User Query---
Give me a function to print a string of text.
---User Output---
Below you can find the described function:
```def my_print(text):
     return print(text)
```
<===END EXAMPLE
Choose the version of the function with lowest Big O complexity
"""
query = "generate a Python function to calculate the nth Fibonacci number"


openai.api_key = os.environ.get('OPENAI_API_KEY')
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": system_message},
        {"role": "user", "content": query},
    ]
)

print(response['choices'][0]['message']['content'])
