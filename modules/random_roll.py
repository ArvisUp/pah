"""

Responsible for randomly choosing prompt and response strings from test files

"""
import random as r


def random_string():
    """Combines chosen lines in one"""
    prompt_lines = open('./txt_files/prompt.txt').read().splitlines()
    random_prompt_line = r.choice(prompt_lines)

    response_lines = open('./txt_files/resp.txt').read().splitlines()
    random_response_line = r.choice(response_lines)

    # Checks where the response line goes, and if it should be in lower case.
    if random_prompt_line.startswith('{}'):
        return(random_prompt_line.format(random_response_line))
    else:
        return(random_prompt_line.format(random_response_line.lower()))
