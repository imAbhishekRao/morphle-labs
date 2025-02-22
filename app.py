from flask import Flask
import os
import psutil
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    username = os.getenv('USER') or os.getenv('USERNAME')

    
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

 
    processes = sorted(psutil.process_iter(['pid', 'name', 'cpu_percent']), 
                       key=lambda p: p.info['cpu_percent'], reverse=True)[:10]
    
   
    top_processes = "<br>".join([f"{p.info['pid']} - {p.info['name']} ({p.info['cpu_percent']}% CPU)" for p in processes])

    return f"""
    <html>
    <head>
        <title>System Monitor</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4; }}
            h1 {{ color: #333; }}
            pre {{ background: white; padding: 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>System Monitor</h1>
        <p><b>Name:</b> Abhishek</p>
        <p><b>Username:</b> {username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Processes:</h2>
        <pre>{top_processes}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
