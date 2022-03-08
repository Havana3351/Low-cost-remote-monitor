from flask_restful import Resource, request
import json
import os
#测试时间用
import datetime
import pymysql

class VideoSaveData(Resource):

    def get(self):
        pass

    def post(self):

        # if request.form.get('recorddate') and request.form.get('recordminute'):
        if((request.get_json())['recorddate'] and (request.get_json())['recordminute'] and (request.get_json())['username']):

            #获得数据并处理成2020(int),0402(int)的形式
            # data = request.form.to_dict()
            # date = data.get('recorddate')
            date = (request.get_json())['recorddate']
            datetemp = date.split(",")
            startdate = datetemp[0].split("-")
            enddate = datetemp[1].split("-")

            startyear = int(startdate[0])
            startday = int(startdate[1] + startdate[2])
            endyear = int(enddate[0])
            endday = int(enddate[1] + enddate[2])
            # 输出时间测试
            print("start: " + datetime.datetime.now().strftime('%H:%M:%S.%f'))

            minute = (request.get_json())['recordminute']
            #minute = data.get('recordminute')
            minutetemp = minute.split(",")
            start = minutetemp[0].split(':')
            end = minutetemp[1].split(':')
            
            startminute = int(start[0] + start[1])
            endminute = int(end[0] + end[1])

            #取得设备名
            username = (request.get_json())['username']
            print(username)
            db = pymysql.connect("rm-2ze61i7u6d7a3fwp9yo.mysql.rds.aliyuncs.com", "team", "Aaa5225975", "pidata")
            cursor = db.cursor()

            sql1 = "select rpiname from user where username=\'" + username + "\'"#可能存在类型问题
            cursor.execute(sql1)
            row1 = cursor.fetchone()

            if not row1:
                rpiname = None
            rpiname = str(row1[0])
            print(rpiname)

            #获取宿舍地址
            sql2 = "select dorm from user where username=\'" + username + "\'"  # 可能存在类型问题
            cursor.execute(sql2)
            row2 = cursor.fetchone()

            if not row2:
                dorm = None
            dorm = str(row2[0])

            #对os.walk(rootpath)下所有结果的收集以及提取需要的列表作为collect
            collectroot = []
            collect = []
            rootpath = r'/root/video/%s' % (rpiname)

            for dirs in os.walk(rootpath):
                time = dirs
                collectroot.append(time)
            #输出时间测试
            print("os.walk: " + datetime.datetime.now().strftime('%H:%M:%S.%f'))

            for menber in collectroot:
                print(menber[1])
                collect.append(menber[1])

            #输出时间测试
            print("sort and append: " + datetime.datetime.now().strftime('%H:%M:%S.%f'))

            #初始化返回用的字典result
            result = {}
            resultlist = []
            #初始化输出各列表和列表指针
            datapointer = 1
            yearlist = collect[0]
            daylist = None
            timelist = None
            yearpointer = 0
            daypointer = None
            timepointer = None
            # 进行加入操作的许可
            permission = False


            while (True):

                # 初始化daypointer
                if (daypointer is None):
                    # 若年份文件夹下不为空
                    if (len(collect[datapointer]) != 0):
                        daylist = collect[datapointer]
                        daypointer = 0
                        datapointer += 1
                    else:
                        datapointer += 1
                        yearpointer += 1
                        continue

                # 初始化timepointer
                if (timepointer is None):
                    # 若日文件夹下不为空
                    if (len(collect[datapointer]) != 0):
                        timelist = collect[datapointer]
                        timepointer = 0
                        datapointer += 1
                    else:
                        datapointer += 1
                        daypointer += 1
                        continue

                #由指针指向的时间是否在需求时间内发放permission
                #年份大等于开始年份
                if (int(yearlist[yearpointer]) >= startyear):
                    #年份为开始年份
                    if (int(yearlist[yearpointer]) == startyear):
                        #筛选年份相同
                        if(startyear == endyear):
                            if(int(daylist[daypointer]) >= startday):
                                #日期等于开始日期
                                if(int(daylist[daypointer]) == startday):
                                    #筛选日期相同
                                    if(startday == endday):
                                        #大于开始时间
                                        if(int(timelist[timepointer]) >= startminute):
                                            if(int(timelist[timepointer]) <= endminute):
                                                permission = True
                                            #超出结束时间，停止读取数据
                                            else:
                                                permission = False
                                                #break
                                        else:
                                            permission = False
                                    #筛选日期不同
                                    else:
                                        #时间大等于开始时间
                                        if(int(timelist[timepointer]) >= startminute):
                                            permission = True
                                        else:
                                            permission = False

                                #日期不等于开始日期但小于结束日期（筛选日期不同）
                                elif(int(daylist[daypointer]) <= endday):
                                    #日期等于结束日期
                                    if(int(daylist[daypointer]) == endday):
                                        if(int(timelist[timepointer]) <= endminute):
                                            permission = True
                                        else:
                                            permission = False
                                            #超过最后一天的时间范围可以退出
                                            #break
                                    #日期小于结束日期
                                    else:
                                        permission = True

                                #日期大于开始日期但在范围外，退出
                                else:
                                    permission = False
                                    #break

                            #日期小于开始日期
                            else:
                                permission = False
                        #筛选年份不同
                        else:
                            #是否在开始日期之后
                            if(int(daylist[daypointer]) >= startday):
                                #是否为开始日期
                                if(int(daylist[daypointer]) == startday):
                                    #是否在开始时间之后
                                    if(int(timelist[timepointer]) >= startminute):
                                        permission = True
                                    else:
                                        permission = False
                                #在开始日期之后
                                else:
                                    permission = True
                            #在开始日期之前
                            else:
                                permission = False

                    #年份大于开始年份且小等于结束年份
                    elif (int(yearlist[yearpointer]) <= endyear):
                        #年份为结束年份
                        if(int(yearlist[yearpointer]) == endyear):
                            #在结束日期的范围内
                            if(int(daylist[daypointer]) <= endday):
                                #为结束年份的结束日期
                                if(int(daylist[daypointer]) == endday):
                                    #在结束时间之前
                                    if(int(timelist[timepointer]) <= endminute):
                                        permission = True
                                    #超过最后一天的时间范围可以退出
                                    else:
                                        permission = False
                                        #break
                                #在范围内且非结束日期
                                else:
                                    permission = True
                            #为结束年份而在结束日期的范围外
                            else:
                                permission = False
                                #break
                        #年份不为结束年份
                        else:
                            permission = True

                    #年份大于开始年份但不在范围内
                    else:
                        permission = False
                        #break
                #年份小于开始年份（不在范围内）
                else:
                    permission = False

                #输出时间测试
                print("if opreation: " + datetime.datetime.now().strftime('%H:%M:%S.%f'))

                #根据permission判定是否将数据归入result
                if (permission):
                    # 不需要初始化则直接获取数据
                    # 初始化本次的取值字典
                    arrange = {}

                    # 将0402改装为-04-02
                    daystringlist = list(daylist[daypointer])
                    daystringlist.insert(0, '-')
                    daystringlist.insert(3, '-')
                    daystring = ''.join(daystringlist)

                    # 设置返回值json中第n个time（'timen'）下'date'的值
                    arrange['date'] = str(yearlist[yearpointer]) + daystring
                    arrange['time'] = str(timelist[timepointer])
                    arrange['name'] = username
                    arrange['address'] = dorm

                    print(arrange)

                    resultlist.append(arrange)

                # 指针数据的改变
                timepointer += 1
                datapointer += 1

                # 若time指针超出timelist，则将pointer与list全部归空，重新进行初始化,并读下一个日期
                if (timepointer + 1 > len(timelist)):
                    timepointer = None
                    timelist = None
                    daypointer += 1
                    # 若day指针超出daylist，则将则将pointer与list全部归空，重新进行初始化,并读下一个年份
                    if (daypointer + 1 > len(daylist)):
                        daypointer = None
                        daylist = None
                        yearpointer += 1
                        #若year指针超出yearlist，则退出循环
                        #在上方超出endday作出break后下面的break已经失去作用
                        if (yearpointer + 1 > len(yearlist)):
                            break

            # 输出时间测试
            print("while opreation: " + datetime.datetime.now().strftime('%H:%M:%S.%f'))
            #重新排序
            result['tables'] = sorted(resultlist, key=lambda i: (i['date'], i['time']))

            # 循环结束，结果json化
            print(json.dumps(result))

            return json.dumps(result)

        else:
            print('error')
            return "error"





