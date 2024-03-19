from utills.load_model_by_tokenizer import Tokenizer
from testcases.test_case_10_multifunctions import run_test_without_system_message


model = "mistralai/Mistral-7B-Instruct-v0.2"


messages, result=run_test_without_system_message(
        Tokenizer( model = model )
    )

print(messages)
print(result)