"""Script to make coding the feedback easier"""

import json
from random import shuffle


def parse_file(filename):
    parsed_data = []
    with open(filename, "r") as f:
        input_file = f.read().split("```")
        for block in input_file:
            try:
                current_block = json.loads(block)
                if type(current_block) is list:
                    for subblock in current_block:
                        parsed_data.append(subblock)
                else:
                    parsed_data.append(current_block)
            except Exception:
                print(block)

    return parsed_data


def combine_data(files):
    """
    input: { Problem, Code, Identifier Naming Quality }
    feedback: { feedback, mapping }
    combined: { id, problem, code, quality, feedback, mapping }

    0: input data
    1: feedback without context
    2: feedback with context

    type:
    0 -> without context
    1 -> with context
    """
    parsed_data = []
    feedback = []

    for filepath in files:
        parsed_data.append(parse_file(filepath))

    for i in range(len(parsed_data[0])):
        without_context = {
            "problem_id": i,
            "type": 0,
            "problem": parsed_data[0][i]["Problem"].strip(),
            "code": parsed_data[0][i]["Code"],
            "quality": parsed_data[0][i]["Identifier Naming Quality"],
            "feedback": parsed_data[1][i]["feedback"],
            "mapping": parsed_data[1][i]["mapping"],
        }
        feedback.append(without_context)
        with_context = {
            "problem_id": i,
            "type": 1,
            "problem": parsed_data[0][i]["Problem"].strip(),
            "code": parsed_data[0][i]["Code"],
            "quality": parsed_data[0][i]["Identifier Naming Quality"],
            "feedback": parsed_data[2][i]["feedback"],
            "mapping": parsed_data[2][i]["mapping"],
        }
        feedback.append(with_context)

    return feedback


def coding(i, sample):
    questions = [
        "Actionability: ",
        "Correctness (Prior): ",
        "Correctness (After): ",
        "Justification: ",
    ]

    rating = [-1, -1, -1, -1]

    print(f"{i + 1}/200 == problem_id {sample['problem_id']} ==>")
    print()
    print(sample["code"])
    print()
    print("---")
    print(sample["problem"])
    print("---")
    for point in sample["feedback"]:
        print(f"- {point}")
    print(sample["mapping"])
    print()

    for i, question in enumerate(questions):
        user_rating = -1
        while not 1 <= user_rating <= 4:
            try:
                user_rating = int(input(question))
            except Exception:
                print("invalid input")
        rating[i] = user_rating

    print()
    print()
    print()

    return rating


def main():
    filemap = ["./data/data.in", "./data/nocontext.out", "./data/context.out"]

    feedback = combine_data(filemap)
    shuffle(feedback)

    res = {i: [0, 0] for i in range(100)}

    for i, fb in enumerate(feedback):
        rating = coding(i, fb)
        res[fb["problem_id"]][fb["type"]] = rating

    print(res)


if __name__ == "__main__":
    main()
