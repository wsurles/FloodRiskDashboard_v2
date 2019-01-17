# test of methods to access geospatial data
# 1. using .shp file and geopandas
# 2. using .json and python parsing
# 3. using .json in a postgres database and sqlalchemy

#  imports
import geopandas as gpd
import time
import json

# data
shpfile = 'shp\S_Structure.shp'
jsonfile = 'jsons\S_Structure.json'

# .shp file and geopandas test
# datalist= ['dataset_10',
#     'dataset_20',
#     'dataset_30',
#     'dataset_40',
#     'dataset_50',
#     'dataset_60',
#     'dataset_70',
#     'dataset_80',
#     'dataset_90'
# ]
    
def generate_from_shp(shpfile):
    print('starting')

    shp_df = gpd.read_file(shpfile)
    print(shp_df.index)
    
    dataset_10 = shp_df[shp_df['R_SCORE'].between(10,20,inclusive=False)]
    dataset_20 = shp_df[shp_df['R_SCORE'].between(20,30,inclusive=False)]
    dataset_30 = shp_df[shp_df['R_SCORE'].between(30,40,inclusive=False)]
    dataset_40 = shp_df[shp_df['R_SCORE'].between(40,30,inclusive=False)]
    dataset_50 = shp_df[shp_df['R_SCORE'].between(40,50,inclusive=False)]
    dataset_60 = shp_df[shp_df['R_SCORE'].between(50,60,inclusive=False)]
    dataset_70 = shp_df[shp_df['R_SCORE'].between(60,70,inclusive=False)]
    dataset_80 = shp_df[shp_df['R_SCORE'].between(80,90,inclusive=False)]
    dataset_90 = shp_df[shp_df['R_SCORE'].between(80,90,inclusive=False)]
    # print (dataset_90.head())

    shp_to_json = json.loads(dataset_10.to_json())


    # datalist= [dataset_10,
    #     dataset_20,
    #     dataset_30,
    #     dataset_40,
    #     dataset_50,
    #     dataset_60,
    #     dataset_70,
    #     dataset_80,
    #     dataset_90]
    # print(dataset_10)
    # print(shp_to_json)
    # print('finished')
    # for i in datalist:
    #     shp_to_json = json.loads(i.to_json)
    #     # print(shp_to_json)
    #     print(i)



# def generate_from_json(jsonfile):
#     json_df = gpd.read_file(jsonfile)
#     dataset_10 = json_df[json_df['R_SCORE']>10]
#     dataset_20 = json_df[json_df['R_SCORE']>20]
#     dataset_30 = json_df[json_df['R_SCORE']>30]
#     dataset_40 = json_df[json_df['R_SCORE']>40]
#     dataset_50 = json_df[json_df['R_SCORE']>50]
#     dataset_60 = json_df[json_df['R_SCORE']>60]
#     dataset_70 = json_df[json_df['R_SCORE']>70]
#     dataset_80 = json_df[json_df['R_SCORE']>80]
#     dataset_90 = json_df[json_df['R_SCORE']>90]
#     print (dataset_90.head())

# generate_from_json(jsonfile)

# jsondata = json.loads(jsonfile)
# # dataset_10 = jsonfile[0]
# print(jsondata)






if True:
    t0 = time.time()
    generate_from_shp(shpfile)
    t1 = time.time()

    # t2 = time.time()
    # generate_from_json(jsonfile)
    # t3 = time.time()

    print('shp Solve Time: {:.2f} seconds'.format(round(t1 - t0, 2)))
    # print('json Solve Time: {:.2f} seconds'.format(round(t3 - t2, 2)))

