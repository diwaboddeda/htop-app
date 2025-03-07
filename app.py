from flask import Flask, redirect
import os
import datetime
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    """Redirects the root URL to /htop"""
    return redirect('/htop')

@app.route('/htop')
def htop():
    name = "Diwakar Boddeda"  # Your full name
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown User"
    
    # Get Server Time in IST
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    
    # Get top command output (Linux/macOS)
    try:
        top_output = subprocess.run(["top", "-b", "-n", "1"], capture_output=True, text=True).stdout
    except Exception as e:
        top_output = f"Error fetching system info: {str(e)}"

    # Format the response
    response = f"""
    <html>
    <head>
        <title>HTOP Info</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }}
        </style>
    </head>
    <body>
        <h1>HTOP Endpoint</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time.strftime('%Y-%m-%d %H:%M:%S')}</p>
        <h2>System Resource Usage:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
