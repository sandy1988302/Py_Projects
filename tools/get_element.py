# noinspection PyBroadException
def get_element_exist(dr, element_xpath):
    element_exist = True
    try:
        # 尝试寻找元素，如若没有找到则会抛出异常
        element = dr.find_element_by_xpath(element_xpath)
    except:
        element_exist = False

    return element_exist
