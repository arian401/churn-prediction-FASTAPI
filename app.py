# app.py
import sys
import subprocess

# Ensure all dependencies are installed when running in Hugging Face Spaces
subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Launch FastAPI app
import uvicorn
uvicorn.run("main:app", host="0.0.0.0", port=7860)
