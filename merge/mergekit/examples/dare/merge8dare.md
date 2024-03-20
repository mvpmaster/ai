
# merge 8 models = weight 0.14 - 0.15

```
models:
  - model: mistralai/Mistral-7B-Instruct-v0.2
    # No parameters necessary for base model
  - model: mvpmaster/MistralDpoPearl-7b-slerp
    parameters:
      density: 0.4
      weight: 0.14
  - model: Locutusque/NeuralHyperion-2.0-Mistral-7B
    parameters:
      density: 0.4
      weight: 0.14
  - model: SanjiWatsuki/Kunoichi-DPO-v2-7B
    parameters:
      density: 0.4
      weight: 0.14
  - model: mvpmaster/NeuralMaths-lafted-7b-slerp
    parameters:
      density: 0.4
      weight: 0.14
  - model: mvpmaster/NeuralDareDMistralPro-slerp
    parameters:
      density: 0.4
      weight: 0.14
  - model: mvpmaster/kellemar-KrishnaHercules-0.1-slerp
    parameters:
      density: 0.4
      weight: 0.14
  - model: mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
    parameters:
      density: 0.4
      weight: 0.14
merge_method: dare_ties
base_model: mistralai/Mistral-7B-Instruct-v0.2
parameters:
  int8_mask: true
dtype: bfloat16
```