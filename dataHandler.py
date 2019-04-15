import pandas as pd



###################
# read test file in
###################
def read_csv_file(path, type = False) :
    print("data reading......")
    data = pd.read_csv(path)
    if type:
        print(data.head(5))
        print(path, "include:")
        print(data.columns.values)
        print(data.describe())
        print(data.info())
    return data
############################################################
# this function is used 2 transfer origin data to new format
# mainly handle the chinese char
# define：
# rentType 未知方式-0， 整租-1，合租-2
# houseType x室y厅z卫-xyz， e.g. 3室2厅1卫-321
# houseFloor 高-3， 中-2， 低-1
# houseToward 东-1， 南-2， 西-3， 北-4，暂无数据-0
# houseDecoration 精装-3， 简装-2， 毛坯-1， 其他-0
###########################################################
def transfer_csv_file(ori_data):

    rst_data = ori_data

    rst_data.to_csv("data/transfer_test_a.csv", index=False, encoding='UTF-8')
