# Smart Study Assistant using LangGraph & LangChain

An AI-powered Smart Study Assistant built using **LangGraph**, **LangChain**, and **Python** that intelligently classifies user queries and routes them to specialized AI agents for accurate responses.

The assistant can handle:

- Theory-based questions
- Coding-related questions

---

# Features

- Intelligent query classification
- Graph-based workflow orchestration using LangGraph
- Specialized Theory and Coding agents
- Shared memory state management
- Prompt engineering support
- Modular architecture

---

# Graph Architecture

```text
                User Query
                     |
              Classifier Node
               /            \
              /              \
      Theory Agent        Coding Agent
            |                  |
         Response           Response
```

---

# Workflow

1. User enters a question
2. Classifier node identifies question type
3. Query is routed to:
   - Theory Node
   - Coding Node
4. Final answer is returned to the user

---

# Tech Stack

- Python
- LangGraph
- LangChain
- Groq
- Prompt Engineering

---

# Project Structure

```text
LangGraph-Smart-Study-Assistant/
│
├── app/
│   ├── state.py
│   ├── prompts.py
│   ├── nodes.py
│   └── graph.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# File Description

## state.py
Defines shared memory state across nodes.

```python
state = {
    "question": "",
    "question_type": "",
    "answer": ""
}
```

---

## prompts.py
Stores all prompts separately for cleaner code and easier prompt engineering.

Example:
```python
CLASSIFIER_PROMPT
THEORY_PROMPT
CODE_PROMPT
```

---

## nodes.py
Contains all AI node logic.

### Nodes
- `classifier_node()`
- `theory_node()`
- `code_node()`

---

## graph.py
Handles:
- Node creation
- Edge creation
- Routing logic
- Graph compilation
- Workflow orchestration

---

## main.py
Handles:
- User input
- Graph invocation
- Final response display

Methods used:
```python
.compile()
.invoke()
```

---

# Example Queries

## Theory Question

```python
What is LangGraph?
```

## Coding Question

```python
Write Python code for Bubble Sort
```

---

