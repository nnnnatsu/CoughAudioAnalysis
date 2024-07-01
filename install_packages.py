# install_packages.py
import os
import subprocess

# List of packages to install
packages = [
    "setuptools",
    "wheel",
    "distutils",
    "streamlit",
    "tensorflow",
    "librosa",
    "soundfile",
    "numpy==1.24.3",
    "audio-recorder-streamlit"
]

# Install each package
for package in packages:
    subprocess.check_call([os.sys.executable, "-m", "pip", "install", package])
