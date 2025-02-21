from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome! Please visit /htop for system information."

@app.route('/htop')
def htop():
    # Get name and username
    name = "sample_name"  # Replace with your name
    username = subprocess.check_output(['whoami']).decode().strip()
    
    # Get IST time
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')
    
    # Get top output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode()
    
    # Format the response
    response = f"""Name: {name}
user: {username}
Server Time (IST): {server_time}
TOP output:
{top_output}"""
    
    return f"<pre>{response}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)