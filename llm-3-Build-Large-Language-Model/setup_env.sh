#!/bin/bash

# Enhanced Python Environment Setup Script
# Updated for modern data science and LLM development

echo "🚀 Setting up Python environment for LLM and Data Science development..."

# 1. Create a virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv .venv

# 2. Activate the environment
echo "🔧 Activating virtual environment..."
source .venv/bin/activate

# 3. Ensure pip is up to date in your virtual environment
echo "⬆️ Upgrading pip to latest version..."
pip install --upgrade pip

# 4. Install build tools and wheel for better package installation
echo "🛠️ Installing build tools..."
pip install --upgrade setuptools wheel

# 5. Core Development Tools
echo "📓 Installing core development tools..."
pip install --upgrade \
    notebook \
    ipython \
    ipykernel \
    pip-tools \
    jupytext

# 6. Install latest Marimo (interactive notebook alternative)
echo "🌊 Installing latest Marimo..."
pip install --upgrade marimo

# 7. Core Data Science Libraries
echo "🔬 Installing core data science libraries..."
pip install --upgrade \
    numpy \
    pandas \
    matplotlib \
    seaborn \
    scikit-learn \
    scipy \
    plotly \
    jupyter-widgets

# 8. LLM and AI Libraries (optional - uncomment if needed)
echo "🤖 Installing AI/LLM libraries..."
pip install --upgrade \
    transformers \
    torch \
    tokenizers \
    datasets \
    huggingface-hub

# 9. Additional useful libraries for development
echo "📊 Installing additional development tools..."
pip install --upgrade \
    requests \
    beautifulsoup4 \
    python-dotenv \
    tqdm \
    rich

# 10. Generate requirements.txt for reproducibility
echo "📋 Generating requirements.txt..."
pip freeze > requirements.txt

# 11. Display installed packages
echo "✅ Environment setup complete! Installed packages:"
pip list

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📝 To activate this environment in the future, run:"
echo "   source .venv/bin/activate"
echo ""
echo "🌊 To start Marimo, run:"
echo "   marimo edit"
echo ""
echo "📓 To start Jupyter notebook, run:"
echo "   jupyter notebook"
echo ""
echo "📋 Requirements saved to requirements.txt for reproducibility"
