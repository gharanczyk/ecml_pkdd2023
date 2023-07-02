import pandas as pd
from tqdm import tqdm
from common import write_submission_file
from settings import segment_length_threshold


def prune_df(df, segment_length_threshold):
    dfg = pd.DataFrame(df.groupby("ts_id")["segment_length"].max().reset_index())

    for index, row in tqdm(df.iterrows(), total=df.shape[0]):
        segment_length = row["segment_length"]
        current_id = row["ts_id"]
        id_max_value = dfg.query(f"ts_id =={current_id}")["segment_length"].values

        if segment_length < segment_length_threshold and index > 1 and id_max_value > segment_length_threshold:
            df.drop(index, inplace=True)
    return df


def get_change_points_from_df(df):
    df["segment_start"] = df["segment_start"].astype(str)
    dfs = df.groupby(["ts_id"], as_index=False).agg({"segment_start": " ".join})
    change_points = dfs.segment_start.values
    change_points = [p.split(" ") for p in change_points]
    change_points = [[int(p) - 1 for p in points_list[1:]] for points_list in change_points]
    return change_points


def create_pruned_submission_file(submission_file, segment_length_threshold):
    df = pd.read_csv(submission_file)
    df["segment_start"] = df.segment.apply(lambda x: int(x.split(" ")[0]))
    df["segment_length"] = df.segment.apply(lambda x: int(x.split(" ")[1]))
    df_pruned = prune_df(df, segment_length_threshold)
    new_change_points = get_change_points_from_df(df_pruned)
    write_submission_file(new_change_points, f"pruned_{segment_length_threshold}_{submission_file}")


if __name__ == "__main__":
    submission_file = "submission_clasp_ensemble_xyz_union.csv"
    create_pruned_submission_file(submission_file, segment_length_threshold)
