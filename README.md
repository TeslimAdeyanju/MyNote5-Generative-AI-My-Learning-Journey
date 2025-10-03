# 🤖 Large Language Models (LLM) Study Repository

A comprehensive collection of practical implementations, tutorials, and experiments with Large Language Models, PyTorch, and Generative AI techniques. This repository serves as a learning journey through various LLM concepts, from fundamentals to advanced applications.

## 📋 Table of Contents
- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Projects](#projects)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Key Topics Covered](#key-topics-covered)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This repository contains multiple learning modules focusing on:
- **PyTorch fundamentals** and neural network architectures
- **Large Language Model** development and implementation
- **Natural Language Processing** techniques
- **Generative AI** applications
- **Text processing** and tokenization
- **Computer Vision** with image segmentation

## 📁 Repository Structure

```
📦 03-Study-LLM
├── 📁 llm-1-PyTorch/                    # PyTorch fundamentals and neural networks
├── 📁 llm-2-freeCodeCamp-LLM-Course/    # FreeCodeCamp LLM tutorial
├── 📁 llm-3-Build-Large-Language-Model/ # Building LLMs from scratch
├── 📁 llm-3-Sebastian-Raschka-workshop-2024/ # Sebastian Raschka's workshop materials
└── 📁 llm-4-Master-Generative-Ai/       # Generative AI and NLP techniques
```

## 🚀 Projects

### 1. 📚 PyTorch Fundamentals (`llm-1-PyTorch/`)
- **Objective**: Master PyTorch basics and neural network architectures
- **Contents**:
  - PyTorch tensor operations and autograd
  - Neural network building blocks
  - Computer vision applications
  - Image segmentation datasets (`seg_pred/`, `seg_test/`, `seg_train/`)
- **Key Files**:
  - `PyTorch.ipynb` - Main PyTorch tutorial
  - `chapter1.6.ipynb` - Advanced PyTorch concepts
  - `SuperdataScience_PyTorch_From Zero to Hero/` - Comprehensive course materials

### 2. 🎓 FreeCodeCamp LLM Course (`llm-2-freeCodeCamp-LLM-Course/`)
- **Objective**: Learn LLM fundamentals through practical examples
- **Contents**:
  - Text processing and tokenization
  - Language model training basics
- **Key Files**:
  - `notebook.ipynb` - Main course notebook
  - `wizard_of_oz.txt` - Sample text data for training

### 3. 🏗️ Building Large Language Models (`llm-3-Build-Large-Language-Model/`)
- **Objective**: Implement LLMs from scratch
- **Contents**:
  - Custom tokenizer implementation
  - Model architecture design
  - Training pipelines
- **Key Files**:
  - `requirements.txt` - Python dependencies
  - `chapter2/notebook.ipynb` - Implementation notebook
  - `chapter2/the-verdict.txt` - Training text sample

### 4. 👨‍🏫 Sebastian Raschka Workshop 2024 (`llm-3-Sebastian-Raschka-workshop-2024/`)
- **Objective**: Advanced LLM concepts and best practices
- **Contents**: Workshop materials and exercises
- **Environment**: Isolated virtual environment (`.venv/`)

### 5. 🎨 Master Generative AI (`llm-4-Master-Generative-Ai/`)
- **Objective**: Explore various NLP and text processing techniques
- **Contents**:
  - Bag of Words implementation
  - TF-IDF vectorization
  - Word2Vec embeddings
  - Spam classification
  - E-commerce data analysis
- **Key Files**:
  - `Bag of Words.ipynb` - BoW implementation
  - `TF-IDF.ipynb` - TF-IDF vectorization
  - `Word2Vec_(Colab).ipynb` - Word embeddings
  - `TeslimNote-1.ipynb` - Personal study notes
  - `spam.csv` & `Ecommerce_data.csv` - Training datasets

## 🛠️ Getting Started

### Prerequisites
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Git

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TeslimAdeyanju/03-Study-LLM.git
   cd 03-Study-LLM
   ```

2. **Set up virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   # For the main LLM building project
   pip install -r llm-3-Build-Large-Language-Model/requirements.txt
   
   # Additional common dependencies
   pip install torch torchvision jupyter pandas numpy matplotlib scikit-learn
   ```

### Usage

1. **Start Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

2. **Navigate to desired project folder** and open the relevant notebook

3. **Follow the notebooks in recommended order**:
   - Start with `llm-1-PyTorch/PyTorch.ipynb` for fundamentals
   - Progress to `llm-2-freeCodeCamp-LLM-Course/notebook.ipynb`
   - Continue with `llm-3-Build-Large-Language-Model/chapter2/notebook.ipynb`
   - Explore specialized topics in `llm-4-Master-Generative-Ai/`

## 🎓 Key Topics Covered

### Machine Learning & Deep Learning
- ✅ PyTorch tensor operations
- ✅ Neural network architectures
- ✅ Backpropagation and optimization
- ✅ Computer vision applications

### Natural Language Processing
- ✅ Text preprocessing and tokenization
- ✅ Bag of Words (BoW) model
- ✅ TF-IDF vectorization
- ✅ Word2Vec embeddings
- ✅ Language model training

### Large Language Models
- ✅ Transformer architecture
- ✅ Attention mechanisms
- ✅ Custom tokenizer implementation
- ✅ Model fine-tuning techniques

### Practical Applications
- ✅ Spam email classification
- ✅ E-commerce data analysis
- ✅ Image segmentation
- ✅ Text generation

## 📊 Project Status

| Project | Status | Complexity | Focus Area |
|---------|--------|------------|------------|
| PyTorch Fundamentals | 🟢 Active | Beginner-Intermediate | Deep Learning Basics |
| FreeCodeCamp LLM | 🟢 Active | Beginner | LLM Introduction |
| Build LLM from Scratch | 🟡 In Progress | Advanced | LLM Implementation |
| Sebastian Raschka Workshop | 🟡 In Progress | Advanced | Best Practices |
| Generative AI Mastery | 🟢 Active | Intermediate | NLP Techniques |

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📚 Resources & References

- [PyTorch Official Documentation](https://pytorch.org/docs/)
- [FreeCodeCamp LLM Course](https://www.freecodecamp.org/)
- [Sebastian Raschka's Work](https://sebastianraschka.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
