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
PACKAGE_NAME = "com.wandafilm.app"

# 全局等待最小值、最大值
GLOBAL_SLEEP_MIN_SEC = 1
GLOBAL_SLEEP_MAX_SEC = 2

start_app(PACKAGE_NAME)
# sleep(20)

# ----------------------------------------点击首页按钮----------------------------------------
home_page_button = poco("com.wandafilm.app:id/tabBar").child("android.widget.LinearLayout").child("android.widget.FrameLayout")[0].wait()
home_page_button.click()
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# ----------------------------------------进入搜索----------------------------------------
# search_text_view = poco("android.widget.FrameLayout").child("android.widget.LinearLayout").offspring("com.wandafilm.app:id/container").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.LinearLayout")[0].child("android.widget.TextView")[0].wait()
search_text_view = poco(text="搜索影片、影城、影人、资讯").wait()
search_text_view.click()
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# ----------------------------------------输入搜索----------------------------------------
search_edit_text = poco("com.wandafilm.app:id/searchView").wait()
# search_edit_text.set_text("长安两万里")
# keyevent("ENTER")
search_edit_text.click()
text("长安两万里", search=True)
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# ----------------------------------------选择购票----------------------------------------
buy_ticket_button = poco("com.wandafilm.app:id/movieTicketTv").wait()
buy_ticket_button.click()
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# ----------------------------------------选择时间----------------------------------------
# 选择明天的门票
today_tab = poco(textMatches="今天.*").wait()
tomorrow_tab = poco(textMatches="明天.*").wait()
acquired_tab = poco(textMatches="后天.*").wait()
tomorrow_tab.click()
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# ----------------------------------------进入影院----------------------------------------
cinema_button = poco("com.wandafilm.app:id/recyclerView").child("android.widget.LinearLayout").wait()
cinema_button.click()
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# 打印时间
date_text_list = poco("com.wandafilm.app:id/opening_time").wait()
for index in range(len(date_text_list)):
    log("date time: " + date_text_list[index].get_text())
    log("price:     " + poco("com.wandafilm.app:id/sales_price")[index].get_text())

# 选择第二场购票
comfirm_ticket_button = poco("com.wandafilm.app:id/buy_btn")[1].wait()
comfirm_ticket_button.click()
sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
