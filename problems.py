"""Script to display problems and feedback in a nicer way"""

import json


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
        sample = {
            "problem_id": i,
            "type": 0,
            "problem": parsed_data[0][i]["Problem"].strip(),
            "code": parsed_data[0][i]["Code"],
            "quality": parsed_data[0][i]["Identifier Naming Quality"],
            "feedback1": parsed_data[1][i]["feedback"],
            "mapping1": parsed_data[1][i]["mapping"],
            "feedback2": parsed_data[2][i]["feedback"],
            "mapping2": parsed_data[2][i]["mapping"],
        }
        feedback.append(sample)

    return feedback


def print_data(sample):
    print(f"problem_id {sample['problem_id']} ==>")
    print()
    print(sample["code"])
    print()
    print("---")
    print(sample["problem"])
    print("--- WITHOUT CONTEXT")
    for point in sample["feedback1"]:
        print(f"- {point}")
    print("Suggested Improvements")
    for old, new in sample["mapping1"].items():
        print(f"    {old} -> {new}")
    print("--- WITH CONTEXT")
    for point in sample["feedback2"]:
        print(f"- {point}")
    print("Suggested Improvements")
    for old, new in sample["mapping2"].items():
        print(f"    {old} -> {new}")
    print()
    print()
    print()


def main():
    filemap = ["./data/data.in", "./data/nocontext.out", "./data/context.out"]

    feedback = combine_data(filemap)

    for fb in feedback:
        print_data(fb)

    print("Completed")


if __name__ == "__main__":
    main()
