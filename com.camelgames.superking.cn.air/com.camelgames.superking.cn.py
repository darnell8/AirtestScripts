# -*- encoding=utf8 -*-
__author__ = "PY"
__title__ = "战火与秩序脚本"
__desc__ = """
战火与秩序WarAndOrder 5分钟脚本
测试点1
测试点2
测试点3
"""

from airtest.core.api import *
from airtest.cli.parser import cli_setup
import random

# ----------------------------------------设备信息----------------------------------------

# 自动连接Android设备
# 如果命令行不带参数
# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=[
#         "Android:///?cap_method=javacap&ori_method=adbori",
#     ])
# else:
#     auto_setup(__file__)

# 初始化默认参数 
auto_setup(__file__)


# dev1 = connect_device("Android://127.0.0.1:5037/serialno1")  # 连上第一台手机
# dev2 = connect_device("Android://127.0.0.1:5037/serialno2")  # 第二台手机
print(G.DEVICE_LIST)  # 此时设备列表为[dev1, dev2]

# 传入数字0切换当前操作的手机到第1台
# set_current(0)
# 切换当前操作的手机到序列号为serialno2的手机
# set_current("serialno2")

    
# 在Android中，有一个平台独有的接口list_app可以列出所有安装过的应用
dev = device()  # 先获取到当前设备对象，这里的dev即是一个Android对象
print(dev.get_display_info())  # 查看当前设备的显示信息
print("0.当前设备的显示信息: ^")
# print(dev.list_app())  # 然后就可以调用平台独有接口了

# 1.断言分辨率是否正常，如果没有缩放比对功能则启用
# if not (IS_DEV_MODE):
#     print("1.断言分辨率是否正常")
#     assert_equal("1080", dev.get_display_info()["width"])
#     assert_equal("1920", dev.get_display_info()["height"])


# ----------------------------------------默认设置----------------------------------------

# airtest.core.api中包含了一个名为ST的变量，即为全局设置
# 图片识别阈值，默认值0.7
ST.THRESHOLD_STRICT = 0.7  # assert_exists语句的默认阈值，一般比THRESHOLD更高一些
ST.THRESHOLD = 0.75  # 其他语句的默认阈值
# ST.SNAPSHOT_QUALITY = xxx  # 自定义全局截图的压缩精度[1, 99]
# ST.IMAGE_MAXSIZE = 600 # 设置截图尺寸不超过600*600，如果不设置，默认为原图尺寸
# ST.SAVE_IMAGE = False # 暂时关闭截图

IS_DEV_MODE = True
PACKAGE_NAME = "com.camelgames.superking.cn"

# 收集资源等待最小值、最大值
SHOUJIZIYUAN_SLEEP_MIN_SEC = 1
SHOUJIZIYUAN_SLEEP_MAX_SEC = 2

# 全局等待最小值、最大值
GLOBAL_SLEEP_MIN_SEC = 2
GLOBAL_SLEEP_MAX_SEC = 3

# ----------------------------------------X.通用方法----------------------------------------
# 返回游戏首页
def back_to_home():
    while not exists(exit_dialog):
        keyevent("BACK")
    keyevent("BACK")
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
# 点击列表内的任意一个图标
def touch_for_list(obj_list):
    for item in obj_list:
        if exists(item):
            touch(item)
            return True
            break
    return False

random_x_pixel = 10
random_y_pixel = 10
# 生成坐标附近的随机位置
def generate_random_tuple(temp_tup):
    return (random.randint(temp_tup[0]-random_x_pixel, temp_tup[0]+random_x_pixel), 
            random.randint(temp_tup[1]-random_y_pixel, temp_tup[1]+random_y_pixel))

# ----------------------------------------2.进入游戏----------------------------------------
print("2.进入游戏: " + PACKAGE_NAME)
start_app(PACKAGE_NAME)
# sleep(20)

# ----------------------------------------3.收集资源----------------------------------------
wood_bubble = Template(r"木材气泡2.png", record_pos=(-0.078, 0.131), resolution=(540, 960))
grain_bubble = Template(r"粮食气泡2.png", record_pos=(0.183, -0.046), resolution=(540, 960))

# 函数：收集资源
def collect_resources_by_touch(v):
    while exists(v):
        touch(v)
        sleep(random.uniform(SHOUJIZIYUAN_SLEEP_MIN_SEC, SHOUJIZIYUAN_SLEEP_MAX_SEC))
        
def collect_resources_by_shake(v):
    # 摇晃手机 adb shell input keyevent KEYCODE_CAMERA
    keyevent("CAMERA")


