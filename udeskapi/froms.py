from django import forms


### 坐席外呼参数
class call1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    mishi = forms.CharField(label='密匙', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '密匙'}))
    agent_email = forms.CharField(label='坐席邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席邮箱'}))
    callnumber = forms.CharField(label='外呼号码', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '外呼号码'}))
    timetemp = forms.CharField(label='时间戳', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


### 获取通话记录参数
class call2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    call_id = forms.CharField(label='callid', max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'callid'}))
    timetemp = forms.CharField(label='时间戳', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    mishi = forms.CharField(label='密匙', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '密匙'}))


### 获取通话记录列表参数
class call3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    mishi = forms.CharField(label='密匙', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '密匙'}))
    start_time = forms.CharField(label='查询开始时间', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '查询开始时间'}))
    end_time = forms.CharField(label='查询结束时间', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '查询结束时间'}))
    page = forms.CharField(label='页码，从1开始', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '页码，从1开始'}))
    page_size = forms.CharField(label='每页数量，最大100', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '每页数量，最大100'}))


### 网页外呼参数
class call4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    from_number = forms.CharField(label='主叫号码（客户号码）', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '主叫号码（客户号码）'}))
    to_number = forms.CharField(label='被叫号码（中继号）', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '被叫号码（中继号）'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call5Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call6Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    agent_email = forms.CharField(label='坐席邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call7Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    agent_email = forms.CharField(label='坐席邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席邮箱'}))
    agent_work_state = forms.CharField(label='坐席状态', max_length=100,
                                       widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席状态'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call8Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    start_time = forms.CharField(label='开始时间', max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '开始时间'}))
    end_time = forms.CharField(label='结束时间', max_length=100,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '结束时间'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call9Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    id = forms.CharField(label='外呼任务ID', max_length=100,
                         widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': '外呼任务ID'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call10Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))


class call11Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(attrs={'class': 'form-control',
                                                                      'placeholder': '二级域名'}))


class call12Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control',
                                                   'placeholder': '二级域名'}))


class call13Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control',
                                                   'placeholder': '二级域名'}))


class call14Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    agent_email = forms.CharField(label='坐席邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席邮箱'}))
    mishi = forms.CharField(label='密匙', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '密匙'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call15Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    agent_email = forms.CharField(label='坐席邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席邮箱'}))
    agent_work_way = forms.CharField(label='坐席在线方式', max_length=100,
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席在线方式'}))
    mishi = forms.CharField(label='密匙', max_length=100,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '密匙'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class call16Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    agent_email = forms.CharField(label='坐席邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '坐席邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class agent1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    per_page = forms.CharField(label='每页数量，默认20，最大100', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '每页数量，默认20，最大100'}))
    with_disabled = forms.CharField(label='是否包含已禁用客服（true 或 false）', max_length=100,
                                    widget=forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': '是否包含已禁用客服（true 或 false）'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class agent2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    type = forms.CharField(label='条件类型(id/email)', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件类型(id/email)'}))
    content = forms.CharField(label='条件内容', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '条件内容'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class agent3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    email = forms.CharField(label='邮箱地址，作为账号', max_length=100,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': '邮箱地址，作为账号'}))
    password = forms.CharField(label='密码', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '密码'}))
    agent_role_ids = forms.CharField(label='角色的id,用逗号隔开的数字,数组最大长度10', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '角色的id,用逗号隔开的数字,数组最大长度10'}))
    user_group_ids = forms.CharField(label='员工组的id,用逗号隔开的数字,数组最大长度10', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '员工组的id,用逗号隔开的数字,数组最大长度10'}))
    department_ids = forms.CharField(label='部门的id,用逗号隔开的数字,数组最大长度10', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '部门的id,用逗号隔开的数字,数组最大长度10'}))
    im_ability_value = forms.CharField(label='对话技能值', max_length=100,
                                       widget=forms.TextInput(
                                           attrs={'class': 'form-control', 'placeholder': '对话技能值'}))
    nick_name = forms.CharField(label='姓名', max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '姓名'}))
    aliase = forms.CharField(label='昵称', max_length=100,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '昵称'}))
    cellphone = forms.CharField(label='电话', max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '电话'}))
    profile = forms.CharField(label='员工类型', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '员工类型'}))
    duty = forms.CharField(label='职务', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '职务'}))
    im_welcomes = forms.CharField(label='欢迎语', max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': '欢迎语'}))
    availability = forms.CharField(label='是否接受自动工单分配', max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '是否接受自动工单分配'}))
    avatar = forms.CharField(label='头像URL', max_length=100,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '头像URL'}))
    work_id = forms.CharField(label='工号', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '工号'}))
    callout_number_id = forms.CharField(label='外呼显号id', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '外呼显号id'}))
    lang = forms.CharField(label='语言偏好', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '语言偏好'}))


