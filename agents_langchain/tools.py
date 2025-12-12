import json
from typing import Dict, Any

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import StructuredTool

from .prompts import (
    PRODUCT_QUESTIONS_PROMPT,
    FAQ_PROMPT,
    PRODUCT_PAGE_PROMPT,
    COMPARISON_PROMPT,
)
from .schemas import (
    ParseProductInput,
    GenerateQuestionsInput,
    BuildFAQInput,
    ProductOnlyInput,
)


# ===================================================================
# LLM FACTORY (Groq) - UPDATED MODEL
# ===================================================================

def _llm():
    """
    Groq LLaMA 3.1 model (latest supported version).
    """
    return ChatGroq(
        model="llama-3.3-70b-versatile",  # updated recommended model
        temperature=0
    )


# ===================================================================
# JSON Helper
# ===================================================================

def _safe_json(text: str) -> Dict[str, Any]:
    """
    Safely extract JSON from LLM text output.
    """
    if isinstance(text, dict):
        return text

    if not isinstance(text, str):
        raise ValueError("LLM output must be a string or dict.")

    text = text.strip()

    try:
        return json.loads(text)
    except Exception:
        pass

    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("Could not find JSON.")

    return json.loads(text[start:end+1])


# ===================================================================
# AGENTS
# ===================================================================

def parse_product(product: Dict[str, Any]) -> Dict[str, Any]:
    required = [
        "product_name", "concentration", "skin_type",
        "key_ingredients", "benefits", "how_to_use",
        "side_effects", "price_inr"
    ]
    missing = [f for f in required if f not in product]
    if missing:
        return {"error": f"Missing fields: {missing}"}

    # Clean price
    try:
        p = product["price_inr"]
        if isinstance(p, str):
            product["price_inr"] = int(p.replace("₹", "").replace(",", "").strip())
    except:
        pass

    # Ensure lists
    for key in ["skin_type", "key_ingredients", "benefits"]:
        if isinstance(product.get(key), str):
            product[key] = [product[key]]

    return {"product": product}


def generate_questions(product: Dict[str, Any]) -> Dict[str, Any]:
    llm = _llm()
    prompt = PromptTemplate.from_template(PRODUCT_QUESTIONS_PROMPT)
    out = llm.invoke(prompt.format(
        product_json=json.dumps(product, ensure_ascii=False)
    ))
    return _safe_json(out.content)


def build_faq(product: Dict[str, Any], questions: Dict[str, Any]) -> Dict[str, Any]:
    llm = _llm()
    prompt = PromptTemplate.from_template(FAQ_PROMPT)
    out = llm.invoke(prompt.format(
        product_json=json.dumps(product, ensure_ascii=False),
        questions_json=json.dumps(questions, ensure_ascii=False)
    ))
    return _safe_json(out.content)


def build_product_page(product: Dict[str, Any]) -> Dict[str, Any]:
    llm = _llm()
    prompt = PromptTemplate.from_template(PRODUCT_PAGE_PROMPT)
    out = llm.invoke(prompt.format(
        product_json=json.dumps(product, ensure_ascii=False)
    ))
    return _safe_json(out.content)


def build_comparison(product: Dict[str, Any]) -> Dict[str, Any]:
    llm = _llm()
    prompt = PromptTemplate.from_template(COMPARISON_PROMPT)
    out = llm.invoke(prompt.format(
        product_json=json.dumps(product, ensure_ascii=False)
    ))
    return _safe_json(out.content)


# ===================================================================
# EXPORTED TOOLS
# ===================================================================

tools = {
    "parse_product": StructuredTool.from_function(
        func=parse_product,
        name="parse_product",
        description="Validate and normalize raw product JSON.",
        args_schema=ParseProductInput,
    ),
    "generate_questions": StructuredTool.from_function(
        func=generate_questions,
        name="generate_questions",
        description="Generate 15 categorized questions about the product.",
        args_schema=GenerateQuestionsInput,
    ),
    "build_faq": StructuredTool.from_function(
        func=build_faq,
        name="build_faq",
        description="Generate FAQ JSON from product + questions.",
        args_schema=BuildFAQInput,
    ),
    "build_product_page": StructuredTool.from_function(
        func=build_product_page,
        name="build_product_page",
        description="Generate JSON product description page.",
        args_schema=ProductOnlyInput,
    ),
    "build_comparison": StructuredTool.from_function(
        func=build_comparison,
        name="build_comparison",
        description="Generate JSON comparison with fictional product B.",
        args_schema=ProductOnlyInput,
    ),
}
