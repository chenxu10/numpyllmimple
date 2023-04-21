import numpy as np

def gpt(input):
    output = [
        [0.75,0.1,0.0,0.15,0.0,0.0,0.0],
        [0.0,0.0,0.8,0.1,0.0,0.1],
        [0.0,0.0,0.0,0.1,0.0,0.05,0.85]]
    return output

def generate(input, n_tokens_to_generate):
    for _ in range(n_tokens_to_generate):
        output = gpt(input)
        next_id = np.argmax(output[-1])
        input.append(int(next_id))
    return input[len(input) - n_tokens_to_generate:]