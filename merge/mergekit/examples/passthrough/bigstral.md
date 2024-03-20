# https://huggingface.co/abacusai/bigstral-12b-32k
# creating new size model 7b 32k -> 12b 32k 


```
dtype: float16
merge_method: passthrough
slices:
- sources:
  - layer_range: [0, 8]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [4, 12]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [8, 16]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [12, 20]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [16, 24]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [20, 28]
    model: mistralai/Mistral-7B-Instruct-v0.2
- sources:
  - layer_range: [24, 32]
    model: mistralai/Mistral-7B-Instruct-v0.2

```