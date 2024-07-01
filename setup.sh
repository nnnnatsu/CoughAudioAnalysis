#!/bin/sh
chmod +x setup.sh
python install_packages.py
PORT=${PORT:-8501}
export PORT
streamlit run streamlit_app.py --server.port $PORT
