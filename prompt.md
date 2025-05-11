Prompt used for generating code (WITHOUT problems)

```prompt
Generate 4 Python code snippets that demonstrate varied degrees of identifier naming quality based on this seed {seed}. Each snippet should be based on a random common introductory programming task.

- Misleading: Use variable names that are deceptive or totally unrelated to their function.
- Bad: Use vague or nondescriptive variable names.
- Good: Use decent, generally descriptive variable names.
- Perfect: Use highly descriptive and meaningful variable names.

Label each function with its respective identifier naming quality.

# Output Format

- Only return the code with no comments except for the label indicating the naming quality.
- Label each function with one of the following: misleading, bad, good, or perfect.
- Each code snippet must be between 10-20 lines long.
- All snippets should have exactly the same implementation but differ in identifier naming quality.

# Notes

- Enforce identical implementation for all snippets to highlight identifier naming differences.
- Each snippet must strictly adhere to the 10-20 line range.
- Focus on the quality of the identifier names with increasing quality from misleading to perfect as specified.
- It is mandatory for each snippet to be long enough, specifically within the 10-20 lines range, even when implementing misleading or bad identifier names.
```

Prompt using for generating code (WITH problems)

```prompt
Generate 4 Python code snippets that demonstrate varied degrees of identifier naming quality based on this seed {12380384}. Each snippet should be based on a random common introductory programming task.

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

# Notes

- Enforce identical implementation for all snippets to highlight identifier naming differences.
- Each snippet must strictly adhere to the 10-20 line range.
- Focus on the quality of the identifier names with increasing quality from misleading to perfect as specified.
- It is mandatory for each snippet to be long enough, specifically within the 10-20 lines range, even when implementing misleading or bad identifier names.
```

Prompt used for generating feedback (WITHOUT problems)

```prompt
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
<student_code>
```

Prompt used for generating feedback (WITH problems)

```prompt
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
<problem>

Student code:
<student_code>
```
