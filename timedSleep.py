import os
import datetime
import argparse
import time
import sys

def getArgs():
    result={"hour":0,"min":0} #使用一个字典以存储参数
    parser = argparse.ArgumentParser(description="your script description") #实例化一个参数对象,描述参数为help内容
    parser.add_argument('--hour', type=int) #创建一个--hour参数,接收数据类型为int
    parser.add_argument('--min', type=int) #创建一个--min参数,接收数据类型为int
    args=parser.parse_args() #获得参数对象
    if args.hour or args.hour==0:
        result["hour"]=args.hour
    else:
        print("参数有误")
        quit()
    if args.min or args.min==0:
        result["min"]=args.min
    else:
        print("参数有误")
        quit()
    return result

def sleep_time(target_hour,target_minute):
    now_time = datetime.datetime.now()
    # now_time=datetime.datetime.now().strftime('%Y-%m-%d')
    hour=now_time.hour
    minute=now_time.minute
    second=now_time.second
    now_sum=hour*3600+minute*60+second
    target_sum=target_hour*3600+target_minute*60
    if target_sum<now_sum :
        target_sum+=24*3600
    result=target_sum-now_sum
    return result

def display(target):
    limit=30*60 #限制每行符号代表时间
    interval=60 #每个符号的间隔时间
    elapse=limit #先启用一行达到时间限制,打印预期耗时
    while True: #循环检测与显示时间剩余
        if elapse==limit: #如果一行达到时间限制则清除标记并计算显示
            elapse=0
            t_h=target//3600
            t_m=target%3600//60
            t_s=target%60
            print("System will sleep after :",t_h,"hour ",t_m,"minute ",t_s,"second!")
        if target>interval: #剩余时间大于间隔时间则打印间隔标记
            time.sleep(interval) #休眠间隔时间
            elapse+=interval #流逝时间计数
            print('I',end='')
            sys.stdout.flush() #刷新输出,否则上一行不立即显示
            target-=interval #修改剩余时间
        else: #剩余时间不满足间隔时间就执行完返回
            time.sleep(target)
            return

if __name__ == "__main__":
    try:
        args=getArgs() #读取时间参数
        target=sleep_time(args["hour"],args["min"]) #计算休眠时间
        display(target) #展示并执行过程
        cmd="shutdown /h" #Windows命令语句
        print(cmd)
        os.system(cmd) #执行休眠
    except Exception as e:
        print("程序意外停止!")
    