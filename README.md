# Bigram Language Model (From Scratch)

This repository contains an implementation of a **Bigram Language Model** written entirely in Python, built from scratch without relying on advanced NLP libraries. The goal of this project is to demonstrate how statistical language models work at the fundamental level, focusing on **bigram probabilities** for next-word prediction and sentence generation.  

By walking through the process of preprocessing raw text, creating frequency tables, calculating probabilities, and then predicting the next word, this project provides a clear and educational approach to understanding the foundations of Natural Language Processing (NLP).  

---

## 🔑 Key Features

- **Text Preprocessing**  
  Scripts to clean raw text, remove punctuation, and tokenize into words.

- **Frequency Table Construction**  
  Generation of unigram and bigram counts from the input dataset.

- **Probabilistic Modeling**  
  Conversion of raw counts into conditional probabilities using the bigram model:
  \[
  P(w_2 \mid w_1) = \frac{Count(w_1, w_2)}{Count(w_1)}
  \]

- **Next Word Prediction**  
  Predict the most likely next word given a current word.

- **Sentence Generation**  
  Generate text sequences by repeatedly sampling the next word from the probability distribution.

- **Modular Codebase**  
  Organized into multiple scripts for preprocessing, model building, and prediction.

---

## 📂 File Structure
data/                        # Store training text files here
punctuation_removal.py       # Removes punctuation from raw text
data_extraction.py           # Extracts text for processing
token_list.py                # Tokenizes text into words
frequency_table.py           # Builds unigram and bigram frequency tables
probabilistic_model_table.py # Converts counts into conditional probabilities
next_word_predict.py         # Predicts the next word for a given input
sentence_generator.py        # Generates sentences using the bigram model
bigram_list.py               # Lists all bigrams
dataprint.py                 # Utility for inspecting outputs

---

## 🚀 Getting Started

Follow these steps to train your bigram model and use it for prediction:

1. **Prepare Your Data**  
   Place your `.txt` training files inside the `data/` directory. These files will be used to build the frequency tables.

2. **Run Preprocessing Scripts**
   ```bash
   python punctuation_removal.py
   python data_extraction.py
   python token_list.py
3.	Build Frequency and Probability Tables
   python frequency_table.py
   python probabilistic_model_table.py
  	
5. Predict Next Words
   python next_word_predict.py
   
6. Generate Sentences
   python sentence_generator.py

🌱 Future Improvements

This project is intentionally simple, but it can be extended in multiple directions:
	•	Add smoothing techniques (Laplace, Kneser-Ney) to handle unseen bigrams.
	•	Expand to trigrams or n-gram models for better context modeling.
	•	Implement a neural version with PyTorch to learn embeddings and capture richer semantics.
	•	Allow training on large public datasets (e.g., Project Gutenberg).

⸻
🎯 Purpose

The main purpose of this repository is educational. By working with this code, students and developers can gain a deeper understanding of how early NLP models function, how probabilities are computed from raw text, and how these methods evolved into modern neural language models.

This project demonstrates that even without machine learning frameworks, we can still build a working system capable of making predictions and generating sentences from natural text.
