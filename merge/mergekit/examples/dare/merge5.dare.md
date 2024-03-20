


# merge 5 models = weight 0.20 - 0.21


models:
  - model: mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
    # No parameters necessary for base model
  - model: mvpmaster/MistralDpoPearl-7b-slerp
    parameters:
      density: 0.4
      weight: 0.20
  - model: SanjiWatsuki/Kunoichi-DPO-v2-7B
    parameters:
      density: 0.4
      weight: 0.20
  - model: mvpmaster/NeuralDareDMistralPro-7b-slerp
    parameters:
      density: 0.4
      weight: 0.20
  - model: mvpmaster/kellemar-KrishnaHercules-0.1-7b-slerp
    parameters:
      density: 0.4
      weight: 0.20
merge_method: dare_ties
base_model: mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
parameters:
  int8_mask: true
dtype: bfloat16