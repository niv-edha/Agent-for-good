import os
import json
import time
import random
from google import genai
from google.genai import types

# --- Tool Implementation ---

def google_search(query: str) -> str:
    print(f"\n⚙️ Teacher Agent is searching for: '{query}'...")
    return f"Top search results for '{query}' (simulated)."


class TeacherAgent:
    def __init__(self):
        # Check for API Key set in environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.offline = True
            self.client = None
            self.model = None
        else:
            self.offline = False
            self.client = genai.Client(api_key=api_key)
            self.model = 'gemini-2.5-flash'

        self.tools = [google_search]

        self.system_prompt = (
            "You are the **Teacher Agent**. Your task is to take the provided study plan (JSON) "
            "and teach the subject in an engaging, detailed lesson. "
            "Use the 'google_search' tool to fetch current information."
        )

    def generate_lesson(self, study_plan_json: str) -> str:
        print("\n\n👨‍🏫 Teacher Agent is starting the lesson generation...")
        try:
            if self.offline:
                # OFFLINE LOGIC: Injecting meaningful content
                try:
                    plan = json.loads(study_plan_json)
                except Exception:
                    plan = {"topic_to_teach": "Topic", "key_concepts": ["Concept 1", "Concept 2"]}

                title = plan.get("topic_to_teach", "Study Topic")
                key_concepts = plan.get("key_concepts", [])

                lesson_lines = [
                    f"## OFFLINE LESSON: {title}",
                    "---",
                    "This lesson is generated in offline mode (no API key detected).",
                    "**NOTE:** Content is static for compliance testing; online mode is required for dynamic lessons.",
                ]
                
                # Use a dictionary for sample content based on the Merkle Tree run
                sample_content = {
                    "Introduction to Merkle Trees: Definition and Purpose": 
                        "A **Merkle Tree**, or hash tree, is a data structure used for secure verification of large datasets. Its primary purpose is to allow quick validation that a piece of data hasn't been tampered with, without checking the entire dataset.",
                    "Merkle Tree Construction: Hashing and Root Generation":
                        "Construction is a bottom-up process: individual data blocks (leaves) are hashed, pairs of hashes are concatenated and re-hashed, until a single final hash—the **Merkle Root**—is generated. Any change to a leaf changes the root.",
                    "Data Verification using Merkle Proofs":
                        "A **Merkle Proof** includes the data block's hash and a list of sibling hashes (the authentication path). Combining these allows one to independently recalculate the Merkle Root. If the calculated root matches the trusted root, the data is verified.",
                    "Applications in Secure Databases: Distributed Ledgers and Tamper Detection":
                        "Merkle Trees are the cornerstone of blockchain technology. They secure all transactions within a block, and the Merkle Root in the block header allows 'light clients' to efficiently verify transactions without downloading the full chain.",
                    "Introduction to Birth of Ai fundamentals": 
                        "The birth of AI is generally traced back to the **Dartmouth Workshop in 1956**, where the term 'Artificial Intelligence' was first coined. Early pioneers like John McCarthy, Marvin Minsky, and Claude Shannon laid the theoretical foundations for machines that could think, learn, and solve problems.",
                    "Core architectural components and mechanisms":
                        "Early AI focused on symbolic logic and problem-solving through **expert systems** and **search algorithms** (like A*). These systems used explicitly programmed knowledge bases and rules, contrasting sharply with modern, data-driven deep learning.",
                    "Practical cloud computing applications":
                        "Modern AI is dominant in the cloud, powering services like **Google Cloud AI** and **AWS SageMaker**. Applications include natural language processing (NLP) for customer service, computer vision for security, and large language models (LLMs) for content generation.",
                    "Security considerations and future directions":
                        "Security concerns include **data privacy** and **model bias**. Future AI is moving toward more generalized intelligence (AGI) and increasing **autonomy**, requiring robust regulatory frameworks and ethical guardrails."
                }
                
                for i, kc in enumerate(key_concepts, start=1):
                    # Use sample content if available, otherwise fall back to a generic message
                    content = sample_content.get(kc, f"Explanation for '{kc}' is available in the full Online Mode.")
                    lesson_lines.append(f"\n### {i}. {kc}\n\n{content}")

                return "\n".join(lesson_lines)

            # Remote flow (runs only in the Kaggle environment)
            # ... (rest of the code remains the same)
            
            # --- [Code from your original teacher_agent.py file continues here] ---
            # NOTE: For brevity, the full remote code block is omitted but must be present in your file.
            # ---------------------------------------------------------------------

        except Exception as e:
            return f"An error occurred in the Teacher Agent: {e}. Check authentication."

    # ... (rest of the code for _generate_with_retry) ...