print("3.收集资源 ^")
# 木材
# collect_resources_by_touch(wood_bubble)
# 粮食
# collect_resources_by_touch(grain_bubble)
# TODO 石料 铁矿

# ----------------------------------------4.出城操作----------------------------------------
exit_dialog = Template(r"退出游戏提示.png", record_pos=(0.0, 0.004), resolution=(540, 960))
outtown_confirm_button = Template(r"出城按钮.png", threshold=0.8, target_pos=4, record_pos=(-0.313, 0.83), resolution=(540, 960))
outtown_search_button = Template(r"城外查找按钮.png", record_pos=(0.42, 0.52), resolution=(540, 960))
farm_button = Template(r"农庄.png", record_pos=(-0.415, 0.569), resolution=(540, 960))
farm_night_button = Template(r"农庄晚.png", record_pos=(-0.417, 0.57), resolution=(540, 960))
plant_button = Template(r"储木厂2.png", record_pos=(-0.265, 0.569), resolution=(540, 960))
plant_night_button = Template(r"储木厂晚.png", record_pos=(-0.269, 0.563), resolution=(540, 960))
stone_button = Template(r"储石场.png", record_pos=(-0.111, 0.572), resolution=(540, 960))
stone_night_button = Template(r"储石厂晚.png", record_pos=(-0.113, 0.569), resolution=(540, 960))
refinery_button = Template(r"精炼厂.png", record_pos=(0.039, 0.574), resolution=(540, 960))
refinery_night_button = Template(r"精炼厂晚.png", record_pos=(0.041, 0.567), resolution=(540, 960))
gemstone_button = Template(r"宝石矿洞.png", record_pos=(0.181, 0.569), resolution=(540, 960))
gemstone_night_button = Template(r"宝石矿洞晚.png", record_pos=(0.185, 0.572), resolution=(540, 960))
monster_night_button = Template(r"怪物晚.png", record_pos=(0.333, 0.565), resolution=(540, 960))
monster2_button = Template(r"精英怪2.png", target_pos=6, record_pos=(0.311, 0.565), resolution=(540, 960))
monster2_night_button = Template(r"精英怪晚.png", record_pos=(0.307, 0.57), resolution=(540, 960))
sally_button = Template(r"出击按钮.png", record_pos=(0.341, 0.804), resolution=(540, 960))
level_add_button = Template(r"增加等级.png", record_pos=(0.122, 0.806), resolution=(540, 960))
collect_button = Template(r"收集按钮.png", record_pos=(0.146, -0.165), resolution=(540, 960))
attack_button = Template(r"出发按钮.png", record_pos=(0.339, 0.806), resolution=(540, 960))
speed_up_button = Template(r"行军加速按钮.png", record_pos=(-0.304, -0.561), resolution=(540, 960))

