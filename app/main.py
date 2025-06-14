from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "✅ Hello from the CI/CD Pipeline!"

if __name__ == '__main__':
# ✅ RIGHT — binds to all interfaces so K8s service can reach it
    app.run(host='0.0.0.0', port=5000)
