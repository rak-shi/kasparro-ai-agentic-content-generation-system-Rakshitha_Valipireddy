import json
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_core.runnables import RunnableSequence
from agents_langchain.tools import tools

if __name__ == "__main__":
    print("\n🚀 Running LangChain multi-agent pipeline (Groq)...\n")

    product_data = {
        "product_name": "GlowBoost Vitamin C Serum",
        "concentration": "10% Vitamin C",
        "skin_type": ["Oily", "Combination"],
        "key_ingredients": ["Vitamin C", "Hyaluronic Acid"],
        "benefits": ["Brightening", "Fades dark spots"],
        "how_to_use": "Apply 2–3 drops in the morning before sunscreen",
        "side_effects": "Mild tingling for sensitive skin",
        "price_inr": 699
    }

    pipeline = RunnableSequence(
        lambda ctx: {"parsed": tools["parse_product"].invoke({"product": ctx["product"]})},

        lambda ctx: {
            **ctx,
            "questions": tools["generate_questions"].invoke(
                {"product": ctx["parsed"]["product"]}
            )
        },

        lambda ctx: {
            **ctx,
            "faq": tools["build_faq"].invoke(
                {
                    "product": ctx["parsed"]["product"],
                    "questions": ctx["questions"]
                }
            )
        },

        lambda ctx: {
            **ctx,
            "product_page": tools["build_product_page"].invoke(
                {"product": ctx["parsed"]["product"]}
            )
        },

        lambda ctx: {
            **ctx,
            "comparison_page": tools["build_comparison"].invoke(
                {"product": ctx["parsed"]["product"]}
            )
        },
    )

    result = pipeline.invoke({"product": product_data})

    os.makedirs("output_langchain", exist_ok=True)

    with open("output_langchain/faq.json", "w", encoding="utf-8") as f:
        json.dump(result["faq"], f, indent=2, ensure_ascii=False)

    with open("output_langchain/product_page.json", "w", encoding="utf-8") as f:
        json.dump(result["product_page"], f, indent=2, ensure_ascii=False)

    with open("output_langchain/comparison_page.json", "w", encoding="utf-8") as f:
        json.dump(result["comparison_page"], f, indent=2, ensure_ascii=False)

    print("\n✔ All outputs written to ./output_langchain\n")
