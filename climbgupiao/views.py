#-*- coding: UTF-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import gupiaolist,bankuai,bankuailist

def compare_result(list1,list2):
    cs =[]
    for a in list1:
        if a in list2:
            cs.append(a)
    return cs


def codesearch(req):
    if req.method == 'POST':
        gupiaos = []
        bankuais = []
        gid = req.POST.get('gid') if req.POST.get('gid') else False
        if gid:
            gupiaos = gupiaolist.objects.filter(code=gid)
        if gupiaos:
            bankuais = bankuailist.objects.filter(code = gupiaos[0].code)
            print bankuais

        return render_to_response('result.html',
                                  {'gupiaolist': gupiaos,
                                   'bankuais':bankuais,
                                   },
                                  context_instance=RequestContext(req))
def ajaxlist(req):
    if req.method == 'POST':
        gupiaos = []
        havelist = False
        print req.POST
        # data = dict(request.GET._iterlists())
        for key, bk_name in req.POST.iteritems():
            print bk_name
            bankuais = bankuailist.objects.filter(bankuai_name = bk_name)
            print len(bankuais)
            if gupiaos or havelist:
                gupiaos_tmp = []
                for bankuai in bankuais:
                    code = bankuai.code
                    gp = gupiaolist.objects.filter(code=code)
                    if(gp):
                        gupiaos_tmp.append(gp[0])
                if gupiaos_tmp:
                    gupiaos = compare_result(gupiaos,gupiaos_tmp)
            else:
                for bankuai in bankuais:
                    code = bankuai.code
                    gp = gupiaolist.objects.filter(code=code)
                    if(gp):
                        gupiaos.append(gp[0])
                if gupiaos:
                    havelist = True
                # print gupiaos
            print gupiaos
        return render_to_response('ajaxlist.html',
                                  {'gupiaolist': gupiaos,
                                   },
                                  context_instance=RequestContext(req))
def search(req):
    if req.method == 'POST':
        gupiaos = []
        v1 = req.POST.get('v1') if req.POST.get('v1') else False
        v4 = req.POST.get('v4') if req.POST.get('v4') else False
        v2 = req.POST.get('v2') if req.POST.get('v2') else False
        v3 = req.POST.get('v3') if req.POST.get('v3') else False
        v5 = req.POST.get('v5') if req.POST.get('v5') else False
        v6 = req.POST.get('v6') if req.POST.get('v6') else False
        v7 = req.POST.get('v7') if req.POST.get('v7') else False
        v8 = req.POST.get('v8') if req.POST.get('v8') else False
        v9 = req.POST.get('v9') if req.POST.get('v9') else False
        v10 = req.POST.get('v10') if req.POST.get('v10') else False


        if v1:
            vp1 = req.POST.get('vp1') if req.POST.get('vp1') else 50.0
            gupiaos = gupiaolist.objects.filter(pe_ttm__lte=vp1, pe_ttm__gt=0)
            # for gupiao in gupiaos:
            #     print gupiao.code
        if v2:
            vp2 = req.POST.get('vp2') if req.POST.get('vp2') else 25.0
            if gupiaos:
                gupiaos = gupiaos.filter(netprofit_jd1__gt=vp2, netprofit_jd2__gt=vp2, netprofit_jd3__gt=vp2)
            else:
                gupiaos = gupiaolist.objects.filter(netprofit_jd1__gt=vp2, netprofit_jd2__gt=vp2, netprofit_jd3__gt=vp2)
        if v3:
            vp3 = req.POST.get('vp3') if req.POST.get('vp3') else 25.0
            if gupiaos:
                gupiaos = gupiaos.filter(netprofit_nd1__gt=vp3, netprofit_nd2__gt=vp3, netprofit_nd3__gt=vp3)
            else:
                gupiaos = gupiaolist.objects.filter(netprofit_nd1__gt=vp3, netprofit_nd2__gt=vp3, netprofit_nd3__gt=vp3)

        if v4:
            vp4 = req.POST.get('vp4') if req.POST.get('vp4') else 1000.0
            # print vp4
            vp4 = float(vp4)*100000000
            if gupiaos:
                gupiaos = gupiaos.filter(marketCapital__lte=vp4, marketCapital__gt=0)
            else:
                gupiaos = gupiaolist.objects.filter(marketCapital__lte=vp4, marketCapital__gt=0)
        if v5:
            vp5 = req.POST.get('vp5') if req.POST.get('vp5') else 10
            if gupiaos:
                gupiaos = gupiaos.filter(test7__gt = vp5)
            else:
                gupiaos = gupiaolist.objects.filter(test7__gt = vp5)
        if v6:
            vp6 = req.POST.get('vp6') if req.POST.get('vp6') else 100
            if gupiaos:
                gupiaos = gupiaos.filter(test3__gt = vp6)
            else:
                gupiaos = gupiaolist.objects.filter(test3__gt = vp6)
        if v7:
            vp7 = req.POST.get('vp7') if req.POST.get('vp7') else 25.0
            if gupiaos:
                gupiaos = gupiaos.filter(salegrossprofitrto__gt=vp7)
            else:
                gupiaos = gupiaolist.objects.filter(salegrossprofitrto__gt=vp7)
        if v8:
            vp8 = req.POST.get('vp8') if req.POST.get('vp8') else 20.0
            if gupiaos:
                gupiaos = gupiaos.filter(dilutedroe__gt=vp8)
            else:
                gupiaos = gupiaolist.objects.filter(dilutedroe__gt=vp8)
        # return HttpResponse("<div id='success'>WAITING</div>")
        if v9:
            if gupiaos:
                gupiaos = gupiaos.filter(test9=1)
            else:
                gupiaos = gupiaolist.objects.filter(test9=1)
        if v10:
            vp10 = req.POST.get('vp10') if req.POST.get('vp10') else 10.0
            vp10 = float(vp10)*100000000
            if gupiaos:
                gupiaos = gupiaos.filter(test2__lte=vp10)
            else:
                gupiaos = gupiaolist.objects.filter(test2__lte=vp10)

        return render_to_response('result.html',
                                  {'gupiaolist': gupiaos,
                                   },
                                  context_instance=RequestContext(req))
    return render_to_response('search.html', context_instance=RequestContext(req))
