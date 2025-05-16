"""Script to calculate intercoder reliability"""

import numpy as np
import pandas as pd


def get_fleiss_kappa_for_dimension(dataset, dim):
    # there are 300 examples
    # 100 rows x 3 columns
    cols = [f"{dim}-kot", f"{dim}-maxine", f"{dim}-owen"]
    filtered_dataset = dataset[cols]
    assert (
        filtered_dataset.shape[1] == 3
    ), f"not 3 raters what? {filtered_dataset.shape[1]}"
    n_raters = filtered_dataset.shape[1]  # number of raters // should be 3
    assert (
        filtered_dataset.shape[0] == 100
    ), f"not 100 samples what? {filtered_dataset.shape[0]}"
    n_samples = filtered_dataset.shape[0]  # number of raters // should be 100
    n_categories = 4

    # contingency_table = np.zeros((n_samples, 4))
    #
    # for i in range(n_samples):
    #     for category in range(1, 5):
    #         contingency_table[i, category - 1] = np.sum(
    #             filtered_dataset.iloc[i] == category
    #         )
    #
    # kappa = fleiss_kappa(contingency_table)
    # print(kappa)
    # return kappa

    contingency_table = np.zeros((n_samples, n_categories))

    for i in range(n_samples):
        for category in range(1, n_categories + 1):
            contingency_table[i, category - 1] = np.sum(
                filtered_dataset.iloc[i] == category
            )

    total_cells = n_raters * n_samples
    # print("w", contingency_table)
    # 0 -> 99, 0 -> 3
    # print("w2", contingency_table[0][0])

    small_p = [0] * n_categories
    big_p = [0] * n_samples

    for i in range(n_samples):
        # print(contingency_table[i])
        for j in range(n_categories):
            rater_count = contingency_table[i, j]
            small_p[j] += rater_count
            big_p[i] += rater_count**2

    # print(big_p)
    print(big_p.count(9))
    print(big_p.count(5))

    for i in range(n_samples):
        big_p[i] = (1 / ((n_raters) * (n_raters - 1))) * (big_p[i] - n_raters)

    for i in range(n_categories):
        small_p[i] = (small_p[i] / total_cells) ** 2

    # print("small p")
    # print(small_p)

    P_o = sum(big_p) / n_samples
    P_e = sum(small_p)

    print(P_o, P_e)

    # # Calculate the observed agreement (P_o)
    # P_o = np.sum(np.square(np.sum(contingency_table, axis=1))) / (n_raters * n_samples)
    #
    # # Calculate the expected agreement (P_e)
    # category_totals = np.sum(contingency_table, axis=0)
    # P_e = np.sum(np.square(category_totals)) / (n_raters * n_samples) ** 2

    # Calculate Fleiss' Kappa
    kappa = (P_o - P_e) / (1 - P_e)
    return kappa


def main():
    kot = pd.read_csv("data/koutaro.csv")
    col = kot.columns[1:]
    maxine = pd.read_csv("data/maxine.csv")
    owen = pd.read_csv("data/owen.csv")

    r1 = kot.add_suffix("-kot").rename(columns={"problem_id-kot": "problem_id"})
    r2 = maxine.add_suffix("-maxine").rename(
        columns={"problem_id-maxine": "problem_id"}
    )
    r3 = owen.add_suffix("-owen").rename(columns={"problem_id-owen": "problem_id"})

    df = r1.merge(r2, on="problem_id").merge(r3, on="problem_id")

    for header in col:
        kappa = get_fleiss_kappa_for_dimension(df, header)
        print(header, "kappa =", kappa)


if __name__ == "__main__":
    main()
