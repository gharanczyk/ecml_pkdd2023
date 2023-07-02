from claspy.segmentation import BinaryClaSPSegmentation
from tqdm import tqdm
import json
from common import load_unzip_data, union_lists
from settings import (
    metrics,
    dataset_path,
    parameter_n_estimators,
    parameter_k_neighbours,
    parameter_window_size,
    parameter_score,
)


def get_clasp_segments(row, metrics=metrics):
    cps_all = []
    for metric in metrics:
        metric_values = row[metric]
        try:
            clasp = BinaryClaSPSegmentation(
                n_estimators=parameter_n_estimators,
                k_neighbours=parameter_k_neighbours,
                window_size=parameter_window_size,
                score=parameter_score,
            )
            cps = clasp.fit_predict(metric_values)
            cps = [int(c) for c in cps]
        except:  # e.g., TypeError: Object of type int64 is not JSON serializable
            cps = []
        cps = list(cps)
        cps_all.append(cps)

    return cps_all


def clasp_submission(selected_metrics, subset=250):
    change_points = []

    for _, row in tqdm(df.iloc[:subset, :].iterrows(), total=df.iloc[:subset, :].shape[0]):
        cps_clasp_all = get_clasp_segments(row, metrics=selected_metrics)

        cps_claps_all_union = union_lists(*cps_clasp_all)
        cps_claps_all_union = sorted(cps_claps_all_union)
        change_points.append(cps_claps_all_union)

    return change_points


if __name__ == "__main__":
    df = load_unzip_data(dataset_path)
    xyz_metrics = ["x-acc", "y-acc", "z-acc"]

    for metric in xyz_metrics:
        change_points_single_metric = clasp_submission([metric])
        with open(f"clasp_change_points_json_{metric}.csv", "w") as fp:
            json.dump(change_points_single_metric, fp)
