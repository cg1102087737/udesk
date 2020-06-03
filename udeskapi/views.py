from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .froms import call1Form, call2Form, call3Form, call4Form, call5Form, call6Form, call7Form, call8Form, call9Form, \
    call10Form, call11Form, call12Form, call13Form, call14Form, call15Form, call16Form, agent1Form, agent2Form, \
    agent3Form, agent4Form, agent5Form, agent6Form, user_group1Form, user_group2Form, user_group3Form, user_group4Form, \
    user_group5Form, callcenter_analysis1Form, callcenter_analysis2Form, callcenter_analysis3Form, \
    callcenter_analysis4Form, custom_fields1Form, custom_fields2Form, organizations1Form, organizations2Form, organizations3Form, organizations4Form, organizations5Form, organizations6Form, customers3Form, customers4Form, customers5Form, customers6Form, customers7Form

from django.http import HttpResponseRedirect
from .encrypt import create_md5, create_SHA1 ,create_SHA256 ,createRandomString
from .strChangelist import Change_Intlist
import requests
import json

sign_version = 'v2'

def home(request):
    return render(request, 'home.html')


# -----------------------------------callcenter-begin----------------------------------------#

def callcenter(request):
    return render(request, 'udeskapi/apiv2/callcenter/callcenter.html')


