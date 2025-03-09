from flask import Flask, redirect
import os

app = Flask(__name__)

@app.route('/')
def home():
    return redirect('https://marketplace-personal-portfolio-zi3v2.wstd.io/', code=301)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render assigns a port
    app.run(host='0.0.0.0', port=port)
