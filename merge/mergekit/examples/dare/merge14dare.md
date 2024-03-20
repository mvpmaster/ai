# https://huggingface.co/EmbeddedLLM/Mistral-7B-Merge-14-v0
# 14 models = weight: 0.07 - 0.08

```
models:
  - model: mistralai/Mistral-7B-v0.1
    # no parameters necessary for base model
  - model: ehartford/dolphin-2.2.1-mistral-7b
    parameters:
      weight: 0.08
      density: 0.4
  - model: SciPhi/SciPhi-Mistral-7B-32k
    parameters:
      weight: 0.08
      density: 0.4
  - model: ehartford/samantha-1.2-mistral-7b
    parameters:
      weight: 0.08
      density: 0.4
  - model: Arc53/docsgpt-7b-mistral
    parameters:
      weight: 0.08
      density: 0.4
  - model: berkeley-nest/Starling-LM-7B-alpha
    parameters:
      weight: 0.08
      density: 0.4
  - model: Q-bert/MetaMath-Cybertron-Starling
    parameters:
      weight: 0.08
      density: 0.4
  - model: Open-Orca/Mistral-7B-OpenOrca
    parameters:
      weight: 0.08
      density: 0.4
  - model: v1olet/v1olet_marcoroni-go-bruins-merge-7B
    parameters:
      weight: 0.08
      density: 0.4
  - model: beowolx/MistralHermes-CodePro-7B-v1
    parameters:
      weight: 0.08
      density: 0.4
  - model: TIGER-Lab/MAmmoTH-7B-Mistral
    parameters:
      weight: 0.08
      density: 0.4
  - model: teknium/OpenHermes-2.5-Mistral-7B
    parameters:
      weight: 0.08
      density: 0.4
  - model: Weyaxi/OpenHermes-2.5-neural-chat-v3-3-Slerp
    parameters:
      weight: 0.08
      density: 0.4
  - model: mlabonne/NeuralHermes-2.5-Mistral-7B
    parameters:
      weight: 0.08
      density: 0.4
  - model: mistralai/Mistral-7B-Instruct-v0.2
    parameters:
      weight: 0.08
      density: 0.5
merge_method: dare_ties
base_model: mistralai/Mistral-7B-v0.1
parameters:
  int8_mask: true
dtype: bfloat16

```