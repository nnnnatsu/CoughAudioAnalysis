#!/bin/sh
# Ensure setuptools, wheel, and python3-distutils are installed
pip install setuptools wheel
apt-get update
apt-get install -y python3-distutils

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
PORT=${PORT:-8501}
export PORT
streamlit run streamlit_app.py --server.port $PORT
