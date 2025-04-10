from flask import Flask, request, jsonify
from flask_cors import CORS
from vanna_setup import vn

vn.allow_llm_to_see_data = True

app = Flask(__name__)
CORS(app, resources={r"/generate-sql": {"origins": "*"}}, supports_credentials=True)

@app.route("/generate-sql", methods=["POST", "OPTIONS"])
def generate_sql():
    if request.method == "OPTIONS":
        # Handle CORS preflight
        return '', 204

    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        sql = vn.generate_sql(question)

        result = []
        with vn.engine.connect() as conn:
            rows = conn.execute(sql)
            result = [dict(row._mapping) for row in rows]

        return jsonify({
            "sql": sql,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "sql": sql if 'sql' in locals() else None,
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, port=8000)
