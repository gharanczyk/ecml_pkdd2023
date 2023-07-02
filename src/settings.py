path = "/human_activity_segmentation_challenge/"
dataset_path = path + "datasets/has2023.csv"

segment_length_threshold = 400
parameter_n_estimators = 10
parameter_k_neighbours = 3
parameter_window_size = "suss"
parameter_score = "roc_auc"

metrics = ["x-acc", "y-acc", "z-acc", "x-gyro", "y-gyro", "z-gyro", "x-mag", "y-mag", "z-mag", "lat", "lon", "speed"]
