#!/usr/bin/env python3
# !-*- coding:utf-8 -*-

"""
演示如何抓取学信网
"""

import time

from selenium import webdriver


def get_sub_regions(browser, url):
    # 登录页面
    browser.get(url)
    # 输入用户名
    elem = browser.find_element_by_id('username')
    elem.clear()
    elem.send_keys('995443908@qq.com')
    elem = browser.find_element_by_id('password')
    # 输入密码
    elem.clear()
    elem.send_keys('shen86312971')
    # 点击登录
    elem = browser.find_element_by_xpath('//input[@class=\"btn_login btn_login_my\"]')
    elem.click()
    # 点击进入查看页面
    time.sleep(5)
    elem = browser.find_element_by_xpath('//a[@class=\"login-btn\"]')
    elem.click()
    # 高等教育信息
    time.sleep(5)
    elem = browser.find_element_by_xpath('//a[@href=\"gdjy/xj/show.action\"]')
    elem.click()
    # 样例查询
    time.sleep(5)
    # elem = browser.find_element_by_xpath('//div[@class=\"main\"]')
    elems = browser.find_elements_by_xpath('//div[@class=\"m-left xj-left main-block border-shadow\"]')
    for i in elems:
        print(i.text)


def main():
    # 启动浏览器
    browser = webdriver.Chrome()
    # 登录学信网
    sh_business_regions = get_sub_regions(browser,'https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check')


if __name__ == '__main__':
    main()
