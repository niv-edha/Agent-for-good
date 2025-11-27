import os 
import json
import time
import random
from google import genai
from google.genai import types

class PlannerAgent:
    def __init__(self):
        # Checks for API Key set in environment (Required for Online)
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            self.offline = True
            self.client = None
            self.model = None
        else:
            self.offline = False
            self.client = genai.Client(api_key=api_key)
            self.model = 'gemini-2.5-flash'
        
        self.plan_schema = types.Schema(
            type=types.Type.OBJECT,
            properties={
                "topic_to_teach": types.Schema(type=types.Type.STRING),
                "difficulty_level": types.Schema(type=types.Type.STRING),
                "key_concepts": types.Schema(type=types.Type.ARRAY, items=types.Schema(type=types.Type.STRING)),
                "learning_goal": types.Schema(type=types.Type.STRING)
            },
            required=["topic_to_teach", "difficulty_level", "key_concepts", "learning_goal"]
        )

        self.system_prompt = "You are the Planner Agent. Your task is to create a structured study plan as a JSON object."

    def generate_plan(self, topic: str, difficulty: str) -> str:
        print(f"🧭 Planner Agent is formulating the plan for '{topic}' ({difficulty})...")
        
        if self.offline:
            # OFFLINE LOGIC
            plan = {
                "topic_to_teach": topic,
                "difficulty_level": difficulty,
                "key_concepts": [
                    f"Introduction to {topic} fundamentals",
                    "Core architectural components and mechanisms",
                    "Practical cloud computing applications",
                    "Security considerations and future directions"
                ],
                "learning_goal": f"The user will gain a practical and theoretical understanding of {topic} at the {difficulty} level."
            }
            return json.dumps(plan)

        # Remote flow (runs only in the Kaggle environment)
        try:
            user_request = f"Create a study plan for the topic: '{topic}' at a '{difficulty}' difficulty level."

            contents = [
                types.Content(role="system", parts=[types.Part.from_text(self.system_prompt)]),
                types.Content(role="user", parts=[types.Part.from_text(user_request)])
            ]

            config = types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=self.plan_schema
            )

            response = self._generate_with_retry(model=self.model, contents=contents, config=config)
            return response.text

        except Exception as e:
            return json.dumps({"error": f"Planner Agent failed: {e}"})

    def _generate_with_retry(self, model, contents, config=None, attempts: int = 3, backoff_factor: float = 1.0):
        last_exc = None
        for attempt in range(attempts):
            try:
                return self.client.models.generate_content(model=model, contents=contents, config=config)
            except Exception as e:
                last_exc = e
                if attempt < attempts - 1:
                    sleep_for = backoff_factor * (2 ** attempt) + random.uniform(0, 0.5)
                    time.sleep(sleep_for)
                    continue
                raise last_exc