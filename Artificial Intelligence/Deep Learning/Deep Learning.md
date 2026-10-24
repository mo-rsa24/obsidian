# Deep Learning

Up: [[Artificial Intelligence]]

Artificial Intelligence, Deep Learning. [[Attention]] and [[Backpropagation]] sit at the top of Artificial Intelligence, and language models are under [[Large Language Models]].

**Deep learning stacks many learned layers into one network. These notes cover the pieces that recur across architectures: turning tokens into vectors, turning scores into probabilities, and the encoder, decoder, transformer and U-Net shapes built from them.**

- [[Embedding]]: An embedding is a learned vector of numbers that stands for a token, a word, a sentence, an image or any other item, placed so that items with similar meaning sit close together.
- [[Softmax]]: Softmax turns a list of real-valued scores (logits) into probabilities by exponentiating each one and dividing by the sum, so every output is positive, they add to one, and the largest score gets the largest share.
- [[Encoder-Decoder]]: An encoder maps an input to an internal representation (a code, a latent or a sequence of vectors) and a decoder maps that representation to the output, so an encoder-decoder network can turn one kind of thing into another, such as an English sentence into French or a noisy latent back into an image.
- [[Transformer]]: A transformer is a stack of identical blocks, each one multi-head attention followed by a small feed-forward network applied to every token, with a residual connection and layer normalisation around both.
- [[Cross-Attention]]: Cross-attention is attention whose queries come from one sequence and whose keys and values come from another, so a decoder can read its encoder or an image can read its text prompt.
- [[U-Net]]: A U-Net is a convolutional network that downsamples an image through an encoder, upsamples it back through a decoder to the input's size, and copies each encoder level's feature maps across to the matching decoder level, so the output keeps fine spatial detail.
