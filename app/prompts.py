CLASSIFIER_PROMPT = """ 
You are the classifier node.Classify the followig text into the one of the categories THEORY or CODE
Return only
-THEORY
or
Return only
-CODE
"""

THEORY_PROMPT = """
you are the Theory node.Answer the following text in the simple manner with related examples 
Question: {question}
"""

CODE_PROMPT = """
You are the code node. Provide the code of implementation for following task
Question :{question}"""