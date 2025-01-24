# FineTuningLLMs

## Setup

- [FAQ](https://github.com/dvgodoy/FineTuningLLMs/blob/main/FAQ.md)
- [Appendix A - Setting Up Your GPU Pod](https://github.com/dvgodoy/FineTuningLLMs/blob/main/AppendixA.md)

## Google Colab

You can easily **load the notebooks directly from GitHub** using Colab and run them using a **GPU** provided by Google. You need to be logged in a Google Account of your own.

You can go through the chapters already using the links below:

- [Chapter 0 - TL;DR](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter0.ipynb)
- [Chapter 1 - Pay Attention to LLMs](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter1.ipynb)
- [Chapter 2 - Loading a Quantized Model](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter2.ipynb)
- [Chapter 3 - Low-Rank Adaptation (LoRA)](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter3.ipynb)
- [Chapter 4 - Formatting Your Dataset](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter4.ipynb)
- [Chapter 5 - Fine-Tuning with `SFTTrainer`](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter5.ipynb)
- [Chapter 6 - Deploying It Locally](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/Chapter6.ipynb)
- [Appendix B - Data Types' Internal Representation](https://colab.research.google.com/github/dvgodoy/FineTuningLLMs/blob/main/AppendixB.ipynb)


## Preface

If you’re reading this, I probably don’t need to tell you that large language models are pretty much _everywhere_, right?

Since the release of ChatGPT in November 2022, it feels almost impossible to keep up with the rapid pace of developments. Every day, there’s a new technique, a new model, or a groundbreaking announcement. These are surely exciting times—but they can also feel overwhelming, exhausting and, at times, frustrating.

"_Where do I even begin to learn this?_" is a perfectly valid question—and a tough one to answer on your own. I wrote this book as a tentative response to that question. It focuses on key concepts that, in my view, have proven to be stable and are likely to remain central to the fine-tuning process for the foreseeable future: quantization, low-rank adapters, and formatting templates.

Mastering these concepts is crucial for understanding the current landscape and will also empower you to handle future developments. They might also be useful to train or fine-tune a variety of large models, not just language models. They are essential tools in any data scientist's toolkit.

****
**This is an intermediate-level book, so to make the most of its content, you need a solid foundation. If Transformers, attention, Adam, tokens, embeddings, and GPUs do not ring any bells, I'd suggest you to start with my beginner-friendly series, _Deep Learning with PyTorch Step-by-Step_.**
****

I chose the Hugging Face ecosystem as the foundation for this book because it is the _de facto_ standard for working with deep learning models, whether they're language models or not. The concepts I  discuss—quantization, adapters, and templates—are neatly implemented and integrated into the ecosystem, making them relatively straightforward to use. But you have to understand how to configure them effectively and what those configurations are actually doing under the hood. It wasn't easy to find out such information out there, though. I missed a comprehensive overview explaining how these techniques work together in practice, especially when fine-tuning LLMs on a single GPU. This is the gap I aim to fill with this book.

Originally, its title was "a short guide," but its scope grew so much that I eventually renamed it "a hands-on guide." It covers a lot of ground, and I truly hope it supports you on your learning journey. Along the way, I've included plenty of fun examples, made-up quotes, and movie references—after all, I believe learning should be fun.

There's nothing cooler than learning about something new, trying it out yourself, and watching it work just fine, don't you agree? That's what you'll do in Chapter 0, the "TL;DR" chapter that will guide you through the entire journey of fine-tuning an LLM: quantization, low-rank adapters, dataset formatting, training, and querying the model. Next, we'll take a step back and have a brief discussion about language models, Transformers, the attention mechanism, and the different types of fine-tuning in Chapter 1.

The following chapters, two through six, correspond to the sections introduced in Chapter 0. In Chapter 2, "Loading a Quantized Model," we'll discuss 8-bit and 4-bit quantization in more detail, as well as the BitsAndBytes configuration. In Chapter 3, "Low-Rank Adaptation (LoRA)," we'll explore the role and usage of low-rank adapters, including how to configure them using the PEFT package and how to prepare the (quantized) base model to improve numerical stability during training. Then, in Chapter 4, "Formatting Your Dataset," we'll focus on data formatting, chat templates, and the role of tokenizers, padding, packing, and data collators.

The next step in our journey is Chapter 5, "Fine-Tuning with `SFTTrainer`," where we'll explore a wide range of configuration possibilites to maximize the performance of a consumer-grade GPU and effectively fine-tune our models. We'll also discuss different implementations of the attention mechanism—Flash Attention and PyTorch's SDPA—and compare their speed and memory requirements. Chapter 6, "Deploying It Locally," is an engineering-focused chapter. It covers the details and alternatives for converting your fine-tuned models to the GGUF format and how to serve your models using either Ollama or llama.cpp.

Every learning journey has its difficulties and pitfalls, and in our case, warnings and raised exceptions. The last chapter, Chapter -1, "Troubleshooting," serves as a reference to help you understand and solve the typical errors you may encounter. 

Finally, there are also two appendices: the first one, "Appendix A: Setting Up Your GPU Pod," is a step-by-step tutorial for using a cloud provider (runpod.io, a personal favorite) to spin up a GPU-powered Jupyter Notebook; the second, "Appendix B: Data Types' Internal Representation," offers an (optional) overview of how integers and floating-point numbers are internally represented by their bits, for those interested in understanding the advantages and disadvantages of each data type in more detail.

That's it! Have fun!
