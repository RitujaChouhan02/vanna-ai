from flask import Flask, request, jsonify
from flask_cors import CORS
from clickhouse_driver import Client
from vanna_setup import vn
import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env file

vn.allow_llm_to_see_data = True

app = Flask(__name__)
CORS(app, resources={r"/generate-sql": {"origins": "*"}}, supports_credentials=True)

# ✅ Get ClickHouse credentials from environment
CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST", "localhost")
CLICKHOUSE_PORT = int(os.getenv("CLICKHOUSE_PORT", 9000))
CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER")
CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")
CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB")

# ✅ Create ClickHouse client
client = Client(
    host=CLICKHOUSE_HOST,
    port=CLICKHOUSE_PORT,
    user=CLICKHOUSE_USER,
    password=CLICKHOUSE_PASSWORD,
    database=CLICKHOUSE_DB
)

@app.route("/generate-sql", methods=["POST", "OPTIONS"])
def generate_sql():
    if request.method == "OPTIONS":
        return '', 204

    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "No question provided"}), 400

    try:
        sql = vn.generate_sql(question)

        # Run SQL and get results
        rows = client.execute(sql)
        column_names = [col[0] for col in client.execute(f"DESCRIBE TABLE ({sql})")]
        result = [dict(zip(column_names, row)) for row in rows] if rows else []

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


# if __name__ == "__main__":
#     app.run(debug=True, port=8000)
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import clickhouse_connect
# from vanna_setup import vn
# import os
# from dotenv import load_dotenv

# load_dotenv()

# vn.allow_llm_to_see_data = True

# app = Flask(__name__)
# CORS(app, resources={r"/generate-sql": {"origins": "*"}}, supports_credentials=True)

# CLICKHOUSE_HOST = os.getenv("CLICKHOUSE_HOST")
# CLICKHOUSE_PORT = int(os.getenv("CLICKHOUSE_PORT", 443))
# CLICKHOUSE_USER = os.getenv("CLICKHOUSE_USER")
# CLICKHOUSE_PASSWORD = os.getenv("CLICKHOUSE_PASSWORD")
# CLICKHOUSE_DB = os.getenv("CLICKHOUSE_DB")

# # ✅ Use clickhouse-connect for HTTP connection
# client = clickhouse_connect.get_client(
#     host=CLICKHOUSE_HOST,
#     port=CLICKHOUSE_PORT,
#     username=CLICKHOUSE_USER,
#     password=CLICKHOUSE_PASSWORD,
#     database=CLICKHOUSE_DB,
#     secure=True  # This makes it use HTTPS (port 443)
#     verify=False  # ← this solves your SSL issue
# )

# @app.route("/generate-sql", methods=["POST", "OPTIONS"])
# def generate_sql():
#     if request.method == "OPTIONS":
#         return '', 204

#     data = request.get_json()
#     question = data.get("question")

#     if not question:
#         return jsonify({"error": "No question provided"}), 400

#     try:
#         sql = vn.generate_sql(question)

#         result = []
#         query_result = client.query(sql)
#         columns = query_result.columns
#         result = [dict(zip(columns, row)) for row in query_result.result_rows]

#         return jsonify({
#             "sql": sql,
#             "result": result
#         })

#     except Exception as e:
#         return jsonify({
#             "sql": sql if 'sql' in locals() else None,
#             "error": str(e)
#         }), 500

# if __name__ == "__main__":
#     app.run(debug=True, port=8000)

