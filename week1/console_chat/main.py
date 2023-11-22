import json
from difflib import get_close_matches

data = json.load(open("db.json"))


def load_kb(filepath:str) -> dict:
    """Loads the knowledge base from a file"""
    with open(filepath, "r") as f:
        data:dict = json.load(f)
    return data

def save_kb(filepath:str, data:dict) -> None:
    with open (filepath, "w") as f:
        json.dump(data, f, indent=2)

def find_match(question:str, questions:list[str]) -> str | None:
    """Finds a match for the question in the list of questions"""
    matches:list = get_close_matches(question, questions, n=2, cutoff=0.6)
    if len(matches) == 0:
        return None
    else:
        return matches[0]

def get_answer(question:str, data:dict) -> str | None:
    """Returns an answer for the question from the knowledge base"""
    if question in data:
        return data[question]
    else:
        match = find_match(question, data.keys())
        if match is not None:
            return data[match]
        else:
            return None

def add_question(question:str, answer:str, data:dict) -> None:
    """Adds a question and answer to the knowledge base"""
    data[question] = answer
    print("Question added!")
    print(data)
    return data
def main():
    """ The function starts a loop for taking customer input"""
    print("Our beloved customer, Please welcome to our Chatbot!")
    while True:
        user_input = input("User: ")
        answer = "Chattin:  we don't know, please help me"
        if str(user_input).lower() == "cancel":
            break
        print(answer)
    print("You cancelled, thanks and be back another time")

if __name__ == "__main__":
    main()