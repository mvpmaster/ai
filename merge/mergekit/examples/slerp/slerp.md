# tutorial https://www.youtube.com/watch?v=qoQowDbq8_Y
# https://huggingface.co/mvpmaster/Einstein-4D-Marcoro14-7b-full-slerp
# merge 2 models

```
slices:
  - sources:
      - model: argilla/distilabeled-Marcoro14-7B-slerp-full
        layer_range: [0, 32]
      - model: Weyaxi/Einstein-v4-7B
        layer_range: [0, 32]
merge_method: slerp
base_model: argilla/distilabeled-Marcoro14-7B-slerp-full
parameters:
  t:
    - filter: self_attn
      value: [0, 0.5, 0.3, 0.7, 1]
    - filter: mlp
      value: [1, 0.5, 0.7, 0.3, 0]
    - value: 0.5
dtype: bfloat16
```