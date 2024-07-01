#!/bin/sh
# Ensure distutils is installed
pip install setuptools wheel

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
PORT=${PORT:-8501}
export PORT
streamlit run streamlit_app.py --server.port $PORT
