import os
import subprocess

if __name__ == "__main__":
    # Path to the streamlit app
    app_path = os.path.join("src", "ui", "app.py")
    
    # Run the streamlit command
    subprocess.run(["streamlit", "run", app_path])
