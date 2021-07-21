# noinspection PyBroadException
def get_element_exist(dr, element_xpath):
    """
    功能：尝试寻找元素，如若没有找到则会抛出异常
    参数：打开目标网页的webdriver.Chrome
    返回：true为在网页中元素存在，false为不存在
    """
    element_exist = True
    try:
        element = dr.find_element_by_xpath(element_xpath)
    except:
        element_exist = False

    return element_exist
