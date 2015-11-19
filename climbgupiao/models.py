#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class gupiaolist(models.Model):
    symbol = models.CharField(max_length=10,primary_key=True)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=15)
    sybk = models.CharField(max_length=15,default='未知') #所属板块
    current = models.FloatField(default=0) #当前价
    marketCapital = models.FloatField(default=0) #总市值
    pe_ttm = models.FloatField(default=0) #市盈率TTM是价格除以最近四个季度每股盈利计算的市盈率，这个是动态市盈率
    pe_lyr = models.FloatField(default=0) #市盈率LYR是价格除以上一年度每股盈利计算的静态市盈率，这个是静态市盈率
    pb = models.FloatField(default=0) #市净率，市净率表示你每股股票对应的公司的净资产的比，股价10元，市净率2.0就是说你花了10元，买到该上市公司5元的净资产。
    net_asset = models.FloatField(default=0) #√每股净资产,每股净资产= 股东权益÷总股本,每股净资产值越大，表明公司每股股票代表的财富越雄厚
    gjj = models.FloatField(default=0) #每股资本公积金,2015第三季度
    netprofit = models.FloatField(default=0)  #净利润
    dilutedroe = models.FloatField(default=0)  #主营业务收入增长率
    netincgrowrate = models.FloatField(default=0)  #净利润增长率
    totassgrowrate = models.FloatField(default=0)  #总资产增长率
    salegrossprofitrto = models.FloatField(default=0)  #销售毛利率,三季度平均值
    mainbusiincome = models.FloatField(default=0)  #主营业务收入,三季度平均值
    test1 = models.FloatField(default=0)  #test high52week
    test2 = models.FloatField(default=0)  #totalShares 总股本
    test3 = models.FloatField(default=0)  #三年股价增长
    test4 = models.FloatField(default=0)  #一年股价增长
    test5 = models.FloatField(default=0)  #test
    test6 = models.FloatField(default=0)  #test
    test7 = models.FloatField(default=0)  #每股资本公积金占股价
    test8 = models.FloatField(default=0)  #test  近三年股价增长率
    test9 = models.FloatField(default=0)  #test 2015年新上市
    test10 = models.FloatField(default=0)  #test  xueqiu
    netprofit_jd1 = models.FloatField(default=0)
    netprofit_jd2 = models.FloatField(default=0)
    netprofit_jd3 = models.FloatField(default=0)
    netprofit_nd1 = models.FloatField(default=0)
    netprofit_nd2 = models.FloatField(default=0)
    netprofit_nd3 = models.FloatField(default=0)
    shangshidays = models.IntegerField(max_length=5, default=0)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.symbol)

    primary = ('symbol', 'name')


class bankuailist(models.Model):
    name = models.CharField(max_length=15,primary_key=True)
    daima = models.CharField(max_length=15)

    def __unicode__(self):
        return u'%s %s' % (self.name, self.daima)
