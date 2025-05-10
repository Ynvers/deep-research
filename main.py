import os
#from dotenv import load_dotenv
from deepsearch import DeepSearch

#load_dotenv()

def main():
    agent = DeepSearch()
    print("Welcome to the Deep Search Agent!")
    print("This agent is designed to help you find information quickly and efficiently.")
    print("Please enter your question: ")
    print("Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        user_question = input("> User: ").strip()
        if user_question.lower() in ["exit", "quit"]:
            print("Exiting the Deep Search Agent. Goodbye!")
            break
        print("Processing your question...")
        agent_response = agent.answer(user_question)
        print("> Deepy : " + agent_response)


if __name__ == "__main__":
    main()