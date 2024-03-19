# example for function calling
function_calling_example="""{
  "id": "chatcmpl-8wmn7kUv4ra0sR506syWCysqQYvxL",
  "object": "chat.completion",
  "created": 1709021269,
  "model": "gpt",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "tool_calls": {
          "function": {
              "name": "name_of_function",
              "arguments": "{\\"area\\":\\"Amsterdam\\"}"
          },
          "type": "function"
        }
      },
      "logprobs": null,
      "finish_reason": "function_call"
    }
  ],
  "usage": {
    "prompt_tokens": 496,
    "completion_tokens": 15,
    "total_tokens": 511
  },
  "system_fingerprint": "fp_9e42505611"
}
"""