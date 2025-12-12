PRODUCT_QUESTIONS_PROMPT = """
You must output ONLY valid JSON.

Given the product:

{product_json}

Generate exactly 15 user questions about the product.

Each must be an object like this:
{{ "question": "<text>", "category": "<one of: Informational, Usage, Safety, Purchase, Comparison>" }}

Return exactly:
{{
  "questions": [
    {{ "question": "...", "category": "..." }}
  ]
}}
"""

FAQ_PROMPT = """
You must output ONLY valid JSON.

Given:
product = {product_json}
questions = {questions_json}

Answer each question using ONLY information present in `product`.
Do not hallucinate new facts.

Return exactly:
{{
  "faqs": [
    {{ "question": "", "answer": "", "category": "" }}
  ]
}}
"""

PRODUCT_PAGE_PROMPT = """
You must output ONLY valid JSON.

Given:
{product_json}

Return exactly this structure:
{{
  "product_name": "",
  "summary": "",
  "key_benefits": [],
  "ingredients_section": "",
  "usage_instructions": "",
  "safety_information": "",
  "pricing_section": "",
  "suitable_skin_types": []
}}
"""

COMPARISON_PROMPT = """
You must output ONLY valid JSON.

Given:
{product_json}

Create a fictional competing product (Product B) that is plausible but fictional.
Compare on: Price, Concentration, Key Ingredients, Benefits, Skin Types.

Return exactly:
{{
  "glowboost_product_name": "",
  "product_b_name": "",
  "overview": "",
  "comparisons": [
    {{
      "attribute": "",
      "glowboost_value": "",
      "product_b_value": "",
      "comparison_note": ""
    }}
  ]
}}
"""
