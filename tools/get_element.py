# noinspection PyBroadException
def get_element_exist(dr, element_xpath):
    """
    :param dr: 打开目标网页的webdriver.Chrome
    :param element_xpath: 元素xpath位置
    :return: 在网页中元素存在
    """
    element_exist = True
    try:
        element = dr.find_element_by_xpath(element_xpath)
    except:
        element_exist = False

    return element_exist


def check_element(bsobj, label, attr, attr_value):
    """
    :param bsobj: 打开目标网页的webdriver.Chrome
    :param label: 元素xpath位置
    :param attr: 元素xpath位置
    :param attr_value: 元素xpath位置
    :return: 在网页中元素存在
    """
    element_exist = True
    try:
        bsobj.find(label, attrs={attr: attr_value})
    except:
        element_exist = False
    return element_exist
