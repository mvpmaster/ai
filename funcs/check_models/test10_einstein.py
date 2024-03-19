

from utills.load_model_by_tokenizer import Tokenizer
from testcases.test_case_10_multifunctions import run_test_without_system_message


# mytokenizer = Tokenizer(
#     model="Weyaxi/Einstein-v4-7B",
#     )

# result=mytokenizer.execute_messages(
#     messages=messages_without_system_message,
#     max_tokens=max_tokens
#     )



messages, result=run_test_without_system_message(
        Tokenizer( model="Weyaxi/Einstein-v4-7B" )
    )

print(messages)
print(result)