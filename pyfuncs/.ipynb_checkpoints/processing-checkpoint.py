import os
import pandas as pd

def load_house(csh_num):
    """Give X, y data for particular house
    :params: csh_num, the number of a house dataset
    :returns: X, y train target pandas object"""
    columns = ['lastSensorEventHours', 'lastSensorEventSeconds',
       'lastSensorDayOfWeek', 'windowDuration', 'timeSinceLastSensorEvent',
       'prevDominantSensor1', 'prevDominantSensor2', 'lastSensorID',
       'lastSensorLocation', 'lastMotionLocation', 'complexity',
       'activityChange', 'areaTransitions', 'numDistinctSensors',
       'sensorCount-Bathroom', 'sensorCount-Bedroom', 'sensorCount-Chair',
       'sensorCount-DiningRoom', 'sensorCount-Hall', 'sensorCount-Ignore',
       'sensorCount-Kitchen', 'sensorCount-LivingRoom', 'sensorCount-Office',
       'sensorCount-OutsideDoor', 'sensorCount-WorkArea',
       'sensorElTime-Bathroom', 'sensorElTime-Bedroom', 'sensorElTime-Chair',
       'sensorElTime-DiningRoom', 'sensorElTime-Hall', 'sensorElTime-Ignore',
       'sensorElTime-Kitchen', 'sensorElTime-LivingRoom',
       'sensorElTime-Office', 'sensorElTime-OutsideDoor',
       'sensorElTime-WorkArea']
    dtype_dict = {column:'float64' for column in columns}
    dtype_dict['activity'] = 'object'
    os.chdir('/home/dyllanjr/Documents/Classification-M2/data/processed')
    df = pd.read_csv('csh{}.csv'.format(csh_num))
    return df[columns], df.reduced_activity
