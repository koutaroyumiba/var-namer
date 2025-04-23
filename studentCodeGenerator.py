import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

REPETITIONS = 1  # number of times to call the API
MODEL = "gpt-4o-mini"  # cost effective model to use

print("\nCOMPSCI 747, Semester 1, 2025")
print("Student Code Generator")
print(f"Using model: {MODEL}\n")

prompt = """
You are a CS1-Level University student. You have just begun learning Python programming.

You are given this task:
You are given a 0-indexed string, consisting of lowercase English letters. You need to select one index and remove the letter at that index from the string so that the frequency of every letter present in the string is equal.
  Return true if it is possible to remove one letter so that the frequency of all letters in are equal, and false otherwise.
- Given two strings `s` and `goal`, return `true` if you can swap two letters in `s` so the result is equal to `goal`, otherwise, return `false`.
  Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`
- You are given an array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinate of a point. Check if these points make a straight line in the XY plane.
- You are given two integers `red` and `blue` representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.
  All the balls in a particular row should be the same color, and adjacent rows should have different colors.
  Return the maximum height of the triangle that can be achieved.

Please write the function as if you were a CS1-Level University student, meaning your code should not have meaningful identifier (variables, function, parameter) names, but AVOID one letter names. Return only the function, nothing else. Return five varied functions.
"""


total_tokens_used = 0
for i in range(REPETITIONS):
    completion = client.chat.completions.create(
        model=MODEL, messages=[{"role": "user", "content": prompt}]
    )
    # Print the response
    print(f"\nrequest {i + 1}:\n{completion.choices[0].message.content}")
    # Track total tokens used
    print("=== completion object ===")
    print(completion)
    print(f"prompt tokens: {completion.usage.prompt_tokens}")
    print(f"completion tokens: {completion.usage.completion_tokens}")
    tokens_used = completion.usage.total_tokens
    total_tokens_used += tokens_used
    print(f"Tokens used in request {i + 1}: {tokens_used}")

print(f"\nTotal tokens used across all requests: {total_tokens_used}")
