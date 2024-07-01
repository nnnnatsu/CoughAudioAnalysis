#!/bin/sh
PORT=${PORT:=8501}
streamlit run streamlit_app.py --server.port $PORT
