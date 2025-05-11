import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

REPETITIONS = 25  # number of times to call the API
MODEL = "gpt-4o-mini"  # cost effective model to use

print("\nCOMPSCI 747, Semester 1, 2025")
print("Student Code Generator")
print(f"Using model: {MODEL}\n")


def base_prompt(seed):
    return f"""Generate 4 Python code snippets that demonstrate varied degrees of identifier naming quality based on this seed {seed}. Each snippet should be based on a random common introductory programming task.

- Misleading: Use variable names that are deceptive or totally unrelated to their function.
- Bad: Use vague or nondescriptive variable names.
- Good: Use decent, generally descriptive variable names.
- Perfect: Use highly descriptive and meaningful variable names.

Label each function with its respective identifier naming quality.

# Output Format

- Return the problem you are trying to solve.
- Only return the code with no comments except for the label indicating the naming quality.
- Label each function with one of the following: misleading, bad, good, or perfect.
- Each code snippet must be between 10-20 lines long.
- All snippets should have exactly the same implementation but differ in identifier naming quality.
- Return a JSON output that looks like:
    {{
        Problem: {{problem here}}
        Code: {{code snippet here}}
        Identifier Naming Quality: {{label here}}
    }}

# Notes

- Enforce identical implementation for all snippets to highlight identifier naming differences.
- Each snippet must strictly adhere to the 10-20 line range.
- Focus on the quality of the identifier names with increasing quality from misleading to perfect as specified.
- It is mandatory for each snippet to be long enough, specifically within the 10-20 lines range, even when implementing misleading or bad identifier names.
    """.strip()


def generate(client: OpenAI, prompt):
    return client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )


def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    total_tokens_used = 0
    for i in range(REPETITIONS):
        prompt = base_prompt(i)
        data = generate(client, prompt)
        print(f"\nrequest {i + 1}:\n{data.choices[0].message.content}")
        print(f"prompt tokens: {data.usage.prompt_tokens}")
        print(f"completion tokens: {data.usage.completion_tokens}")
        tokens_used = data.usage.total_tokens
        total_tokens_used += tokens_used
        print(f"Tokens used in request {i + 1}: {tokens_used}")

    print(f"\nTotal tokens used across all requests: {total_tokens_used}")


if __name__ == "__main__":
    main()
