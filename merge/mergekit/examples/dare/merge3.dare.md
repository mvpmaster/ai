
# merge 3 models = weight 0.50 - 0.55

models:
  - model: mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
    # No parameters necessary for base 
  - model: mvpmaster/NeuralDareDMistralPro-7b-slerp
    parameters:
      density: 0.4
      weight: 0.5
  - model: mvpmaster/kellemar-KrishnaHercules-0.1-7b-slerp
    parameters:
      density: 0.4
      weight: 0.5
merge_method: dare_ties
base_model: mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
parameters:
  int8_mask: true
dtype: bfloat16