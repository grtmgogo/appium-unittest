from appium.webdriver.common.mobileby import MobileBy

from library.core.BasePage import BasePage
from library.core.TestLogger import TestLogger


class SelectOneGroupPage(BasePage):
    """选择一个群页面"""
    ACTIVITY = 'com.cmcc.cmrcs.android.ui.activities.GroupChatListActivity'

    __locators = {'': (MobileBy.ID, ''),
                  'com.chinasofti.rcs:id/action_bar_root': (MobileBy.ID, 'com.chinasofti.rcs:id/action_bar_root'),
                  'android:id/content': (MobileBy.ID, 'android:id/content'),
                  'com.chinasofti.rcs:id/select_picture_custom_toolbar': (
                  MobileBy.ID, 'com.chinasofti.rcs:id/select_picture_custom_toolbar'),
                  '返回': (MobileBy.ID, 'com.chinasofti.rcs:id/left_back'),
                  'com.chinasofti.rcs:id/select_picture_custom_toolbar_back_btn': (
                  MobileBy.ID, 'com.chinasofti.rcs:id/select_picture_custom_toolbar_back_btn'),
                  '选择一个群': (MobileBy.ID, 'com.chinasofti.rcs:id/select_picture_custom_toolbar_title_text'),
                  '搜索群组': (MobileBy.ID, 'com.chinasofti.rcs:id/et_search'),
                  'com.chinasofti.rcs:id/contentFrame': (MobileBy.ID, 'com.chinasofti.rcs:id/contentFrame'),
                  'com.chinasofti.rcs:id/recyclerView_contactList': (
                  MobileBy.ID, 'com.chinasofti.rcs:id/recyclerView_contactList'),
                  'com.chinasofti.rcs:id/contact_list': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_list'),
                  'com.chinasofti.rcs:id/rl_group_list_item': (MobileBy.ID, 'com.chinasofti.rcs:id/rl_group_list_item'),
                  'Q': (MobileBy.ID, ''),
                  'com.chinasofti.rcs:id/contact_image': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_image'),
                  '群聊002': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
                  '群聊001': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
                  '群聊名': (MobileBy.ID, 'com.chinasofti.rcs:id/contact_name'),
                  'com.chinasofti.rcs:id/contact_index_bar_view': (
                  MobileBy.ID, 'com.chinasofti.rcs:id/contact_index_bar_view'),
                  'com.chinasofti.rcs:id/contact_index_bar_container': (
                  MobileBy.ID, 'com.chinasofti.rcs:id/contact_index_bar_container'),
                  'A': (MobileBy.ID, ''),
                  'B': (MobileBy.ID, ''),
                  'C': (MobileBy.ID, ''),
                  'D': (MobileBy.ID, ''),
                  'E': (MobileBy.ID, ''),
                  'F': (MobileBy.ID, ''),
                  'G': (MobileBy.ID, ''),
                  'H': (MobileBy.ID, ''),
                  'I': (MobileBy.ID, ''),
                  'J': (MobileBy.ID, ''),
                  'K': (MobileBy.ID, ''),
                  'L': (MobileBy.ID, ''),
                  'M': (MobileBy.ID, ''),
                  'N': (MobileBy.ID, ''),
                  'O': (MobileBy.ID, ''),
                  'P': (MobileBy.ID, ''),
                  'R': (MobileBy.ID, ''),
                  'S': (MobileBy.ID, ''),
                  'T': (MobileBy.ID, ''),
                  'U': (MobileBy.ID, ''),
                  'V': (MobileBy.ID, ''),
                  'W': (MobileBy.ID, ''),
                  'X': (MobileBy.ID, ''),
                  'Y': (MobileBy.ID, ''),
                  'Z': (MobileBy.ID, ''),
                  '#': (MobileBy.ID, '')
                  }

    @TestLogger.log()
    def get_group_name(self):
        """获取群名"""
        els = self.get_elements(self.__class__.__locators["群聊名"])
        group_names = []
        if els:
            for el in els:
                group_names.append(el.text)
        return group_names

    @TestLogger.log()
    def select_one_group_by_name(self, name):
        """通过群名选择一个群"""
        self.click_element((MobileBy.XPATH, '//*[@text ="%s"]' % name))

    @TestLogger.log()
    def click_back(self):
        """点击返回"""
        self.click_element(self.__class__.__locators['返回'])

    @TestLogger.log()
    def wait_for_page_load(self, timeout=8, auto_accept_alerts=True):
        """等待选择一个群页面加载"""
        try:
            self.wait_until(
                timeout=timeout,
                auto_accept_permission_alert=auto_accept_alerts,
                condition=lambda d: self._is_element_present(self.__class__.__locators["选择一个群"])
            )
        except:
            message = "页面在{}s内，没有加载成功".format(str(timeout))
            raise AssertionError(
                message
            )
        return self

    @TestLogger.log()
    def is_on_this_page(self):
        """当前页面是否在选择一个群"""
        el = self.get_elements(self.__locators['选择一个群'])
        if len(el) > 0:
            return True
        return False
