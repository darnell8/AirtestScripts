# -*- encoding=utf8 -*-
__author__ = "PY"

from airtest.core.api import *
import random

auto_setup(__file__)


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# airtest.core.api中包含了一个名为ST的变量，即为全局设置
# 图片识别阈值，默认值0.7
ST.THRESHOLD_STRICT = 0.7  # assert_exists语句的默认阈值，一般比THRESHOLD更高一些
ST.THRESHOLD = 0.75  # 其他语句的默认阈值
# ST.SNAPSHOT_QUALITY = xxx  # 自定义全局截图的压缩精度[1, 99]
# ST.IMAGE_MAXSIZE = 600 # 设置截图尺寸不超过600*600，如果不设置，默认为原图尺寸
# ST.SAVE_IMAGE = False # 暂时关闭截图

IS_DEV_MODE = True
PACKAGE_NAME = "cn.mopon.film.zygj"

# 全局等待最小值、最大值
GLOBAL_SLEEP_MIN_SEC = 1
GLOBAL_SLEEP_MAX_SEC = 2

start_app(PACKAGE_NAME)
# sleep(20)

