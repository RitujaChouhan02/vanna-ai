from vanna_setup import vn  # your Vanna instance from earlier

# Step 4: Ask a natural language question
question = "Give me user_id and total amount who have invested the most in april 2025 with status = 1 and also give me the name of this user"

# Generate SQL using Vanna
sql = vn.generate_sql(question)

# Output the result
print("Your question:", question)
print("Generated SQL:\n", sql)
