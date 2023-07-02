# ecml_pkdd2023


solution to “Human Activity Segmentation Challenge” ECML/PKDD'23 [1] where the task was to predict the offsets of activity transitions for multivariate time series


data, python data loaders and baseline approaches: https://github.com/patrickzib/human_activity_segmentation_challenge

competition page: https://www.kaggle.com/competitions/human-activity-segmentation-challenge/overview


### solution

solution consists of the following three steps:

- generation of ClaSP change points for selected channels;

- consolidation of change points obtained from various channels; 

- elimination of irrelevant change points through pruning.

  

To run a code you should launch 3 python scripts - as follow:

#### step 1:

generation of ClaSP change points for selected channels for tuned hyperparameters
(in the selected solution for for x-acc,y-acc,z-acc coordinates)

```
python src/change_points_per_channel.py
```


*input:*

has2023.csv

*output:*

clasp_change_points_json_x-acc.csv

clasp_change_points_json_y-acc.csv

clasp_change_points_json_z-acc.csv

#### step 2:

consolidation of change points obtained from various channels
```
python src/merge_change_points.py
```

*input:*

clasp_change_points_json_x-acc.csv

clasp_change_points_json_y-acc.csv

clasp_change_points_json_z-acc.csv

*output:*
submission_clasp_ensemble_xyz_union.csv

#### step 3:

elimination of irrelevant change points through pruning
```
python src/pruning.py
```


*input:*

submission_clasp_ensemble_xyz_union.csv

*output:*

pruned_400_submission_clasp_ensemble_xyz_union.csv



### results

pruned_400_submission_clasp_ensemble_xyz_union.csv 

public  score: 0.48752

private score: 0.51455


### references 
[1]  Ermshaus, A., Schafer, P., Leser, U., Bagnall, A., Tavenard, R., Leverger, C.,
Lemaire, V., Malinowski, S., Guyet, T., Ifrim, G.: Human Activity Segmentation
Challenge. ECML/PKDD 2023 Discovery Challenge (2023)

