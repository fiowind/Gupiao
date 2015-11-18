#!/usr/bin/python
#coding=utf-8


from models import gupiaolist
import urllib2, httplib, urlparse
import re, os, json

# import sqlite3 as dbapi
# con = dbapi.connect('db.sqlite3')
# con.text_factory = str
# fin = open("./output_action.txt", mode='r')
# data = fin.read()
fout = open("./output_action.txt", mode='w')

# reg = re.compile(r'每股公积金\(元\)</span></td><td class="tips-data-Right"><span>(.*?)</span>')
# codes = reg.findall(data)
# # print data
# print codes
# for code in codes:
#     print code

# fin.close


def totalDM():
    url = 'http://bbs.10jqka.com.cn/codelist.html'
    req = urllib2.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
    try:
        res = urllib2.urlopen(req)
        print 'ok1'
    except Exception, e:
        raise e
    html = res.read()
    reg = re.compile(r'<li><a href="http://bbs.10jqka.com.cn/(.*?),.*?>(.*?) (\d*?)</a></li>')
    codes = reg.findall(html)

    for code in codes:
        print code[1].decode('gb2312')
        gupiao = gupiaolist.objects.get(symbol=code[0]+code[2])
        gupiao.name = code[1].decode('gb2312')
        gupiao.save()

def totalDM2():
    for i in range(10):
        c = str(i+1)
        url = 'http://data.10jqka.com.cn/ipo/xgsgyzq/board/cyb/field/SGDATE/page/'+c+'/order/desc/ajax/1/'
        print url
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        try:
            res = urllib2.urlopen(req)
            print 'ok1'
        except Exception, e:
            raise e
        html = res.read()
        reg = re.compile(r'class="blue" target="_blank">(30.\d*?)</a>')
        codes = reg.findall(html)
        for code in codes:
            print code
            gupiao = gupiaolist(symbol='sz'+code, code=code, test9=1)
            gupiao.save()
    for i in range(5):
        c = str(i+1)
        url = 'http://data.10jqka.com.cn/ipo/xgsgyzq/board/hszb/field/SGDATE/page/'+ c +'/order/desc/ajax/1/'
        print url
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        try:
            res = urllib2.urlopen(req)
            print 'ok1'
        except Exception, e:
            raise e
        html = res.read()
        reg = re.compile(r'class="blue" target="_blank">(30.\d*?)</a>')
        codes = reg.findall(html)
        for code in codes:
            print code
            gupiao = gupiaolist(symbol='sh'+code, code=code, test9=1)
            gupiao.save()
    for i in range(12):
        c = str(i+1)
        url = 'http://data.10jqka.com.cn/ipo/xgsgyzq/board/zxb/field/SGDATE/page/'+c+'/order/desc/ajax/1/'
        print url
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        try:
            res = urllib2.urlopen(req)
            print 'ok1'
        except Exception, e:
            raise e
        html = res.read()
        reg = re.compile(r'class="blue" target="_blank">(30.\d*?)</a>')
        codes = reg.findall(html)
        for code in codes:
            print code
            gupiao = gupiaolist(symbol='sz'+code, code=code, test9=1)
            gupiao.save()


def fangkong(str):
    if str == '' or str is None:
        return 0.0
    else:
        return str


def xueqiu():
    Gupiaolist = gupiaolist.objects.filter(test10=0)
    for gupiao in Gupiaolist:
        print gupiao.symbol
        url = 'http://xueqiu.com/v4/stock/quote.json?code=' + gupiao.symbol + '&_=1447660947532'
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        req.add_header("Cookie", "s=18wd1ctj06; bid=7dc18ce8a8b5d0fb872b756e46a961c8_igz5gk95; snbim_minify=true; last_account=zfx1226%40163.com; xq_a_token=b6008ac7be5f9a5386e65964ba1f3738111eea48; xq_r_token=6578cf2d69723f9da6f5c67809b90e68c29d52ca; __utmt=1; __utma=1.1148970814.1447506729.1447665270.1447693198.10; __utmb=1.1.10.1447693198; __utmc=1; __utmz=1.1447506729.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1447506729; Hm_lpvt_1db88642e346389874251b5a1eded6")
        try:
            res = urllib2.urlopen(req)
            print 'ok1'
        except Exception, e:
            print e
            fout.write(gupiao.symbol+'\n')
            continue
        html = res.read()
        jsonVal = json.loads(html)
        # print jsonVal[gupiao.symbol.upper()]['current']
        gupiao = gupiaolist(symbol=gupiao.symbol, name=fangkong(jsonVal[gupiao.symbol.upper()]['name']), current=fangkong(jsonVal[gupiao.symbol.upper()]['current']), code=fangkong(jsonVal[gupiao.symbol.upper()]['code']), test1=fangkong(jsonVal[gupiao.symbol.upper()]['high52week']), marketCapital=fangkong(jsonVal[gupiao.symbol.upper()]['marketCapital']), pe_ttm=fangkong(jsonVal[gupiao.symbol.upper()]['pe_ttm']), pe_lyr=fangkong(jsonVal[gupiao.symbol.upper()]['pe_lyr']), pb=fangkong(jsonVal[gupiao.symbol.upper()]['pb']), net_asset=fangkong(jsonVal[gupiao.symbol.upper()]['net_assets']), test2=fangkong(jsonVal[gupiao.symbol.upper()]['totalShares']), test10 = '1')
        gupiao.save()


