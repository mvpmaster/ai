
# https://github.com/AIAnytime/Medical-Mixture-of-Experts-LLM

```
base_model: BioMistral/BioMistral-7B
dtype: float16
gate_mode: cheap_embed
experts:
  - source_model: epfl-llm/meditron-7b
    positive_prompts: ["You are a helpful medical assistant."]
  - source_model: medalpaca/medalpaca-7b
    positive_prompts: ["You are assistant for medical question answering."]
```