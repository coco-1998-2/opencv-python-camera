#-*-coding:utf-8-*-

def mkdir(path):
    # 引入模块
    import os
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+'images文件夹创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+'images文件夹已存在')
        return False