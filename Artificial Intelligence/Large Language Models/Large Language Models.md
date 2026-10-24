# Large Language Models

Up: [[Artificial Intelligence]]

Artificial Intelligence, Large Language Models. The model itself is a [[Transformer]] built on [[Attention]], both under Deep Learning.

**A large language model is a transformer trained to predict the next token of text. These notes cover how text becomes tokens, how a trained model is adapted to a task, and how its predictions are scored.**

- [[Tokenization]]: Tokenization splits text into tokens from a fixed vocabulary and gives each an integer ID, and byte-pair encoding builds that vocabulary by repeatedly merging the most frequent adjacent pair of symbols.
- [[Fine-Tuning]]: Fine-tuning continues training a pretrained model on a smaller task-specific dataset, and supervised fine-tuning does it on prompt and response pairs so a base model that only continues text learns to follow instructions.
- [[LoRA]]: LoRA fine-tunes a large model by freezing each chosen weight matrix W and training only a low-rank update BA beside it, so W + BA keeps W's shape while the trainable parameters fall from d² to 2dr.
- [[Perplexity]]: Perplexity is a language model's cross-entropy on a text turned back into a count, 2 to the power H in bits, so it reads as the number of equally likely next tokens the model is choosing between.
- [[KV Cache]]: The KV cache stores the attention keys and values of every token already processed, so each new decoding step computes them only for the newest token.
- [[Retrieval-Augmented Generation]]: Retrieval-augmented generation looks up passages relevant to a question in an outside store and puts them in the model's prompt, so the answer can draw on them.
