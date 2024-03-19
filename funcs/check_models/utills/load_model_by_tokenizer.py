

from transformers import AutoModelForCausalLM, AutoTokenizer


class Tokenizer():
    def __init__(   self,
                    model="Qwen/Qwen1.5-7B-Chat",
                    device="cuda") -> None:
        self.device = device
        self.model = AutoModelForCausalLM.from_pretrained(
            #"Qwen/Qwen1.5-7B-Chat",
            #"Locutusque/NeuralHyperion-2.0-Mistral-7B",
            model,
            torch_dtype="auto",
            device_map="auto"
        )
        self.tokenizer = AutoTokenizer.from_pretrained(model)


    def execute_messages(self, messages, max_tokens=512):
        text = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )
        model_inputs = self.tokenizer([text], return_tensors="pt").to(self.device)

        generated_ids = self.model.generate(
            model_inputs.input_ids,
            max_new_tokens=max_tokens # 512
        )
        generated_ids = [
            output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
        ]

        response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return response

# print(messages)
# print(response)
