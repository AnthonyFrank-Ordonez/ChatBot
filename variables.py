import time
from datetime import datetime
from difflib import get_close_matches, SequenceMatcher
import json

system_exit: tuple[str, str, str, str] = ("exit", "Exit", "Quit", "quit")
base_knowledge: dict = {
    "what time it is?": f"It's {time.strftime('%I:%M %p')}",
    "time": f"It's {time.strftime('%I:%M %p')}",
    "what date is it?": f'It\'s {datetime.now().strftime("%B %d, %Y (%A)")}',
    "date": f'It\'s {datetime.now().strftime("%B %d, %Y (%A)")}',

}


def check_content(msg_content: str, update: bool = True):
    # Always update the dictionary until the update set to False or 0
    if update:
        with open('train.json', 'r') as content:
            base_knowledge.update(json.load(content))

    #  get the close match from the given input and used the join method to convert it as a string from list also used
    #  the built-in function lower if the user tries to enter a capital or title input
    match: str = ''.join(get_close_matches(msg_content.lower(), base_knowledge, n=1))

    if match in base_knowledge.keys():
        return base_knowledge.get(match)

    else:
        return
