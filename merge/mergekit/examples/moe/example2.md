

```
base_model: mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
dtype: float16
gate_mode: cheap_embed
experts:
  - source_model: mvpmaster/pmmpk-EinstainMorcoro14KrishnaHercules-7b-slerp
    positive_prompts: ["You a helpful assistant in code and main question answering"]
  - source_model: mvpmaster/kellemar-KrishnaHercules-0.1-7b-slerp
    positive_prompts: ["You are assistant for geometry and creative answers."]
```