class agent4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    id = forms.CharField(label='客服id', max_length=100,
                         widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': '客服id'}))
    email = forms.CharField(label='邮箱地址，作为账号', max_length=100,
                            widget=forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': '邮箱地址，作为账号'}))
    password = forms.CharField(label='密码', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '密码'}))
    agent_role_ids = forms.CharField(label='角色的id,用逗号隔开的数字,数组最大长度10', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '角色的id,用逗号隔开的数字,数组最大长度10'}))
    user_group_ids = forms.CharField(label='员工组的id,用逗号隔开的数字,数组最大长度10', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '员工组的id,用逗号隔开的数字,数组最大长度10'}))
    department_ids = forms.CharField(label='部门的id,用逗号隔开的数字,数组最大长度10', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '部门的id,用逗号隔开的数字,数组最大长度10'}))
    im_ability_value = forms.CharField(label='对话技能值', max_length=100,
                                       widget=forms.TextInput(
                                           attrs={'class': 'form-control', 'placeholder': '对话技能值'}))
    nick_name = forms.CharField(label='姓名', max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '姓名'}))
    aliase = forms.CharField(label='昵称', max_length=100,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '昵称'}))
    cellphone = forms.CharField(label='电话', max_length=100,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '电话'}))
    profile = forms.CharField(label='员工类型', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '员工类型'}))
    duty = forms.CharField(label='职务', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '职务'}))
    im_welcomes = forms.CharField(label='欢迎语', max_length=100,
                                  widget=forms.TextInput(
                                      attrs={'class': 'form-control', 'placeholder': '欢迎语'}))
    availability = forms.CharField(label='是否接受自动工单分配', max_length=100,
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': '是否接受自动工单分配'}))
    avatar = forms.CharField(label='头像URL', max_length=100,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': '头像URL'}))
    work_id = forms.CharField(label='工号', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '工号'}))
    disable_status = forms.CharField(label='启用或禁止的状态(enable 或 disable)', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '启用或禁止的状态(enable 或 disable)'}))
    callout_number_id = forms.CharField(label='外呼显号id', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '外呼显号id'}))
    lang = forms.CharField(label='语言偏好', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '语言偏好'}))


class agent5Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    id = forms.CharField(label='客服id', max_length=100,
                         widget=forms.TextInput(
                             attrs={'class': 'form-control', 'placeholder': '客服id'}))
    owner_group_id = forms.CharField(label='客服组id', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': '客服组id'}))


class agent6Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class user_group1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    per_page = forms.CharField(label='每页数量，默认20，最大100', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '每页数量，默认20，最大100'}))


class user_group2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    per_page = forms.CharField(label='每页数量，默认20，最大100', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '每页数量，默认20，最大100'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))


class user_group3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_name = forms.CharField(label='客服组名称', max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '客服组名称'}))


class user_group4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))
    group_name = forms.CharField(label='客服组名称', max_length=100,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': '客服组名称'}))


class user_group5Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))


class callcenter_analysis1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    perpage = forms.CharField(label='每页数量，默认30，最大100', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '每页数量，默认30，最大100'}))


class callcenter_analysis2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    perpage = forms.CharField(label='每页数量，默认30，最大100', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '每页数量，默认30，最大100'}))


class callcenter_analysis3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    perpage = forms.CharField(label='每页数量，默认30，最大100', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '每页数量，默认30，最大100'}))


class callcenter_analysis4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    group_id = forms.CharField(label='客服组id', max_length=100,
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': '客服组id'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    perpage = forms.CharField(label='每页数量，默认30，最大100', max_length=100,
                              widget=forms.TextInput(
                                  attrs={'class': 'form-control', 'placeholder': '每页数量，默认30，最大100'}))


class custom_fields1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    category = forms.CharField(label='要获取的自定义字段类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '要获取的自定义字段类型'}))
class custom_fields2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

    field_name = forms.CharField(label='field_name字段获取 如TextField_97', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'field_name字段获取 如TextField_97'}))

class organizations1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    page = forms.CharField(label='页码，从1开始，默认为1', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '页码，从1开始，默认为1'}))
    perpage = forms.CharField(label='每页数量，默认20，最大100', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '每页数量，默认20，最大100'}))

class organizations2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    type = forms.CharField(label='条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件类型'}))
    content = forms.CharField(label='条件内容', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件内容'}))
class organizations3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class organizations4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class organizations5Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class organizations6Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))


class customers3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    page = forms.CharField(label='页码', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '页码'}))
    page_size = forms.CharField(label='每页数量', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '每页数量'}))

class customers4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    type = forms.CharField(label='条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件类型'}))
    content = forms.CharField(label='条件内容', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件内容'}))

class customers5Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    nick_name = forms.CharField(label='姓名', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓名'}))

class customers6Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    type = forms.CharField(label='条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件类型'}))
    content = forms.CharField(label='条件内容', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件内容'}))
    nick_name = forms.CharField(label='姓名', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓名'}))

class customers7Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    type = forms.CharField(label='条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件类型'}))
    content = forms.CharField(label='条件内容', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件内容'}))

class customers8Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    type = forms.CharField(label='条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件类型'}))
    content = forms.CharField(label='条件内容', max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '条件内容'}))

class customers9Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class customers10Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    nick_name = forms.CharField(label='姓名', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '姓名'}))

class customers11Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class customers12Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    from_type = forms.CharField(label='客户A条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '客户A条件类型'}))
    from_content = forms.CharField(label='客户A条件内容', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '客户A条件内容'}))
    to_type = forms.CharField(label='客户B条件类型', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '客户B条件类型'}))
    to_content = forms.CharField(label='客户B条件内容', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '客户B条件内容'}))



class notes1Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class notes2Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    id = forms.CharField(label='ID', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ID'}))
    name = forms.CharField(label='name', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}))

class notes3Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class notes4Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))
    note_id = forms.CharField(label='业务记录id', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '业务记录id'}))

class notes5Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))

class notes6Form(forms.Form):
    company_subdomain = forms.CharField(label='二级域名', max_length=100,
                                        widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '二级域名'}))
    admin_email = forms.CharField(label='管理员邮箱', max_length=100,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '管理员邮箱'}))
    open_api_token = forms.CharField(label='open_api_token', max_length=100,
                                     widget=forms.TextInput(
                                         attrs={'class': 'form-control', 'placeholder': 'open_api_token'}))
    timestamp = forms.CharField(label='时间戳', max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '时间戳'}))