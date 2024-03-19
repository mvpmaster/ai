import json

from utills.function_calling_example import function_calling_example

remove_pydantic_to_json = """, if pydantic transform to json and nothing else, answer formated json (no write pydantic in json, only valid json), only one aswer"""


# opensource 
copybara_fix_resoning_off_instruction=""
addon_message=[{"role": "user", "content": f"""Please output next messages valid JSON format, without any COMMENTS, without any CODE, only {{...}}{remove_pydantic_to_json}"""}]


def compile_function_message_without_system_message(user_prompt, tools_list):
    messages = [
        #{"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_prompt}
    ]
    #messages=addon_message + messages
    addon_message[0]['content']+="\n\n"+messages[0]['content']



    tools_=json.dumps(tools_list)

    messages=[{"role": "user", "content":""}]
    messages[0]['content']= f"""Please output valid JSON same format, without any comments (exacly in this output format, with changing function, no <</SYS>> generations, max token count of answer: 2048): {function_calling_example}"""+ \
    f"""\n\nfunction execute description:

    ```
    tools={tools_}{copybara_fix_resoning_off_instruction}
    ```"""+ \
    "\n\n"+addon_message[0]['content']+\
    "\n\none json answer"

    return messages