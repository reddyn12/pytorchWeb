from flask import Flask, send_file
import torch.onnx

app = Flask(__name__)

@app.route('/model')
def get_model():
    # Load the PyTorch model
    model = torch.load('model.pt')
    # Convert the model to ONNX format
    torch.onnx.export(model, 'model.onnx')
    # Return the ONNX model file
    return send_file('model.onnx', mimetype='application/octet-stream')

if __name__ == '__main__':
    app.run()