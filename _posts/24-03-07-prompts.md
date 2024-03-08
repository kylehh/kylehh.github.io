---
title: Prompts 
mathjax: true
toc: true
categories:
  - Study 
tags:
  - LLM
---

## 1 Build evaluation
```python
def build_grader_prompt(answer, rubric):
    user_content = f"""You will be provided an answer that an assistant gave to a question, and a rubric that instructs you on what makes the answer correct or incorrect.
    
    Here is the answer that the assistant gave to the question.
    <answer>{answer}</answer>
    
    Here is the rubric on what makes the answer correct or incorrect.
    <rubric>{rubric}</rubric>
    
    An answer is correct if it entirely meets the rubric criteria, and is otherwise incorrect. =
    First, think through whether the answer is correct or incorrect based on the rubric inside <thinking></thinking> tags. Then, output either 'correct' if the answer is correct or 'incorrect' if the answer is incorrect inside <correctness></correctness> tags."""

    messages = [{'role': 'user', 'content': user_content}]
    return messages
```

## 2 Moderation by CoT
```python
cot_prompt = '''You are a content moderation expert tasked with categorizing user-generated text based on the following guidelines:

BLOCK CATEGORY:
- Content that is not related to rollercoasters, theme parks, or the amusement industry
- Explicit violence, hate speech, or illegal activities
- Spam, advertisements, or self-promotion

ALLOW CATEGORY:
- Discussions about rollercoaster designs, ride experiences, and park reviews
- Sharing news, rumors, or updates about new rollercoaster projects
- Respectful debates about the best rollercoasters, parks, or ride manufacturers
- Some mild profanity or crude language, as long as it is not directed at individuals

First, inside of <thinking> tags, identify any potentially concerning aspects of the post based on the guidelines below and consider whether those aspects are serious enough to block the post or not. Finally, classify this text as either ALLOW or BLOCK inside <output> tags. Return nothing else.

Given those instructions, here is the post to categorize:

<user_post>{user_post}</user_post>'''
```

## 3. JSON output
```python
client.messages.create(
    model=MODEL_NAME,
    max_tokens=1024,
    messages=[
        {
            "role": "user", 
            "content": "Give me a JSON dict with names of famous athletes & their sports."
        },
        {
            "role": "assistant",
            "content": "Here is the JSON requested:\n{"
        }
    ]
)
```

## 4. SQL Query
```python
prompt = f"""Here is the schema for a database:

{schema}

Given this schema, can you output a SQL query to answer the following question? Only output the SQL query and nothing else.

Question: {query}
"""
```