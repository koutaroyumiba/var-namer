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
        "Justification: ",
        "Correctness (Prior): ",
        "Correctness (After): ",
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


def format_for_csv(result_dictionary):
    # actionability, correctness (pre), correctness (after), justification
    res = [
        "problem_id,actionability1,actionability2,justification1,justification2,c(pre)1,c(pre)2,avg(c(pre)),c(after)1,c(after)2"
    ]
    for key, value in result_dictionary.items():
        # actionability, justification, c(pre), c(after)
        current = [str(key)]
        no_context, context = value
        current.append(str(no_context[0]))
        current.append(str(context[0]))
        current.append(str(no_context[1]))
        current.append(str(context[1]))
        current.append(str(no_context[2]))
        current.append(str(context[2]))
        current.append(str((no_context[2] + context[2]) / 2))
        current.append(str(no_context[3]))
        current.append(str(context[3]))
        res.append(",".join(current))

    return "\n".join(res)


def main():
    filemap = ["./data/data.in", "./data/nocontext.out", "./data/context.out"]

    feedback = combine_data(filemap)
    shuffle(feedback)

    name = input("output file: ")

    res = {i: [[0, 0, 0, 0], [0, 0, 0, 0]] for i in range(100)}

    for i, fb in enumerate(feedback):
        rating = coding(i, fb)
        res[fb["problem_id"]][fb["type"]] = rating

    str_res = format_for_csv(res)

    with open(f"./data/{name}.csv", "w") as f:
        f.write(str_res)

    print("Completed")


if __name__ == "__main__":
    main()