### 坐席外呼
def call1(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call1Form(request.POST)
        company_subdomain = request.POST['company_subdomain']
        mishi = request.POST['mishi']
        agent_email = request.POST['agent_email']
        callnumber = request.POST['callnumber']
        timetemp = request.POST['timetemp']
        sign_str = 'agent_email=' + agent_email + '&number=' + callnumber + '&timestamp=' + timetemp + '&' + mishi + ''
        call_out_sign = create_md5(sign_str)
        # print(call_out_sign)
        requset_url = 'http://' + company_subdomain + '.udesk.cn/open_api/callcenter/agent_callout?agent_email=' + agent_email + '&number=' + callnumber + '&timestamp=' + timetemp + '&sign=' + call_out_sign + ''
        r = requests.post(requset_url)
        return render(request, 'udeskapi/apiv1/call/call1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': requset_url, 'encrypt':'MD5', 'request_type':'POST'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call1Form()
    return render(request, 'udeskapi/apiv1/call/call1.html', {'form': form, 'encrypt':'MD5', 'request_type':'POST'})


### 获取通话记录
def call2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call2Form(request.POST)
        company_subdomain = request.POST['company_subdomain']
        call_id = request.POST['call_id']
        mishi = request.POST['mishi']
        timetemp = request.POST['timetemp']

        call_log_sign_str = 'call_id=' + call_id + '&timestamp=' + timetemp + '&' + mishi + ''
        call_log_sign = create_md5(call_log_sign_str)
        requset_url = 'http://' + company_subdomain + '.udesk.cn/open_api/callcenter/call_log?call_id=' + call_id + '&timestamp=' + timetemp + '&sign=' + call_log_sign + ''
        r = requests.get(requset_url)
        return render(request, 'udeskapi/apiv1/call/call2.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': requset_url, 'encrypt':'MD5', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call2Form()
    return render(request, 'udeskapi/apiv1/call/call2.html', {'form': form, 'encrypt':'MD5', 'request_type':'GET'})


def call3(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call3Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        mishi = request.POST['mishi']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        page = request.POST['page']
        page_size = request.POST['page_size']

        ### 调用规则
        call_log_sign_list_str = 'start_time=' + start_time + '&' \
                                                              'end_time=' + end_time + '&' \
                                                                                       'page=' + page + '&' \
                                                                                                        'page_size=' + page_size + '&' \
                                                                                                                                   '' + mishi + ''
        call_log_sign = create_md5(call_log_sign_list_str)
        requset_url = 'https://' + company_subdomain + '.udesk.cn/api/v2/ucpapp/calllogs?start_time=' + start_time + '&end_time=' + end_time + '&page=' + page + '&page_size=' + page_size + '&sign=' + call_log_sign + ''
        r = requests.get(
            'https://' + company_subdomain + '.udesk.cn/api/v2/ucpapp/calllogs?start_time=' + start_time + '&end_time=' + end_time + '&page=' + page + '&page_size=' + page_size + '&sign=' + call_log_sign + '')
        return render(request, 'udeskapi/apiv1/call/call3.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': requset_url, 'encrypt':'MD5', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call3Form()
    return render(request, 'udeskapi/apiv1/call/call3.html', {'form': form, 'encrypt':'MD5', 'request_type':'GET'})


def call4(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call4Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        open_api_token = request.POST['open_api_token']
        admin_email = request.POST['admin_email']
        from_number = request.POST['from_number']
        to_number = request.POST['to_number']
        timestamp = request.POST['timestamp']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + '&'+ nonce +'&'+ sign_version +''
        call_out_sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter/web_callback?from_number=' + from_number + '&to_number=' + to_number + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + call_out_sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        print(sign_str)
        print(request_url)
        r = requests.post(request_url)
        return render(request, 'udeskapi/apiv2/callcenter/call4.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'POST' ,'sign_str':sign_str, 'sign':call_out_sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call4Form()
    return render(request, 'udeskapi/apiv2/callcenter/call4.html', {'form': form, 'encrypt':'SHA256', 'request_type':'POST'})


def call5(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call5Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        open_api_token = request.POST['open_api_token']
        admin_email = request.POST['admin_email']
        timestamp = request.POST['timestamp']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + '&'+ nonce +'&'+ sign_version +''
        print(sign_str)
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter/callout_number_list?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        print(request_url)
        r = requests.get(request_url)
        print(r)
        return render(request, 'udeskapi/apiv2/callcenter/call5.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'GET' ,'sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call5Form()
    return render(request, 'udeskapi/apiv2/callcenter/call5.html', {'form': form, 'encrypt':'SHA256', 'request_type':'GET'})


def call6(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call6Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        agent_email = request.POST['agent_email']
        open_api_token = request.POST['open_api_token']
        admin_email = request.POST['admin_email']
        timestamp = request.POST['timestamp']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + '&'+ nonce +'&'+ sign_version +''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter/agent_state?agent_email=' + agent_email + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/callcenter/call6.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'GET','sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call6Form()
    return render(request, 'udeskapi/apiv2/callcenter/call6.html', {'form': form, 'encrypt':'SHA256', 'request_type':'GET'})


def call7(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call7Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        agent_email = request.POST['agent_email']
        agent_work_state = request.POST['agent_work_state']
        open_api_token = request.POST['open_api_token']
        admin_email = request.POST['admin_email']
        timestamp = request.POST['timestamp']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + '&'+ nonce +'&'+ sign_version +''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter/agent_state?agent_email=' + agent_email + '&agent_work_state=' + agent_work_state + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        r = requests.post(request_url)
        return render(request, 'udeskapi/apiv2/callcenter/call7.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'POST','sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call7Form()
    return render(request, 'udeskapi/apiv2/callcenter/call7.html', {'form': form, 'encrypt':'SHA256', 'request_type':'POST'})


def call8(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call8Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        open_api_token = request.POST['open_api_token']
        admin_email = request.POST['admin_email']
        timestamp = request.POST['timestamp']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callout_tasks?start_time=' + start_time + '&end_time=' + end_time + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/callcenter/call8.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call8Form()
    return render(request, 'udeskapi/callcenter/call8.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def call9(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call9Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        id = request.POST['id']
        open_api_token = request.POST['open_api_token']
        admin_email = request.POST['admin_email']
        timestamp = request.POST['timestamp']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callout_tasks/' + id + '?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/callcenter/call9.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call9Form()
    return render(request, 'udeskapi/callcenter/call9.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def call10(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call10Form(request.POST)
        ### 参数

        ### 调用规则

        return render(request, 'udeskapi/callcenter/call10.html', {'form': form})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call10Form()
    return render(request, 'udeskapi/callcenter/call10.html', {'form': form})


def call11(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call11Form(request.POST)
        ### 参数

        ### 调用规则

        return render(request, 'udeskapi/callcenter/call11.html', {'form': form})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call11Form()
    return render(request, 'udeskapi/callcenter/call11.html', {'form': form})


def call12(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call12Form(request.POST)
        ### 参数

        ### 调用规则

        return render(request, 'udeskapi/callcenter/call12.html', {'form': form})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call12Form()
    return render(request, 'udeskapi/callcenter/call12.html', {'form': form})


def call13(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call13Form(request.POST)
        ### 参数

        ### 调用规则

        return render(request, 'udeskapi/callcenter/call13.html', {'form': form})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call13Form()
    return render(request, 'udeskapi/callcenter/call13.html', {'form': form})


def call14(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call14Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        agent_email = request.POST['agent_email']
        mishi = request.POST['mishi']
        timestamp = request.POST['timestamp']
        ### 调用规则
        sign_str = 'agent_email=' + agent_email + '&timestamp=' + timestamp + '&' + mishi + ''
        sign = create_md5(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api/callcenter/agent_work_way?agent_email=' + agent_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv1/call/call14.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'MD5', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call14Form()
    return render(request, 'udeskapi/apiv1/call/call14.html', {'form': form, 'encrypt':'MD5', 'request_type':'GET'})


def call15(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call15Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        agent_email = request.POST['agent_email']
        agent_work_way = request.POST['agent_work_way']
        mishi = request.POST['mishi']
        timestamp = request.POST['timestamp']
        ### 调用规则
        sign_str = 'agent_email=' + agent_email + '&agent_work_way=' + agent_work_way + '&timestamp=' + timestamp + '&' + mishi + ''
        sign = create_md5(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api/callcenter/agent_work_way?agent_email=' + agent_email + '&agent_work_way=' + agent_work_way + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.post(request_url)
        return render(request, 'udeskapi/apiv1/call/call15.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'MD5', 'request_type':'POST'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call15Form()
    return render(request, 'udeskapi/apiv1/call/call15.html', {'form': form, 'encrypt':'MD5', 'request_type':'POST'})


def call16(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = call16Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        agent_email = request.POST['agent_email']
        timestamp = request.POST['timestamp']
        open_api_token = request.POST['open_api_token']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)

        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/get_agent_token'
        payload = {
            "email": admin_email,
            "agent_email": agent_email,
            "timestamp": timestamp,
            "sign": sign
        }
        headers = {'content-type': 'application/json', 'open_api_token': open_api_token}
        r = requests.post(request_url, data=json.dumps(payload), headers=headers)
        data11 = json.dumps(payload)
        print(data11)
        return render(request, 'udeskapi/apiv1/call/call16.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': data11, 'encrypt':'SHA1', 'request_type':'POST'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = call16Form()
    return render(request, 'udeskapi/apiv1/call/call16.html', {'form': form, 'encrypt':'SHA1', 'request_type':'POST'})


def agent1(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = agent1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        open_api_token = request.POST['open_api_token']
        page = request.POST['page']
        per_page = request.POST['per_page']
        with_disabled = request.POST['with_disabled']
        timestamp = request.POST['timestamp']
        admin_email = request.POST['admin_email']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/agents?page=' + page + '&per_page=' + per_page + '&with_disabled=' + with_disabled + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        print(r.json())
        return render(request, 'udeskapi/apiv2/agents/agent1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})

        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = agent1Form()
    return render(request, 'udeskapi/apiv2/agents/agent1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def agent2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = agent2Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        type = request.POST['type']
        content = request.POST['content']
        timestamp = request.POST['timestamp']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/agents/get_agent?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&type=' + type + '&content=' + content + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/agents/agent2.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = agent2Form()
    return render(request, 'udeskapi/apiv2/agents/agent2.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def agent3(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = agent3Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        ### 必填参数
        email = request.POST['email']
        password = request.POST['password']
        agent_role_ids = Change_Intlist(request.POST['agent_role_ids'])
        user_group_ids = Change_Intlist(request.POST['user_group_ids'])
        department_ids = Change_Intlist(request.POST['department_ids'])
        im_ability_value = int(request.POST['im_ability_value'])
        ### 选填参数
        # nick_name = request.POST['nick_name']
        # aliase = request.POST['aliase']
        # cellphone = request.POST['cellphone']
        # profile = request.POST['profile']
        # duty = request.POST['duty']
        # im_welcomes = request.POST['im_welcomes']
        # availability = bool(request.POST['availability'])
        # print(availability)
        # avatar = request.POST['avatar']
        # work_id = request.POST['work_id']
        # callout_number_id = int(request.POST['callout_number_id'])
        # lang = request.POST['lang']

        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/agents?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        payload = {
            "agent":
                {
                    "email": email,
                    "password": password,
                    "agent_role_ids": agent_role_ids,
                    "user_group_ids": user_group_ids,
                    "department_ids": department_ids,
                    "im_ability_value": im_ability_value,
                    # "nick_name": nick_name,
                    # "aliase": aliase,
                    # "cellphone": cellphone,
                    # "profile": profile,
                    # "duty": duty,
                    # "im_welcomes": im_welcomes,
                    # "availability": availability,
                    # "avatar": avatar,
                    # "work_id": work_id,
                    # "callout_number_id": callout_number_id,
                    # "lang": lang
                }
        }
        headers = {'content-type': 'application/json', 'open_api_token': open_api_token}
        r = requests.post(request_url, data=json.dumps(payload), headers=headers)
        return render(request, 'udeskapi/apiv2/agents/agent3.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'POST'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = agent3Form()
    return render(request, 'udeskapi/apiv2/agents/agent3.html', {'form': form, 'encrypt':'SHA1', 'request_type':'POST'})


def agent4(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = agent4Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        ### 必填参数
        id = request.POST['id']
        ### 选填参数
        email = request.POST['email']
        # password = request.POST['password']
        # agent_role_ids = Change_Intlist(request.POST['agent_role_ids'])
        # user_group_ids = Change_Intlist(request.POST['user_group_ids'])
        # department_ids = Change_Intlist(request.POST['department_ids'])
        # im_ability_value = int(request.POST['im_ability_value'])
        # nick_name = request.POST['nick_name']
        # aliase = request.POST['aliase']
        # cellphone = request.POST['cellphone']
        # profile = request.POST['profile']
        # duty = request.POST['duty']
        # im_welcomes = request.POST['im_welcomes']
        # availability = bool(request.POST['availability'])
        # print(availability)
        # avatar = request.POST['avatar']
        # work_id = request.POST['work_id']
        # disable_status = request.POST['disable_status']
        # callout_number_id = int(request.POST['callout_number_id'])
        # lang = request.POST['lang']

        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/agents/' + id + '?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        payload = {
            "agent":
                {
                    "email": email,
                    # "password": password,
                    # "agent_role_ids": agent_role_ids,
                    # "user_group_ids": user_group_ids,
                    # "department_ids": department_ids,
                    # "im_ability_value": im_ability_value,
                    # "nick_name": nick_name,
                    # "aliase": aliase,
                    # "cellphone": cellphone,
                    # "profile": profile,
                    # "duty": duty,
                    # "im_welcomes": im_welcomes,
                    # "availability": availability,
                    # "avatar": avatar,
                    # "work_id": work_id,
                    # "callout_number_id": callout_number_id,
                    # "lang": lang
                }
        }
        headers = {'content-type': 'application/json', 'open_api_token': open_api_token}
        r = requests.put(request_url, data=json.dumps(payload), headers=headers)
        return render(request, 'udeskapi/apiv2/agents/agent4.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'PUT'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = agent4Form()
    return render(request, 'udeskapi/apiv2/agents/agent4.html', {'form': form, 'encrypt':'SHA1', 'request_type':'PUT'})


def agent5(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = agent5Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        ### 必填参数
        owner_group_id = request.POST['owner_group_id']
        id = request.POST['id']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/agents/' + id + '?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        payload = {
            "owner_group_id": owner_group_id,
            "owner_id": id
        }
        headers = {'content-type': 'application/json'}
        r = requests.delete(request_url, data=json.dumps(payload), headers=headers)
        return render(request, 'udeskapi/apiv2/agents/agent5.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'DELETE'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = agent5Form()
    return render(request, 'udeskapi/apiv2/agents/agent5.html', {'form': form, 'encrypt':'SHA1', 'request_type':'DELETE'})


def agent6(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = agent6Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/agent_roles?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/agents/agent6.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = agent6Form()
    return render(request, 'udeskapi/apiv2/agents/agent6.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def user_group1(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_group1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        page = request.POST['page']
        per_page = request.POST['per_page']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/user_groups?page=' + page + '&per_page=' + per_page + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/user_groups/user_group1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = user_group1Form()
    return render(request, 'udeskapi/apiv2/user_groups/user_group1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def user_group2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_group2Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        page = request.POST['page']
        per_page = request.POST['per_page']
        group_id = request.POST['group_id']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'http://' + company_subdomain + '.udesk.cn/open_api_v1/user_groups/' + group_id + '/agents?page=' + page + '&per_page=' + per_page + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/user_groups/user_group2.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = user_group2Form()
    return render(request, 'udeskapi/apiv2/user_groups/user_group2.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def user_group3(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_group3Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_name = request.POST['group_name']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/user_groups?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        payload = {
            "name": group_name
        }
        headers = {'content-type': 'application/json'}
        r = requests.post(request_url, data=json.dumps(payload), headers=headers)
        return render(request, 'udeskapi/apiv2/user_groups/user_group3.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'POST'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = user_group3Form()
    return render(request, 'udeskapi/apiv2/user_groups/user_group3.html', {'form': form, 'encrypt':'SHA1', 'request_type':'POST'})


def user_group4(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_group4Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_id = request.POST['group_id']
        group_name = request.POST['group_name']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/user_groups/' + group_id + '?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        payload = {
            "name": group_name
        }
        headers = {'content-type': 'application/json'}
        r = requests.put(request_url, data=json.dumps(payload), headers=headers)
        return render(request, 'udeskapi/apiv2/user_groups/user_group4.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'PUT'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = user_group4Form()
    return render(request, 'udeskapi/apiv2/user_groups/user_group4.html', {'form': form, 'encrypt':'SHA1', 'request_type':'PUT'})


def user_group5(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = user_group5Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_id = request.POST['group_id']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/user_groups/' + group_id + '?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.delete(request_url)
        return render(request, 'udeskapi/apiv2/user_groups/user_group5.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'DELETE'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = user_group5Form()
    return render(request, 'udeskapi/apiv2/user_groups/user_group5.html', {'form': form, 'encrypt':'SHA1', 'request_type':'DELETE'})


def callcenter_analysis1(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = callcenter_analysis1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_id = request.POST['group_id']
        page = request.POST['page']
        perpage = request.POST['perpage']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter_analysis/agents_of_group?group_id=' + group_id + '&page=' + page + '&perpage=' + perpage + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = callcenter_analysis1Form()
    return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def callcenter_analysis2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = callcenter_analysis2Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_id = request.POST['group_id']
        page = request.POST['page']
        perpage = request.POST['perpage']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter_analysis/calls_info_of_today?group_id=' + group_id + '&page=' + page + '&perpage=' + perpage + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis2.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = callcenter_analysis2Form()
    return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis2.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def callcenter_analysis3(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = callcenter_analysis3Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_id = request.POST['group_id']
        page = request.POST['page']
        perpage = request.POST['perpage']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter_analysis/calls_in_queue?group_id=' + group_id + '&page=' + page + '&perpage=' + perpage + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis3.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = callcenter_analysis3Form()
    return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis3.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def callcenter_analysis4(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = callcenter_analysis4Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        group_id = request.POST['group_id']
        page = request.POST['page']
        perpage = request.POST['perpage']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/callcenter_analysis/calls_quitted_queue?group_id=' + group_id + '&page=' + page + '&perpage=' + perpage + '&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis4.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = callcenter_analysis4Form()
    return render(request, 'udeskapi/apiv2/callcenter_analysis/callcenter_analysis4.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def custom_fields1(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = custom_fields1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        category = request.POST['category']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/custom_fields?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&category=' + category + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/custom_fields/custom_fields1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = custom_fields1Form()
    return render(request, 'udeskapi/apiv2/custom_fields/custom_fields1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})


def custom_fields2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = custom_fields2Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        field_name = request.POST['field_name']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://'+company_subdomain+'.udesk.cn/open_api_v1/custom_fields/'+field_name+'?email='+admin_email+'&timestamp='+timestamp+'&sign='+sign+''
        payload = {
            "title": "api测试更改单行文本自定义字段",
            "comment": "api测试更改单行文本自定义字段",
        }
        headers = {'content-type': 'application/json', 'open_api_token': open_api_token}
        r = requests.put(request_url, data=json.dumps(payload), headers=headers)
        return render(request, 'udeskapi/apiv2/custom_fields/custom_fields2.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'PUT'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = custom_fields2Form()
    return render(request, 'udeskapi/apiv2/custom_fields/custom_fields2.html', {'form': form, 'encrypt':'SHA1', 'request_type':'PUT'})


def organizations1(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = organizations1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        page = request.POST['page']
        perpage = request.POST['perpage']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://'+company_subdomain+'.udesk.cn/open_api_v1/organizations?page='+page+'&per_page='+perpage+'&email='+admin_email+'&timestamp='+timestamp+'&sign='+sign+''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/organizations/organizations1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = organizations1Form()
    return render(request, 'udeskapi/apiv2/organizations/organizations1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})

def organizations2(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = organizations2Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        type = request.POST['type']
        content = request.POST['content']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://'+company_subdomain+'.udesk.cn/open_api_v1/organizations/show_org?type='+type+'&content='+content+'&email='+admin_email+'&timestamp='+timestamp+'&sign='+sign+''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/organizations/organizations2.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = organizations2Form()
    return render(request, 'udeskapi/apiv2/organizations/organizations2.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})

def organizations3(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = organizations1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        category = request.POST['category']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/custom_fields?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&category=' + category + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/organizations/organizations1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = organizations1Form()
    return render(request, 'udeskapi/apiv2/organizations/organizations1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})

def organizations4(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = organizations1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        category = request.POST['category']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/custom_fields?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&category=' + category + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/organizations/organizations1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = organizations1Form()
    return render(request, 'udeskapi/apiv2/organizations/organizations1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})

def organizations5(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = organizations1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        category = request.POST['category']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/custom_fields?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&category=' + category + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/organizations/organizations1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = organizations1Form()
    return render(request, 'udeskapi/apiv2/organizations/organizations1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})

def organizations6(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = organizations1Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        category = request.POST['category']
        ### 调用规则
        sign_str = '' + admin_email + '&' + open_api_token + '&' + timestamp + ''
        sign = create_SHA1(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/custom_fields?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&category=' + category + ''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/organizations/organizations1.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA1', 'request_type':'GET'})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = organizations1Form()
    return render(request, 'udeskapi/apiv2/organizations/organizations1.html', {'form': form, 'encrypt':'SHA1', 'request_type':'GET'})





def customers3(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = customers3Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        page = request.POST['page']
        page_size = request.POST['page_size']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = ''+admin_email+'&' + open_api_token + '&' + timestamp + '&' + nonce + '&' + sign_version + ''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/customers?page='+page+'&page_size='+page_size+'&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/customers/customers3.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'GET' ,'sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = customers3Form()
    return render(request, 'udeskapi/apiv2/customers/customers3.html', {'form': form, 'encrypt':'SHA256', 'request_type':'GET'})


def customers4(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = customers4Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        type = request.POST['type']
        content = request.POST['content']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = ''+admin_email+'&' + open_api_token + '&' + timestamp + '&' + nonce + '&' + sign_version + ''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/customers/get_customer?type='+type+'&content='+content+'&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/customers/customers4.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'GET' ,'sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = customers4Form()
    return render(request, 'udeskapi/apiv2/customers/customers4.html', {'form': form, 'encrypt':'SHA256', 'request_type':'GET'})


def customers5(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = customers5Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        nick_name = request.POST['nick_name']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = ''+admin_email+'&' + open_api_token + '&' + timestamp + '&' + nonce + '&' + sign_version + ''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/customers?email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        customer = {
            "nick_name": nick_name
        }
        headers = {'content-type': 'application/json'}
        r = requests.post(request_url, data=json.dumps(customer), headers=headers)
        return render(request, 'udeskapi/apiv2/customers/customers5.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'POST' ,'sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = customers5Form()
    return render(request, 'udeskapi/apiv2/customers/customers5.html', {'form': form, 'encrypt':'SHA256', 'request_type':'POST'})

def customers6(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = customers6Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        type = request.POST['type']
        content = request.POST['content']
        nick_name = request.POST['nick_name']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = ''+admin_email+'&' + open_api_token + '&' + timestamp + '&' + nonce + '&' + sign_version + ''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/customers/update_customer?type='+type+'&content='+content+'&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        customer = {
            "nick_name": nick_name
        }
        headers = {'content-type': 'application/json'}
        r = requests.put(request_url, data=json.dumps(customer), headers=headers)
        return render(request, 'udeskapi/apiv2/customers/customers6.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'PUT' ,'sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = customers6Form()
    return render(request, 'udeskapi/apiv2/customers/customers6.html', {'form': form, 'encrypt':'SHA256', 'request_type':'PUT'})

def customers7(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = customers5Form(request.POST)
        ### 参数
        company_subdomain = request.POST['company_subdomain']
        admin_email = request.POST['admin_email']
        open_api_token = request.POST['open_api_token']
        timestamp = request.POST['timestamp']
        nick_name = request.POST['nick_name']
        nonce = createRandomString(6)
        ### 调用规则
        sign_str = ''+admin_email+'&' + open_api_token + '&' + timestamp + '&' + nonce + '&' + sign_version + ''
        sign = create_SHA256(sign_str)
        request_url = 'https://' + company_subdomain + '.udesk.cn/open_api_v1/customers/get_customer?type='+type+'&content='+content+'&email=' + admin_email + '&timestamp=' + timestamp + '&sign=' + sign + '&nonce='+ nonce +'&sign_version='+ sign_version +''
        r = requests.get(request_url)
        return render(request, 'udeskapi/apiv2/customers/customers5.html',
                      {'form': form, 'reponse': r.json(), 'requset_url': request_url, 'encrypt':'SHA256', 'request_type':'GET' ,'sign_str':sign_str, 'sign':sign})
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = customers5Form()
    return render(request, 'udeskapi/apiv2/customers/customers5.html', {'form': form, 'encrypt':'SHA256', 'request_type':'GET'})
# -----------------------------------callcenter-end------------------------------------------#


# -----------------------------------第三方对接-begin------------------------------------------#

@csrf_exempt
def cc_force_api(request):
    return JsonResponse({"result": 0, "msg": "111111"})


# -----------------------------------第三方对接-end------------------------------------------#

def ticket(request):
    return render(request, 'udeskapi/ticket/ticket.html')

# -----------------------------------新增测试------------------------------------------#
def ticket2(request):
    return render(request, 'udeskapi/ticket/ticket.html')
