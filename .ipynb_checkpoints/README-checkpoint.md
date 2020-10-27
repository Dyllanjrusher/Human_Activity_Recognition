## Human Activity Recognition
---

### The Problem:
---
Smart home technology has become increasingly common during the crux of the information age. Given the diligent protection of privacy, data collected from a smart home can assist disabled people with their day-to-day tasks. Such assistance has already become accessible with, for instance, reminders on your phone. But imagine your entire house acting as a sort of butler for you. When you get dressed, your closet suggests outfits you haven’t worn in a while. When you take your medication, your pill dispenser automatically gives you the pills you need and orders new prescriptions when necessary. When you’re cooking, your fridge suggests new recipes to try based on the food in your fridge, and your stovetop automatically turns off when you’ve left home. All of this may seem like an intrusion of privacy, but for people struggling with day to day tasks such as cooking, dressing, and taking your medication, It could mean the difference between living the rest of their life in a nursing home or the comfort of their own home.

### The Solution; One Bite of the Elephant:
---
It is necessary to build a model that can classify what a resident is doing in their smart home before developing technology to help residents therein. This project focuses on just that. Using the CASAS assisted living dataset to build a supervised model that can classify human activity based on smart home sensors.


### Table of Contents
---

* [exploratory](exploratory) : Exploratory Data Analysis and GCloud startup
    * [1pre_sql_exploration.ipynb](1pre_sql_exploration.ipynb) : Exploring target variables and home sensors before loading 14GBs into remote postgreSQL server.
    * [2extract_annotated_csvs_map.ipynb](2extract_annotated_csvs_map.ipynb) : Script to unzip dataset and get all 30 sensor layout pngs into directory.
    * [3Extracting_csh120.ipynb](3Extracting_csh120.ipynb) : After loading data into Gcloud Compute PostgreSQL server, connected to database with sqlalchemy and visualized data to explore class separability.
    *[testing_d6tstack.ipynb](testing_d6tstack.ipynb) : I used d6stack to create database schemas for me automatically, but tested on a local postgreSQL server first.
    *[gcloud_csvs.py](gcloud_csvs.py) : Script to load all 30 csv's into Gcloud Compute instance
* [model_building](model_building) : Classifier selection and evaluation
    * [1baseline.ipynb](1baseline.ipynb) : Created random forest classifier baseline that performed very well but isn't generalizable.
    * [2model_testing_on_other_houses.ipynb](2model_testing_on_other_houses.ipynb) : Testing baseline on houses it hasn't seen before, target classes not the same in each house dataset.
    * [3activity_narrowing.ipynb](3activity_narrowing.ipynb) : Narrowing target class so that all 30 house datasets have the same classes
    * [4modelling_on_117.ipynb](4modelling_on_117.ipynb) : Trying to model house 117 on other classifiers.
    * [5testing_models_trained_on_117.ipynb](5testing_models_trained_on_117.ipynb) : Model evaluation, previously trained model does not generalize well.
    * [6Sampling_from_houses.ipynb](6Sampling_from_houses.ipynb) : Randomly sampled from 27 out of 30 houses, and ran SMOTE oversampling to create a dataset containing information from 27 houses for increased generalizability.
    * [7Model_on_sampled_data.ipynb](7Model_on_sampled_data.ipynb) : Trained various models on previously made dataset.
    * [8test_sample_trained_model.ipynb](8test_sample_trained_model.ipynb) : Testing random forest classifier on data from houses it has seen (f1 score of .71) and houses it hasn't seen (f1 score of .54)
    * [9load_predictions_into_db.ipynb](9load_predictions_into_db.ipynb) : loaded predictions into local database for use in a flask app (work in progress)
* [pyfuncs](pyfuncs) : Contains function for data processing.
* [flask_app](flask_app) : Work in progress, flask app for simulating live streaming home sensor data predictions.
* [imgs](imgs) : Images for use inside project presentation.


 CASAS Dataset was retrieved from the UCI Machine Learning Repository.
 
Enjoy!

Here's example of the sensor layout of one of the 30 houses. 
![Sensor Map Layout](imgs/csh128.sensor_map.png)

