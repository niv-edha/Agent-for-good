import json
import sys
from google.genai import types 
from planner_agent import PlannerAgent
from teacher_agent import TeacherAgent
from evaluator_agent import EvaluatorAgent

# --- Function to handle real user interaction and collect answers ---
def get_user_answers(quiz_data):
    """
    Presents the quiz to the user and collects their input for grading.
    Returns a dictionary of {question_number: user_answer_text}.
    """
    user_answers = {}
    
    if not isinstance(quiz_data.get("questions"), list):
        print("Warning: Quiz data is missing or invalid question list.")
        return {}

    print("\n===============================================")
    print(f"       STARTING INTERACTIVE QUIZ: {quiz_data.get('quiz_title', 'Quiz')}")
    print("===============================================")
    
    for i, question in enumerate(quiz_data["questions"]):
        q_identifier = question.get("question_number", i + 1)
        options = question.get("options", [])
        
        print(f"\n--- Question {q_identifier} ---")
        print(question.get("question_text", "No question text provided."))
        
        # Display options with numbers
        option_map = {}
        for idx, option in enumerate(options):
            print(f"  {idx + 1}. {option}")
            option_map[str(idx + 1)] = option

        
        # Loop until valid input is received
        while True:
            raw_answer = input(f"Enter the number of your choice (1-{len(options)}): ").strip()
            
            # Check if input is a valid option number
            if raw_answer in option_map:
                # Store the full text of the chosen option
                user_answers[q_identifier] = option_map[raw_answer]
                break
            else:
                print(f"Invalid input. Please enter a number between 1 and {len(options)}.")

    return user_answers

def run_study_streamliner(topic: str, difficulty: str):
    """
    Executes the multi-agent workflow for the Study Streamliner.
    """
    print(f"--- 💡 Starting Study Streamliner for: **{topic}** ({difficulty}) ---")
    
    try:
        # Initialize all agents
        planner = PlannerAgent()
        teacher = TeacherAgent()
        evaluator = EvaluatorAgent()
        
        # Inform the user about the current operating mode
        if planner.offline:
            print("\n*** LOCAL TEST WARNING ***")
            print("Running in **Compliance Offline Mode** (generic content).")
            print("The full LLM functionality will work on the competition platform.")
            print("**************************\n")


        # 1. Planner Agent: Generate the study plan
        study_plan_json = planner.generate_plan(topic, difficulty)
        
        try:
            plan_data = json.loads(study_plan_json)
            print("✅ Plan Generated Successfully:")
            print(json.dumps(plan_data, indent=2))
        except json.JSONDecodeError:
            print(f"❌ Planner failed to return valid JSON. Output:\n{study_plan_json}")
            return

        # 2. Teacher Agent: Generate the lesson based on the plan (uses Google Search tool)
        lesson_content = teacher.generate_lesson(study_plan_json)
        
        print("\n✅ Lesson Generated Successfully. Content Preview:")
        print(lesson_content[:400] + "...")

        # 3. Evaluator Agent: Generate the quiz based on the lesson
        quiz_json = evaluator.generate_quiz(lesson_content)

        try:
            quiz_data = json.loads(quiz_json)
            print("\n✅ Quiz Generated Successfully.")
            
            print("\n\n===============================================")
            print("         STUDY STREAMLINER LESSON")
            print("===============================================")
            
            # Display the Lesson
            print("\n\n*** LESSON ***")
            print(lesson_content)
            
            # --- PHASE 4: USER INTERACTION & FEEDBACK ---
            
            # 4. Interactive Quiz
            user_answers = get_user_answers(quiz_data)
            
            # 5. Evaluator Agent: Provide Feedback (using local grading logic)
            print("\n🧠 Evaluator Agent is grading and providing feedback...\n")
            
            feedback = evaluator.grade_quiz(quiz_data, user_answers)

            print("*** GRADING & FEEDBACK ***")
            print(f"Score: {feedback.get('score')}")
            for det in feedback.get('details', []):
                qn = det.get('question_number')
                print(f"\nQuestion {qn} - Correct: {'YES' if det.get('is_correct') else 'NO'}")
                print(f"  Your answer: {det.get('your_answer')}")
                print(f"  Correct answer: {det.get('correct_answer')}")
                explanation = det.get('explanation')
                if explanation:
                    print(f"  Explanation: {explanation}")
            print("\n===============================================\n")

        except json.JSONDecodeError:
            print(f"❌ Evaluator failed to return valid JSON. Output:\n{quiz_json}")
            return

    except Exception as e:
        print(f"\n\n🛑 A critical error occurred in the Streamliner workflow: {e}")
        print("\n*** SETUP CHECK ***")
        print("The system encountered an error. If running locally without an API key, this is expected in the remote path.")


if __name__ == '__main__':
    VALID_DIFFICULTIES = ["Beginner", "Intermediate", "Advanced"]
    
    if len(sys.argv) != 3:
        print("Usage: python main_streamliner.py <topic_to_study> <difficulty_level>")
        print(f"Accepted difficulties (case-insensitive): {', '.join(VALID_DIFFICULTIES)}")
        sys.exit(1)
        
    study_topic = sys.argv[1]
    study_difficulty = sys.argv[2]
    
    if study_difficulty.capitalize() not in VALID_DIFFICULTIES:
        print(f"🛑 Error: '{study_difficulty}' is not a valid difficulty level.")
        print(f"Please choose from: {', '.join(VALID_DIFFICULTIES)}")
        sys.exit(1)

    validated_difficulty = study_difficulty.capitalize()
    
    run_study_streamliner(study_topic, validated_difficulty)