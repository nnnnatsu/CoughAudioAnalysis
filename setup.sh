#!/bin/sh
# Ensure distutils is installed
pip install setuptools
pip install wheel
pip install distutils

# Proceed with the rest of the installations
pip install -r requirements.txt

PORT=${PORT:-8501}
export PORT
streamlit run streamlit_app.py --server.port $PORT
