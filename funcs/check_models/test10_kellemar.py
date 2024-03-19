from utills.load_model_by_tokenizer import Tokenizer
from testcases.test_case_10_multifunctions import run_test_without_system_message


model = "decruz07/kellemar-DPO-Orca-Distilled-7B-SLERP"


messages, result=run_test_without_system_message(
        Tokenizer( model = model )
    )

print(messages)
print(result)