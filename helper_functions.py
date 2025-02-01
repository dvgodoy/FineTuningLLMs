import torch

def rounding_evolution(lr=3e-3, n_updates=1000, seed=42, decimals=6):
    def round_down(v, decimals):
        return torch.floor(v*10**decimals)/(10**decimals)

    def round_up(v, decimals):
        return torch.ceil(v*10**decimals)/(10**decimals)

    torch.set_default_dtype(torch.float16)
    torch.manual_seed(seed)
    initial = torch.randn(1)
    updates = torch.randn(n_updates)

    res = {False: {}, True: {}}
    for stochastic in [False, True]:
        for decimals in range(3, decimals+1):
            weight = initial.clone()
            history = torch.zeros_like(updates)
            for i in range(len(updates)):
                weight += lr*updates[i]
                rdown = round_down(weight, decimals)
                rup = round_up(weight, decimals)
                if stochastic:
                    prob = (weight - rdown)/(rup - rdown)
                else:
                    prob = 0.0
                weight = rup if torch.rand(1) <= prob else rdown
                history[i] = weight
            res[stochastic].update({decimals: history.numpy()})
    return res

def modify_tokenizer(tokenizer, 
                     alternative_bos_token='<|im_start|>', 
                     alternative_unk_token='<unk>', 
                     special_tokens=None, 
                     tokens=None):
    eos_token, bos_token = tokenizer.eos_token, tokenizer.bos_token
    pad_token, unk_token = tokenizer.pad_token, tokenizer.unk_token

    # BOS token must be different than EOS token
    if bos_token == eos_token:
        bos_token = alternative_bos_token

    # UNK token must be different than EOS token
    if unk_token == eos_token:
        unk_token = alternative_unk_token

    # PAD token must be different than EOS token
    # but can be the same as UNK token
    if pad_token == eos_token:
        pad_token = unk_token
        
    assert bos_token != eos_token, "Please choose a different BOS token."
    assert unk_token != eos_token, "Please choose a different UNK token."

    # Creates dict for BOS, PAD, and UNK tokens
    # Keeps the EOS token as it was originally defined
    special_tokens_dict = {'bos_token': bos_token, 
                           'pad_token': pad_token, 
                           'unk_token': unk_token}
    
    # If there are additional special tokens, add them
    if special_tokens is not None:
        if isinstance(special_tokens, list):
            special_tokens_dict.update({'additional_special_tokens': special_tokens})
        
    tokenizer.add_special_tokens(special_tokens_dict)
    
    # If there are new regular (not special) tokens to add
    if tokens is not None:
        if isinstance(tokens, list):
            tokenizer.add_tokens(tokens)
        
    return tokenizer

def jinja_template(tokenizer):
    return ("{% for message in messages %}"
            f"{{{{'{tokenizer.bos_token}' + message['role'] + '\n' + message['content'] + '{tokenizer.eos_token}' + '\n'}}}}"
            "{% endfor %}"
            "{% if add_generation_prompt %}"
            f"{{{{ '{tokenizer.bos_token}assistant\n' }}}}"
            "{% endif %}")


def add_template(tokenizer, chat_template=None):
    # If not chat template was given, creates a ChatML template
    # using the BOS and EOS tokens
    if chat_template is None:
        chat_template = jinja_template(tokenizer)
        
    # Assigns chat template to tokenizer
    tokenizer.chat_template = chat_template
    
    return tokenizer

def get_multiple_of(vocab_size):
    return 2**(bin(vocab_size)[::-1].find('1'))

def modify_model(model, tokenizer):    
    # If new tokenizer length exceeds vocabulary size
    # resizes it while keeping it a multiple of the same value
    if len(tokenizer) > model.config.vocab_size:
        pad_to_multiple_of = get_multiple_of(model.vocab_size)
        model.resize_token_embeddings(len(tokenizer), 
                                      pad_to_multiple_of=pad_to_multiple_of)    

    # Updates token ids on model configurations
    if getattr(model, "config", None) is not None:
        model.config.pad_token_id = tokenizer.pad_token_id
        model.config.bos_token_id = tokenizer.bos_token_id
        model.config.eos_token_id = tokenizer.eos_token_id
    if getattr(model, "generation_config", None) is not None:
        model.generation_config.bos_token_id = tokenizer.bos_token_id
        model.generation_config.eos_token_id = tokenizer.eos_token_id
        model.generation_config.pad_token_id = tokenizer.pad_token_id
    
    return model

def generate(model, tokenizer, sentence, max_new_tokens=64, skip_special_tokens=False):
    converted_sample = [
        {"role": "user", "content": sentence},
    ]
    prompt = tokenizer.apply_chat_template(converted_sample, 
                                           tokenize=False, 
                                           add_generation_prompt=True)

    tokenized_input = tokenizer(prompt, add_special_tokens=False, return_tensors="pt")
    input_ids = tokenized_input["input_ids"].to(model.device)

    model.eval()
    generation_output = model.generate(input_ids=input_ids, 
                                       eos_token_id=tokenizer.eos_token_id,
                                       max_new_tokens=max_new_tokens)
    
    output = tokenizer.batch_decode(generation_output, 
                                    skip_special_tokens=skip_special_tokens)[0]
    return output
