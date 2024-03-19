from utills.load_model_by_tokenizer import Tokenizer
from testcases.test_case_10_multifunctions import run_test_without_system_message


model = "NousResearch/Hermes-2-Pro-Mistral-7B"


messages, result=run_test_without_system_message(
        Tokenizer( model = model )
    )

print(messages)
print(result)