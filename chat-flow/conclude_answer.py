
from promptflow import tool


@tool
def return_answer(sql_answer: str, chat_answer) -> str:
    # if sql answer is not empty or null, return sql answer, otherwise return chat answer
    return sql_answer if sql_answer else chat_answer
