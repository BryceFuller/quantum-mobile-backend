from flask import Flask, jsonify, request, make_response
import qiskit
app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
  res_string = "No data returned"
  to_run = request.get_json(force=True)
  
  # Break down each command
  for x in range(0, len(to_run)):
    print(to_run[str(x)])

  # Do magic
  return res_string
