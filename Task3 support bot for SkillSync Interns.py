# Define a dictionary to store questions and answers
support_data = {
    "how to submit the task": "You can submit your task by following the instructions provided in the task details or by reaching out to your supervisor.",
    "whom to contact for queries": "If you have any queries, please contact the email address mentioned in your offer letter.",
    "what is the task deadline": "The task deadline is November 18, 2023.",
    "how to reach HR": "You can reach the HR department by sending an email to hr@skillsync.com or by calling our HR helpline at +1-123-456-7890.",
    "what are the working hours": "The standard working hours for interns are from 9:00 AM to 5:00 PM, Monday to Friday.",
    "where to find project resources": "You can find project resources and materials on the SkillSync intranet portal under the 'Resources' section.",
    "how to report technical issues": "If you encounter any technical issues, please contact our IT support team at it-support@skillsync.com.",
    "how to request leave": "To request leave, please fill out the leave request form available on the company's website and submit it to your supervisor for approval.",
}

# Function to handle intern questions and provide answers
def answer_question(question):
    question = question.lower()
    if question in support_data:
        return support_data[question]
    else:
        return "I'm sorry, I don't have information on that topic. Please contact your supervisor or HR for assistance."

# Main loop
print("Support Bot: Hello! I'm here to assist you with your questions. Type 'exit' to quit.")
while True:
    user_question = input("You: ").strip()
    if user_question.lower() == "exit":
        print("Support Bot: Goodbye!")
        break
    response = answer_question(user_question)
    print(f"Support Bot: {response}")
