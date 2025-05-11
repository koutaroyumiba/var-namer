import json
import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "gpt-4o-mini"  # cost effective model to use

print("\nCOMPSCI 747, Semester 1, 2025")
print("Variable Feedback Generator")
print(f"Using model: {MODEL}\n")


def no_problem_prompt(student_code):
    return f"""
    Please provide feedback on a student's code with a focus ONLY on variable names, listing specific suggestions for improvement.

Examine the given code and focus on evaluating variable names. Do not critique variables used in loops such as "i". Consider clarity, descriptiveness, and consistency of the variable names in your feedback. Provide feedback based on the initial problem the code is trying to solve.

Output Format

- Provide the feedback in a bullet point list format.
- Use concise sentences, highlighting areas of success and potential improvement in variable naming.
- Output the format in a JSON format:
            {{
                feedback: {{list of feedback here}}
                mapping: {{(key: value of old variable name: new variable name}}
            }}

Student code:
{student_code}
    """.strip()


def with_problem_prompt(problem, student_code):
    return f"""
    Please provide feedback on a student's code with a focus ONLY on variable names, listing specific suggestions for improvement.

Examine the given code and focus on evaluating variable names. Do not critique variables used in loops such as "i". Consider clarity, descriptiveness, and consistency of the variable names in your feedback. Provide feedback based on the initial problem the code is trying to solve.

Output Format

- Provide the feedback in a bullet point list format.
- Use concise sentences, highlighting areas of success and potential improvement in variable naming.
- Output the format in a JSON format:
            {{
                feedback: {{list of feedback here}}
                mapping: {{(key: value of old variable name: new variable name}}
            }}

Problem:
{problem}

Student code:
{student_code}
    """.strip()


def generate(client: OpenAI, prompt):
    return client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    total_tokens_used = 0
    student_data = parse_student_code()
    for i, data in enumerate(student_data):
        # prompt = no_problem_prompt(data["Code"])
        prompt = with_problem_prompt(data["Problem"], data["Code"])
        data = generate(client, prompt)
        print(f"\nrequest {i + 1}:\n{data.choices[0].message.content}")
        print(f"prompt tokens: {data.usage.prompt_tokens}")
        print(f"completion tokens: {data.usage.completion_tokens}")
        tokens_used = data.usage.total_tokens
        total_tokens_used += tokens_used
        print(f"Tokens used in request {i + 1}: {tokens_used}")

    print(f"\nTotal tokens used across all requests: {total_tokens_used}")


def parse_student_code():
    student_code_list = []
    with open("./data/json-format-input.md", "r") as f:
        input_file = f.read().split("```")
        for block in input_file:
            if block[:4] == "json":
                current_block = json.loads(block[4:].strip())
                if type(current_block) is list:
                    for subblock in current_block:
                        student_code_list.append(subblock)
                else:
                    student_code_list.append(current_block)

    """
    [{
        Problem
        Code
        Identifier Naming Quality
    }]
    """
    return student_code_list


if __name__ == "__main__":
    main()