def caiwu():
    Gupiaolist = gupiaolist.objects.filter(test10=1,test7=0)
    for gupiao in Gupiaolist:
        print gupiao.symbol
        url = 'http://xueqiu.com/stock/f10/finmainindex.json?symbol='+ gupiao.symbol +'&page=1&size=30&_=1447754364227';
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        req.add_header("Cookie", "s=18wd1ctj06; bid=7dc18ce8a8b5d0fb872b756e46a961c8_igz5gk95; snbim_minify=true; last_account=zfx1226%40163.com; xq_a_token=b6008ac7be5f9a5386e65964ba1f3738111eea48; xq_r_token=6578cf2d69723f9da6f5c67809b90e68c29d52ca; __utmt=1; __utma=1.1148970814.1447506729.1447665270.1447693198.10; __utmb=1.1.10.1447693198; __utmc=1; __utmz=1.1447506729.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; Hm_lvt_1db88642e346389874251b5a1eded6e3=1447506729; Hm_lpvt_1db88642e346389874251b5a1eded6")
        try:
            res = urllib2.urlopen(req)
            print 'ok1'
        except Exception, e:
            print e
            print 'notok'
            fout.write('1'+gupiao.symbol+'\n')
            continue
        html = res.read()
        jsonVal = json.loads(html)
        # print jsonVal['list'][0]['salegrossprofitrto']
        try:
            salegrossprofitrto = float(fangkong(jsonVal['list'][0]['salegrossprofitrto'])+fangkong(jsonVal['list'][1]['salegrossprofitrto'])+fangkong(jsonVal['list'][2]['salegrossprofitrto']))/3
            netprofit_jd1 = fangkong(jsonVal['list'][0]['netincgrowrate'])
            netprofit_jd2 = fangkong(jsonVal['list'][1]['netincgrowrate'])
            netprofit_jd3 = fangkong(jsonVal['list'][2]['netincgrowrate'])
            netprofit_nd1 = fangkong(jsonVal['list'][0]['netincgrowrate'])
            netprofit_nd2 = fangkong(jsonVal['list'][3]['netincgrowrate'])
            netprofit_nd3 = fangkong(jsonVal['list'][7]['netincgrowrate'])
            dilutedroe = float(fangkong(jsonVal['list'][0]['mainbusincgrowrate']) + fangkong(jsonVal['list'][1]['mainbusincgrowrate']) + fangkong(jsonVal['list'][2]['mainbusincgrowrate']))/3
            mainbusiincome = float(fangkong(jsonVal['list'][0]['mainbusiincome']) + fangkong(jsonVal['list'][1]['mainbusiincome']) + fangkong(jsonVal['list'][2]['mainbusiincome']))/3
        except Exception, e:
            print e
            fout.write('2'+gupiao.symbol+'\n')
            continue
        gupiao = gupiaolist.objects.get(symbol = gupiao.symbol)
        gupiao.salegrossprofitrto = salegrossprofitrto
        gupiao.netprofit_jd1 = netprofit_jd1
        gupiao.netprofit_jd2 = netprofit_jd2
        gupiao.netprofit_jd3 = netprofit_jd3
        gupiao.netprofit_nd1 = netprofit_nd1
        gupiao.netprofit_nd2 = netprofit_nd2
        gupiao.netprofit_nd3 = netprofit_nd3
        gupiao.dilutedroe = dilutedroe
        gupiao.mainbusiincome = mainbusiincome
        gupiao.test7 = 1.0
        gupiao.save()
        # break

        # gupiao.save()


def dongcai():
    Gupiaolist = gupiaolist.objects.filter(test10=1,gjj=0)
    for gupiao in Gupiaolist:
        url = 'http://f10.eastmoney.com/f10_v2/FinanceAnalysis.aspx?code=' + gupiao.symbol
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        try:
            res = urllib2.urlopen(req)
            print gupiao.symbol
        except Exception, e:
            print e
            print 'notok'
            fout.write('1'+gupiao.symbol+'\n')
            continue
        html = res.read()
        # print html
        # fout.write(html)
        #大师傅
        reg = re.compile(r'每股公积金\(元\)</span></td><td class="tips-data-Right"><span>(.*?)</span>')
        codes = reg.findall(html)
        if codes:
            try:
                gupiao = gupiaolist.objects.get(symbol=gupiao.symbol)
                gupiao.gjj = codes[0]
                gupiao.save()
                print 'ok'
            except Exception,e:
                fout.write(u'%s %s \n' % (gupiao.symbol, e))
                continue


def sohuzhangfu():
    Gupiaolist = gupiaolist.objects.filter(test10=1)
    for gupiao in Gupiaolist:
        url = 'http://q.stock.sohu.com/hisHq?code=cn_'+gupiao.code+'&start=20131031&end=20151117&stat=1&order=D&period=m&callback=historySearchHandler&rt=jsonp&r=0.9727671290747821&0.9856262989342213'
        req = urllib2.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0")
        try:
            res = urllib2.urlopen(req)
            print gupiao.symbol
        except Exception, e:
            print e
            print 'notok'
            fout.write('openerror'+gupiao.symbol+'\n')
            fout.write(e+'\n')
            continue
        html = res.read().decode('gb2312')
        x = html.index(u'累计')
        y = html.index(')')
        sStr1 = html[x+5:y-1].replace('"','').split(',')
        print sStr1
        break
        # jsonVal = json.loads(sStr1.decode('gb2312'))
        # print jsonVal
        # print jsonVal['stat']
        # print jsonVal[0]['stat']

# totalDM()
# totalDM2()
caiwu()
# xueqiu()
# dongcai()
# sohuzhangfu()
fout.close()
