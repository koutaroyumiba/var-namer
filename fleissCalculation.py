import pandas as pd
from statsmodels.stats.inter_rater import fleiss_kappa, aggregate_raters

cats = [1, 2, 3, 4]

def get_fleiss_kappa_for_dimension(dataset, dim):
    cols = [f"{dim}-kot", f"{dim}-maxine", f"{dim}-owen"]
    counts = (
        dataset[cols]
        .apply(lambda row: pd.Series(row.value_counts()), axis=1)
        .fillna(0)
        .reindex(columns=cats, fill_value=0)  # ensure all 1-4 columns exist
        .astype(int)
    )
    print(counts.values)

    return fleiss_kappa(counts.values)

kot = pd.read_csv('data/koutaro.csv')
maxine = pd.read_csv('data/maxine.csv')
owen = pd.read_csv('data/owen.csv')

r1 = kot.add_suffix("-kot").rename(columns={"problem_id-kot": "problem_id"})
r2 = maxine.add_suffix("-maxine").rename(columns={"problem_id-maxine": "problem_id"})
r3 = owen.add_suffix("-owen").rename(columns={"problem_id-owen": "problem_id"})

df = r1.merge(r2, on="problem_id").merge(r3, on="problem_id")

kappa_actionability1 = get_fleiss_kappa_for_dimension(df, "actionability1")
print(f"Fleiss' kappa for actionability with context: {kappa_actionability1:.3f}")
