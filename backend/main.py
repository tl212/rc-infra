import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import datastore

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Initialize a datastore client
client = datastore.Client(project="rc-stage2")

# Function to get or create the visitor count entity
def get_or_create_visitor_count():
    entity_ref = client.key("visitorCount", 5634161670881280)
    entity = client.get(entity_ref)
    if entity is None:
        entity = datastore.Entity(key=entity_ref)
        entity['count'] = 0
    return entity

@app.route("/count", methods=['GET', 'POST'])
def save_count():
    try:
        entity = get_or_create_visitor_count()
        if request.method == 'POST':
            entity['count'] += 1
            client.put(entity)
        return jsonify(count=entity['count']), 200
    except Exception as e:
        # Log the error
        app.logger.error(f"Error: {str(e)}") 
        return jsonify(error=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))