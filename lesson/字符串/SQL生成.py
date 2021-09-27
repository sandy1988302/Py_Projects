import random
import time
import datetime

t = time.time()

print(t)  # 原始时间数据
print(int(t))  # 秒级时间戳
print(int(round(t * 1000)))  # 毫秒级时间戳
print(int(round(t * 1000000)))  # 微秒级时间戳

zhuangru = 'a'
order_no = int(round(time.time() * 1000))
reporter_id = '575158925988740c180acba67addd9e3'
reporter_name = '上报人'
report_time = '2021-09-24 09:31:29'
report_location = '展厅B'
# t_report_work_order
print('INSERT INTO `hnpark_realtymanagement`.`t_report_work_order`'
      '(`order_no`, `reporter_id`, `reporter_name`, `report_time`, `report_location`, `report_content`, `report_image`, `order_source`, `report_type`, `status`, `accept_time`, `finish_time`, `handle_id`, `handle_name`) '
      'VALUES (\'' + str(order_no) + '\', \''+reporter_id+'\', \''+reporter_name+'\', \''+report_time+'\', \''+report_location+'\', \'消防隐患\', NULL, 1, 1, 2, \'2021-09-24 17:43:19\', \'2021-09-25 18:15:00\', \'0f106cbc7320f116c6840d8df0628e0f\', \'物业人员3\');')

print('INSERT INTO `hnpark_realtymanagement`.`t_report_work_order`'
      '(`order_no`, `reporter_id`, `reporter_name`, `report_time`, `report_location`, `report_content`, `report_image`, `order_source`, `report_type`, `status`, `accept_time`, `finish_time`, `handle_id`, `handle_name`) '
      'VALUES (\'' + str(order_no+1) + '\', \''+reporter_id+'\', \''+reporter_name+'\', \''+report_time+'\', \''+report_location+'\', \'消防隐患\', NULL, 1, 1, 2, \'2021-09-25 17:43:19\', \'2021-09-26 18:15:00\', \'342e55f12d59dc957ccba47fa3c00302\', \'物业人员2\');')

# t_report_work_order_rel
