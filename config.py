
#学生信息接入
username = "201918020116"
password = "510106200104075913"

#初始日期设定
Year = 2021


#参数设定
sleep_time = 1

#第几年第几学期(如:202101)设定
term_time = 202101

#链接设定
login_link = 'http://www.aao.cdut.edu.cn/'
schedule_link = 'http://202.115.133.173:805/Classroom/ProductionSchedule/StuProductionSchedule.aspx?termid={term}&stuID={stuid}'.format(term=term_time,stuid='202103080106')


# data = []

# array_1, array_2, array_3, array_4, array_5, array_6, array_7, array_8, array_9, array_10, \
# array_11, array_12, array_13, array_14, array_15, array_16, array_17, array_18, array_19, array_20 = [], [], [], [], [], [], [], [], [], [], \
#                                                                                                      [], [], [], [], [], [], [], [], [], []
#
# dict_1, dict_2, dict_3, dict_4, dict_5, dict_6, dict_7, dict_8, dict_9, dict_10, \
# dict_11, dict_12, dict_13, dict_14, dict_15, dict_16, dict_17, dict_18, dict_19, dict_20 = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, \
#                                                                                            {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

# if my_dict['Week'] == '1':
#     array_1.append(my_dict)
# elif my_dict['Week'] == '2':
#     array_2.append(my_dict)
# elif my_dict['Week'] == '3':
#     array_3.append(my_dict)
# elif my_dict['Week'] == '4':
#     array_4.append(my_dict)
# elif my_dict['Week'] == '5':
#     array_5.append(my_dict)
# elif my_dict['Week'] == '6':
#     array_6.append(my_dict)
# elif my_dict['Week'] == '7':
#     array_7.append(my_dict)
# elif my_dict['Week'] == '8':
#     array_8.append(my_dict)
# elif my_dict['Week'] == '9':
#     array_9.append(my_dict)
# elif my_dict['Week'] == '10':
#     array_10.append(my_dict)
# elif my_dict['Week'] == '11':
#     array_11.append(my_dict)
# elif my_dict['Week'] == '12':
#     array_12.append(my_dict)
# elif my_dict['Week'] == '13':
#     array_13.append(my_dict)
# elif my_dict['Week'] == '14':
#     array_14.append(my_dict)
# elif my_dict['Week'] == '15':
#     array_15.append(my_dict)
# elif my_dict['Week'] == '16':
#     array_16.append(my_dict)
# elif my_dict['Week'] == '17':
#     array_17.append(my_dict)
# elif my_dict['Week'] == '18':
#     array_18.append(my_dict)
# elif my_dict['Week'] == '19':
#     array_19.append(my_dict)
# elif my_dict['Week'] == '20':
#     array_20.append(my_dict)
#
#     dict_1['week'] = array_1
#     all_data.append(dict_1)
#     dict_2['week'] = array_2
#     all_data.append(dict_2)
#     dict_3['week'] = array_3
#     all_data.append(dict_3)
#     dict_4['week'] = array_4
#     all_data.append(dict_4)
#     dict_5['week'] = array_5
#     all_data.append(dict_5)
#     dict_6['week'] = array_6
#     all_data.append(dict_6)
#     dict_7['week'] = array_7
#     all_data.append(dict_7)
#     dict_8['week'] = array_8
#     all_data.append(dict_8)
#     dict_9['week'] = array_9
#     all_data.append(dict_9)
#     dict_10['week'] = array_10
#     all_data.append(dict_10)
#     dict_11['week'] = array_11
#     all_data.append(dict_11)
#     dict_12['week'] = array_12
#     all_data.append(dict_12)
#     dict_13['week'] = array_13
#     all_data.append(dict_13)
#     dict_14['week'] = array_14
#     all_data.append(dict_14)
#     dict_15['week'] = array_15
#     all_data.append(dict_15)
#     dict_16['week'] = array_16
#     all_data.append(dict_16)
#     dict_17['week'] = array_17
#     all_data.append(dict_17)
#     dict_18['week'] = array_18
#     all_data.append(dict_18)
#     dict_19['week'] = array_19
#     all_data.append(dict_19)
#     dict_20['week'] = array_20
#     all_data.append(dict_20)