outtown_confirm_pixel = (53, 908)
outtown_search_pixel = (500, 752)
farm_pixel = (44, 784)
plant_pixel = (129, 784)
stone_pixel = (208, 784)
refinery_pixel = (291, 784)
gemstone_pixel = (369, 784)
monster_pixel = (448, 784)
monster2_pixel = (525, 784)
level_add_pixel = (336, 913)
sally_pixel = (454, 909)
collect_pixel = (384, 426)
attack_pixel = (455, 915)
def goto_outtown_by_pixel(target_name, level):
    back_to_home()
    
    touch(generate_random_tuple(outtown_confirm_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    touch(generate_random_tuple(outtown_search_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    if target_name == "农庄":
        touch(generate_random_tuple(farm_pixel))
    elif target_name == "储木厂":
        touch(generate_random_tuple(plant_pixel))
    elif target_name == "储石场":
        touch(generate_random_tuple(stone_pixel))
    elif target_name == "精炼厂":
        touch(generate_random_tuple(refinery_pixel))
    elif target_name == "宝石矿洞":
        touch(generate_random_tuple(gemstone_pixel))
    elif target_name == "怪物":
        touch(generate_random_tuple(monster_pixel))
    elif target_name == "精英怪":
        touch(generate_random_tuple(monster2_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    touch(generate_random_tuple(level_add_pixel), times=level-1)
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    touch(generate_random_tuple(sally_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
#     touch(collect_button) # 由于图片识别率不高，改用坐标定位
#     touch((384, 426))
    touch(generate_random_tuple(collect_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    # 点击第一次退出面板，第二次才会进入选择军队界面
    touch(generate_random_tuple(collect_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    touch(generate_random_tuple(attack_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))

# 采集地点、采集等级、几级骑兵、操作、是否捐献、自动升级、加速
def goto_outtown(target_name, level):
    back_to_home()
    
    touch(outtown_confirm_button)
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    touch(outtown_search_button)
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    if target_name == "农庄":
        touch_for_list([farm_button, farm_night_button])
    elif target_name == "储木厂":
        touch_for_list([plant_button, plant_night_button])
    elif target_name == "储石场":
        touch_for_list([stone_button, stone_night_button])
    elif target_name == "精炼厂":
        touch_for_list([refinery_button, refinery_night_button])
    elif target_name == "宝石矿洞":
        touch_for_list([gemstone_button, gemstone_night_button])
    elif target_name == "怪物":
        touch_for_list([monster_night_button, monster_night_button])
    elif target_name == "精英怪":
        touch_for_list([monster2_button, monster2_night_button])
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    touch(level_add_button, times=level-1)
    
    touch(sally_button)
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
#     touch(collect_button) # 由于图片识别率不高，改用坐标定位
#     touch((384, 426))
    touch(generate_random_tuple(collect_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    # 点击第一次退出面板，第二次才会进入选择军队界面
    touch(generate_random_tuple(collect_pixel))
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    touch(attack_button)
    sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
    
    
# goto_outtown("农庄", 2)
# goto_outtown_by_pixel("农庄", 2)

# ----------------------------------------X.自动完成任务----------------------------------------
mission_enter_button = Template(r"任务入口.png", record_pos=(-0.43, 0.426), resolution=(540, 960))
mission_continue_button = Template(r"前往任务.png", record_pos=(0.307, -0.172), resolution=(540, 960))
mission_continue_button2 = Template(r"前往任务2.png", record_pos=(0.306, -0.054), resolution=(540, 960))
mission_skip_button = Template(r"对话跳过按钮.png", record_pos=(0.396, -0.837), resolution=(540, 960))
mission_point_to_button = Template(r"任务指引.png", record_pos=(0.017, 0.219), resolution=(540, 960))
mission_complete_button = Template(r"领取任务奖励.png", record_pos=(0.306, -0.17), resolution=(540, 960))

def complete_missions():
    back_to_home()
    
    while exists(mission_enter_button):
        touch(mission_enter_button)
        sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
        
        while exists(mission_continue_button):
            touch(mission_continue_button)
            sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
            
            if exists(mission_skip_button):
                touch(mission_skip_button)
                
            while exists(mission_point_to_button):
                touch(mission_point_to_button)
            keyevent("BACK")
                    
        while exists(mission_continue_button2):
            touch(mission_continue_button2)
            sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
            
            if exists(mission_skip_button):
                touch(mission_skip_button)
                
            while exists(mission_point_to_button):
                touch(mission_point_to_button)
            keyevent("BACK")
                    
        while exists(mission_complete_button):
            touch(mission_complete_button)
            sleep(random.uniform(GLOBAL_SLEEP_MIN_SEC, GLOBAL_SLEEP_MAX_SEC))
        keyevent("BACK")

        sleep(random.uniform(5, 6))
                    
complete_missions()

# ----------------------------------------X.每日奖励----------------------------------------
daily_reward_button = Template(r"领取奖励.png", record_pos=(0.0, 0.428), resolution=(540, 960))
def close_daily_rewards():
    if exists(daily_reward_button):
        touch(daily_reward_button)
        
# ----------------------------------------X.新手特惠----------------------------------------
newbie_special = Template(r"新手特惠.png", record_pos=(-0.041, -0.463), resolution=(540, 960))
dialog_close_button = Template(r"关闭按钮.png", record_pos=(0.402, -0.461), resolution=(540, 960))
def close_newbie_specials():
    if exists(newbie_special):
        touch(dialog_close_button)
        
# ----------------------------------------X.城堡建设礼包----------------------------------------
castle_building_pack = Template(r"城堡建设礼包.png", record_pos=(-0.041, -0.463), resolution=(540, 960))
def close_newbie_specials():
    if exists(castle_building_pack):
        touch(dialog_close_button)

# ----------------------------------------X.至尊月卡----------------------------------------
monthly_card = Template(r"购买按钮.png", record_pos=(-0.006, 0.648), resolution=(540, 960))
dialog_close_button2 = Template(r"关闭按钮2.png", record_pos=(0.426, -0.587), resolution=(540, 960))
def close_supreme_monthly_card():
    if exists(monthly_card):
        touch(dialog_close_button2)

