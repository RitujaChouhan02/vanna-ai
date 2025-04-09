from vanna_setup import vn  # your Vanna instance from earlier
from doc import fetch_google_doc_text


doc_id = "1Z2vseeWcZ24Ru9isd0zHwFWVQ5qg_fDZbevEl1SIrTI"
domain_knowledge = fetch_google_doc_text(doc_id)
vn.add_documentation(domain_knowledge)

# Step 4: Ask a natural language question
question = "Give me the value of the AUM on DoD basis from november 1, 2024"

# Generate SQL using Vanna
sql = vn.generate_sql(question)

# Output the result
print("Your question:", question)
print("Generated SQL:\n", sql)