#!/bin/sh
PORT=${PORT:-8501}
export PORT
streamlit run streamlit_app.py --server.port $PORT
