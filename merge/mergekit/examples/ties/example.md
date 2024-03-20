models:
  - model: Kukedlc/Neural4gsm8k
    parameters:
      density: [1, 0.7, 0.1] # density gradient
      weight: 1.0
  - model: PetroGPT/WestSeverus-7B-DPO
    parameters:
      density: 0.5
      weight: [0, 0.3, 0.7, 1] # weight gradient
  - model: samir-fama/FernandoGPT-v1
    parameters:
      density: 0.33
      weight:
        - filter: mlp
          value: 0.5
        - value: 0
merge_method: ties
base_model: liminerity/M7-7b
parameters:
  normalize: true
  int8_mask: true
dtype: bfloat16
