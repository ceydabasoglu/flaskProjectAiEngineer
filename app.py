from flask import Flask, request, jsonify
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
import os
from third_tool import rapid_qa_on_pdfs

app = Flask(__name__)
chroma_db = Chroma()
openai_embeddings = OpenAIEmbeddings(api_key="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")


UPLOAD_FOLDER = 'vector_database'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return 'API is running!'
@app.route('/upload-text', methods=['POST'])
def upload_text():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    allowed_extensions = {'txt', 'pdf'}
    if not file.filename.split('.')[-1] in allowed_extensions:
        return jsonify({"error": "Invalid file extension"})

    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    with open(file_path, 'r') as f:
        text = f.read()

    # Convert text to vector using OpenAI embeddings
    vector = openai_embeddings.embed_query(text)


    # Upload vector to Chroma
    vector_id = chroma_db.upload_vector(vector)
    print("Vector uploaded with ID:", vector_id)

    # Get vector from Chroma using its ID
    stored_vector = chroma_db.get_vector(vector_id)
    print("Stored vector:", stored_vector)

    return jsonify({"message": "Text file uploaded successfully"})

@app.route('/vector-search', methods=['POST'])
def vector_search():
    user_message = request.json['message']

    # Convert user message to vector using OpenAI embeddings
    user_vector = openai_embeddings.embed_query(user_message)

    # Perform vector similarity search using Chroma
    similar_vectors = chroma_db.search_similar_vectors(user_vector)

    return jsonify({"similar_vectors": similar_vectors})

from math_tool import MathTool
math_tool = MathTool()


@app.route('/math', methods=['POST'])
def math_operation():
    data = request.json
    if not data or 'operation' not in data or 'operands' not in data:
        return jsonify({'error': 'Geçersiz istek'}), 400

    operation = data['operation']
    operands = data['operands']

    try:
        result = math_tool.perform_operation(operation, operands)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rapid-qa-on-pdfs', methods=['POST'])
def rapid_qa_endpoint():
    data = request.json
    if 'query' not in data:
        return jsonify({'error': 'Invalid request, missing query parameter'}), 400

    query = data['query']
    rapid_qa_on_pdfs(query)

if __name__ == '__main__':
    app.run()

