---
title: Andrej Karpathy-Tokenizer
mathjax: true
toc: true
categories:
  - Study
tags:
  - LLM
---

[Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE) sounds trivial but plays such an important role in LLM. It actually simply explains why LLM is not good at math arithmatics.

## 0 Unicode and UTF
Issues in LLM may track back to tokenizations.
![Alt text](/assets/images/2024/24-05-18-Karpathy-tokenizer_files/issues.png) 
Mapping from character to numbers, ASCII is using 1 byte to map 128 most common used characters.
![Alt text](/assets/images/2024/24-05-18-Karpathy-tokenizer_files/ascii.png)
Resource for Unicode [here](https://www.reedbeta.com/blog/programmers-intro-to-unicode/)
 
Unicode converts characters, or grapheme according to this [video](https://www.youtube.com/watch?v=ut74oHojxqo), to **code points**. There are over 1M code points in the codespace and only 12% are used ( so lots of rooom to grow)
![Alt text](/assets/images/2024/24-05-18-Karpathy-tokenizer_files/unicode.png)
UTF-8 manifesto [here](https://utf8everywhere.org/).  
UTF(Unicode Tranformation Format) converts unicode to bytes. UTF-8/16 converts to 1~4 bytes and UTF-32 to 4 bytes(directly converting same as ASCII to 1 byte). UTF-8 is most widely used.
![Alt text](/assets/images/2024/24-05-18-Karpathy-tokenizer_files/utf8.png) 
So we should use **unicode aware string** to get correct string length
```python
s="👍"
len(s) == 4
s=u"👍"
len(s) == 1
```
If raw byte sequences can be directly feed into LLM, it would be great improvment but still not available for now. (one [paper](https://arxiv.org/pdf/2305.07185))

## 1. BPE(Byte Pair Encoding)
The [example](https://en.wikipedia.org/wiki/Byte_pair_encoding) from wiki is simple and clear. Repetitively replacing "byte pairs" with new code, so dictionary with new byte pairs keep growing and the encoding length keep decreasing.
1. Given a list of integers, return a dictionary of counts of consecutive pairs
  ```python
  #characters to bytes
  utf8 = "test".encode("utf-8")
  #bytes to integers
  #ids = list(utf8)
  ids = list(map(int,utf8))
  # ord to get the unicode of cha
  ids[0] == ord('t')
  def get_stats(ids, counts=None):
      """
      Example: [1, 2, 3, 1, 2] -> {(1, 2): 2, (2, 3): 1, (3, 1): 1}
      """
      for pair in zip(ids, ids[1:]): # iterate consecutive elements
          counts[pair] = counts.get(pair, 0) + 1
      return counts
  stats = get_stats(ids)
  ## stats a list of {(pair0, pair1):freq}
  ## max return keys for a map, based on the max value
  top_pair = max(stats, key=stats.get)
  #Get the character of this byte
  chr(top_pair[0])
  ```  

2. In the list of integers (ids), replace all consecutive occurrences
    of pair with the new integer token idx
  ```python
  def merge(ids, pair, idx):
    """
    Example: ids=[1, 2, 3, 1, 2], pair=(1, 2), idx=4 -> [4, 3, 4]
    """
    newids = []
    i = 0
    while i < len(ids):
        # if not at the very last position AND the pair matches, replace it
        if ids[i] == pair[0] and i < len(ids) - 1 and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids
  ```
3. Training for the tokenizer by iteratively merging the most common pairs to create new tokens
  ```python
  num_merges = vocab_size - 256

  # input text preprocessing
  text_bytes = text.encode("utf-8") # raw bytes
  ids = list(text_bytes) # list of integers in range 0..255

  merges = {} # (int, int) -> int
  vocab = {idx: bytes([idx]) for idx in range(256)} # int -> bytes
  for i in range(num_merges):
      # count up the number of times every consecutive pair appears
      stats = get_stats(ids)
      # find the pair with the highest count
      pair = max(stats, key=stats.get)
      # mint a new token: assign it the next available id
      idx = 256 + i
      # replace all occurrences of pair in ids with idx
      ids = merge(ids, pair, idx)
      # save the merge
      merges[pair] = idx
      vocab[idx] = vocab[pair[0]] + vocab[pair[1]]
  ```
4. Decode and Encode  
Decode may not work for every bytes, so `error="replace"` will catch the fell through bytes
  ```python
  def decode(self, ids):
    # given ids (list of integers), return Python string
    text_bytes = b"".join(self.vocab[idx] for idx in ids)
    text = text_bytes.decode("utf-8", errors="replace")
    return text
  ```
  Encoding needs to find the pair with the lowest merge index
  ```python
   def encode(self, text):
        # given a string text, return the token ids
        text_bytes = text.encode("utf-8") # raw bytes
        ids = list(text_bytes) # list of integers in range 0..255
        while len(ids) >= 2:
            stats = get_stats(ids)
            pair = min(stats, key=lambda p: self.merges.get(p, float("inf")))
            # subtle: if there are no more merges available, the key will
            # result in an inf for every single pair, and the min will be
            # just the first pair in the list, arbitrarily
            # we can detect this terminating case by a membership check
            if pair not in self.merges:
                break # nothing else can be merged anymore
            # otherwise let's merge the best pair (lowest merge index)
            idx = self.merges[pair]
            ids = merge(ids, pair, idx)
        return ids
  ```