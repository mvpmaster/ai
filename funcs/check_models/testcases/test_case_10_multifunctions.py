

user_prompt = f""" check wheather in Chicago  ? and Can you please provide me stock price or Apple ? use tools, use original function names"""
max_output_tokens=512

tools_list = [
    {
        "type": "function",
        "function": {
            "name": "get_stock_price",
            "description": "Retrieve the latest closing price of a stock using its ticker symbol",
            "parameters": {
                "type": "object",
                "properties": {
                    "symbol": {
                        "type": "string",
                        "description": "The ticker symbol of the stock"
                    }
                },
                "required": ["symbol"]
            }
        }
    },

        {
        "type": "function",
        "function": {
            "name": "get_wheather",
            "description": "Retrive wheather of city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Provide city to get wheather"
                    }
                },
                "required": ["city"]
            }
        }
    },
]

from utills.complile_func_message import compile_function_message_without_system_message

messages_without_system_message=compile_function_message_without_system_message(
    user_prompt=user_prompt, 
    tools_list=tools_list
    )

def run_test_without_system_message(tokenizer, messages=None, max_tokens=None):
    result=tokenizer.execute_messages(
    messages=messages or messages_without_system_message,
    max_tokens=max_tokens or max_output_tokens
    )
    return messages_without_system_message, result