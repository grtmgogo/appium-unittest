import datetime
import os
import re
import sys
from collections import OrderedDict
from xml.etree import ElementTree as ET

from appium.webdriver.common.mobileby import MobileBy

import settings
from library.core import Keywords

_ENCODING = sys.stdin.encoding if sys.stdin.encoding else "UTF-8"

DISTINCT_PATH = os.path.join(settings.PROJECT_PATH, 'pages')
TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template')
PAGE_OBJECT_TEMPLATE = os.path.join(TEMPLATE_PATH, 'pageobject.pyt')


def get_template(path):
    with open(path, 'r+', encoding='UTF-8') as t:
        content = t.read()
        return content


def build_page_object(page_name=None, page_description=None, activity=None, locator=None):
    temp = get_template(PAGE_OBJECT_TEMPLATE)
    file_path = ''
    try_times = 0
    while not page_name:
        sys.stdout.write('请输入页面类名：')
        page_name = sys.stdin.readline().strip()
        file_path = os.path.join(DISTINCT_PATH, page_name + '.py')
        if os.path.isfile(file_path):
            page_name = None
        try_times += 1
        if try_times > 3:
            raise Exception('尝试超过3次，请确认页面名不会重复再执行该任务!')
    if not page_description:
        sys.stdout.write('请输入页面描述：')
        page_description = sys.stdin.readline().strip()

    # output = temp % {
    #     'PageName': page_name,
    #     'PageDescription': page_description,
    #     'Activity': activity,
    #     'Locator': locator
    # }
    out = re.sub(r"(%\(PageName\)s)", page_name, temp)
    out = re.sub(r'(%\(PageDescription\)s)', page_description, out)
    out = re.sub(r'(%\(Activity\)s)', activity, out)
    out = re.sub(r'(%\(Locator\)s)', locator, out)
    with open(file_path, 'w+', encoding='UTF-8') as f:
        f.write(out)
        return True


def generate_page_object():
    activity = Keywords.current_driver().current_activity
    page_source = Keywords.current_driver().page_source
    tree = ET.XML(page_source)
    elements = []

    def parse(node):
        for child in node.getchildren():
            resource_id = child.get('resource-id')
            text = child.get('text') if child.get('text') else resource_id
            elements.append((text, (MobileBy.ID, resource_id)))
            parse(child)

    parse(tree)
    # template = get_template(PAGE_OBJECT_TEMPLATE)
    # result = template % {}
    locators = re.sub(r"('[^)]+\),?)", r'\1\n', dict(OrderedDict(elements)).__repr__())
    locators = re.sub(r"(\('id')", r'(MobileBy.ID', locators)
    build_page_object(activity=activity, locator=locators)
    #
    # with open(datetime.datetime.now().timestamp().__str__() + '.py', 'w+', encoding='UTF-8') as f:
    #     f.write('from appium.webdriver.common.mobileby import MobileBy\n')
    #     f.write('ACTIVITY = ' + activity.__repr__() + '\n')
    #
    #     f.write('locators =' + locators)
    return True
