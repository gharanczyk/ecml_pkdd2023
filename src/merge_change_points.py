import json
from common import write_submission_file

if __name__ == "__main__":
    xyz_metrics = ["x-acc", "y-acc", "z-acc"]

    single_metrics = {}
    for metric in xyz_metrics:
        file = f"clasp_change_points_json_{metric}.csv"
        with open(file) as fp:
            imported_metric = json.load(fp)
            single_metrics[metric] = imported_metric

    xyz_candidate = [x + y + z for x, y, z in zip(*[single_metrics[metric] for metric in xyz_metrics])]
    xyz_candidate = [sorted(s) for s in xyz_candidate]

    write_submission_file(xyz_candidate, "submission_clasp_ensemble_xyz_union.csv")
