import json, time
import requests
import math
from platForm.oclick.logout.tool import ynby_db, wami_db


class Cancellation(object):
    def __init__(self, number, phone):
        self.number = number
        self.phone = phone
        self.provin_sql = "select * from ynby.provincial_agent where phone_number = '%s'" % self.number
        self.maker_sql = "select * from ynby.maker where phone_number = '%s'" % self.number
        self.traff_sql = "select * from ynby.traffic_referral_man where phone_number = '%s'" % self.number
        self.member_sql = "select * from skin_care_mgr.c_membership where login_id = '%s'" % self.number
        self.provin_maker_sql = "select phone_number,id from ynby.maker where provincial_agent_id = " \
                                "(select id from ynby.provincial_agent where phone_number = '%s' " \
                                "and del_flag = '0')" % self.number
        self.maker_membership_sql = "select * from skin_care_mgr.c_membership where maker_id = " \
                                    "(select id from ynby.maker where phone_number = '%s' " \
                                    "and del_flag = '0')" % self.number
        self.allpro_mem_sql = "select login_id,id from skin_care_mgr.c_membership WHERE maker_id = " \
                              "any(select id from ynby.maker where provincial_agent_id = " \
                              "(select id from ynby.provincial_agent where phone_number = '%s' and del_flag = '1') " \
                              "and del_flag = '0' ) and del_flag = '1' and login_id = '%s'" % (self.number, self.number)
        self.allpro_maker_sql = "select phone_number,id,del_flag from ynby.maker where provincial_agent_id = " \
                                "(select id from ynby.provincial_agent where phone_number = '%s' " \
                                "and del_flag = '1')" % self.number
        self.delprovin_sql = "delete from ynby.provincial_agent where phone_number = '%s' " % self.number
        self.delmaker_sql = "delete from ynby.maker where phone_number = '%s'" % self.number
        self.invite_maker = "delete from ynby.invite_maker_record where phone = '%s'" % self.number
        self.delmembership_sql = "delete from skin_care_mgr.c_membership where login_id = '%s'" % self.number
        self.delcell = "delete from skin_care_mgr.c_membership where cell_phone = '%s'" % self.number
        self.deltraff_sql = "delete from ynby.traffic_referral_man where phone_number = '%s'" % self.number
        self.dwdistr_sql = "delete from distribution_customer where customer_account = '%s'" % self.number
        self.dwmaker_sql = "delete from maker_information where phone_no = '%s'" % self.number
        self.dwstore_sql = "delete from store where contact_mobile = '%s'" % self.number
        self.memsql = "select * FROM `sbc-customer`.customer WHERE customer_account = '%s' " \
                      "and del_flag = '0'" % self.phone
        self.provin = "select * from `sbc-customer`.store WHERE contact_mobile = '%s' and del_flag = '0'" % self.phone
        self.maker = "select * from `sbc-customer`.maker_information WHERE phone_no = '%s' " \
                     "and del_flag = '0'" % self.phone
        self.login = "delete from skin_care_mgr.c_membership where login_id = '%s'" % self.phone
        self.cell = "delete from skin_care_mgr.c_membership where cell_phone = '%s'" % self.phone
        self.out_url = 'https://devhshop.baiyaodajiankang.com/mbff/customer/delCustomer'

    """
    注销身份及会员
    """

    def baiyao(self):
        if self.number:
            p_data = ynby_db(self.provin_sql)
            if p_data is None:
                print('此账号不是省代：%s' % self.number)
                m_data = ynby_db(self.maker_sql)
                if m_data is None:
                    print('此账号不是创客：%s' % self.number)
                    ynby_db(self.invite_maker)
                    t_data = ynby_db(self.traff_sql)
                    if t_data is None:
                        print('此账号不是天使:%s' % self.number)
                        mem_data = ynby_db(self.member_sql)
                        if mem_data is None:
                            print('此账号不是会员:%s' % self.number)
                            logout_data = json.loads(self.logout_membership(self.number))
                            if logout_data.get('code') == "K-000000":
                                re = {'msg_code': '00000', 'msg': '会员注销成功', 'msg_list': '%s' % logout_data}
                            else:
                                re = {'msg_code': '00000', 'msg': '会员注销失败', 'msg_list': '%s' % logout_data}
                        else:
                            selmem_data = ynby_db(self.member_sql)
                            selmem_name = selmem_data.get('member_name')
                            logout_data = json.loads(self.logout_membership(self.number))
                            ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                            if logout_data.get('code') == "K-000000":
                                re = {'msg_code': '00000', 'msg': '会员注销成功：%s' % selmem_name,
                                      'msg_list': '%s' % logout_data}
                            else:
                                re = {'msg_code': '00000', 'msg': '会员注销失败', 'msg_list': '%s' % logout_data}
                    else:
                        seltra_data = ynby_db(self.traff_sql)
                        seltra_name = seltra_data.get('nick_name')  # 获取该天使name
                        seltra_mem_id = seltra_data.get('phone_number')
                        ynby_db(self.deltraff_sql)  # 删除天使
                        wami_db(self.dwdistr_sql)  # 删除万米端天使
                        logout_data = json.loads(self.logout_membership(self.number))
                        ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                        if logout_data.get('code') == "K-000000":
                            re = {'msg_code': '00000',
                                  'msg': "天使注销成功：'%s',会员注销成功：'%s'" % (seltra_name, seltra_mem_id),
                                  'msg_list': '%s' % logout_data}
                        else:
                            re = {'msg_code': '00000',
                                  'msg': "天使注销成功：'%s',会员注销失败：'%s'" % (seltra_name, seltra_mem_id),
                                  'msg_list': '%s' % logout_data}
                else:
                    selmak_mem_data = ynby_db(self.maker_membership_sql)
                    selmak_data = ynby_db(self.maker_sql)
                    if selmak_mem_data is None:  # 如果该创客无会员绑定直接删除
                        ynby_db(self.delmaker_sql)
                        ynby_db(self.invite_maker)  # 删除邀请创客记录
                        wami_db(self.dwmaker_sql)  # 删除万米端创客
                        selmak_data_name = selmak_data.get('name')
                        selmak_data_phone = selmak_data.get('phone_number')
                        logout_data = json.loads(self.logout_membership(self.number))
                        ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                        if logout_data.get('code') == "K-000000":
                            re = {'msg_code': '00000',
                                  'msg': "创客注销成功:'%s',会员注销成功：'%s'" % (selmak_data_name, selmak_data_phone),
                                  'msg_list': '%s' % logout_data}
                        else:
                            re = {'msg_code': '00000',
                                  'msg': "创客注销成功:'%s',会员注销失败：'%s'" % (selmak_data_name, selmak_data_phone),
                                  'msg_list': '%s' % logout_data}
                    else:
                        maker_membership_data = ynby_db(self.maker_membership_sql)
                        maker_membership_phone = maker_membership_data.get('login_id')
                        self.logout_membership(maker_membership_phone)  # 根据绑定该创客的会员手机号注销该会员
                        time.sleep(1)
                        delsql = "delete from skin_care_mgr.c_membership where login_id = '%s'" % maker_membership_phone
                        ynby_db(delsql)
                        selmak_mem_data1 = ynby_db(self.maker_membership_sql)  # 二次查询
                        while selmak_mem_data1 is not None:
                            maker_membership_phone1 = selmak_mem_data1.get('login_id')
                            maker_membership_id = selmak_mem_data1.get('id')
                            self.logout_membership(maker_membership_phone1)
                            delsql = "delete from skin_care_mgr.c_membership where id = '%s'" % maker_membership_id
                            ynby_db(delsql)
                            selmak_mem_data1 = ynby_db(self.maker_membership_sql)
                        else:
                            selmak_data_name1 = selmak_data.get('name')
                            selmak_data_phone1 = selmak_data.get('phone_number')
                            ynby_db(self.delmaker_sql), \
                            ynby_db(self.invite_maker), wami_db(self.dwmaker_sql)  # 删除创客
                            logout_data = json.loads(self.logout_membership(self.number))
                            ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                            if logout_data.get('code') == "K-000000":
                                re = {'msg_code': '00000',
                                      'msg': "创客注销成功:'%s',会员注销成功：'%s'" % (selmak_data_name1, selmak_data_phone1),
                                      'msg_list': '%s' % logout_data}
                            else:
                                re = {'msg_code': '00000',
                                      'msg': "创客注销成功:'%s',会员注销失败：'%s'" % (selmak_data_name1, selmak_data_phone1),
                                      'msg_list': '%s' % logout_data}
            else:
                pro_mak_data = ynby_db(self.provin_maker_sql)  # 查询绑定该省代的创客
                selpro_data = ynby_db(self.provin_sql)
                if pro_mak_data is None:  # 无创客天使绑定该省代直接删除
                    selpro_data_id = selpro_data.get('id')
                    selpro_data_phone = selpro_data.get('phone')
                    ynby_db(self.delprovin_sql), wami_db(self.dwstore_sql)  # 万米端删除省代
                    logout_data = json.loads(self.logout_membership(self.number))
                    ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                    if logout_data.get('code') == "K-000000":
                        re = {'msg_code': '00000',
                              'msg': "省代注销成功:'%s',会员注销成功:'%s'" % (selpro_data_id, selpro_data_phone),
                              'msg_list': '%s' % logout_data}
                    else:
                        re = {'msg_code': '00000',
                              'msg': "省代注销成功:'%s',会员注销失败:'%s'" % (selpro_data_id, selpro_data_phone),
                              'msg_list': '%s' % logout_data}
                else:
                    all_promem_data = ynby_db(self.allpro_mem_sql)  # 查询绑定该省代的所有会员
                    all_promaker_data = ynby_db(self.allpro_maker_sql)  # 查询绑定该省代的所有创客
                    while all_promem_data is not None:
                        all_promem_login = all_promem_data.get('login_id')
                        all_promem_id = all_promem_data.get('id')
                        del_sql = "delete from skin_care_mgr.c_membership where id = '%s'" % all_promem_id
                        self.logout_membership(all_promem_login)  # 注销绑定该省代的所有会员
                        time.sleep(1)
                        ynby_db(del_sql)
                        all_promem_data = ynby_db(self.allpro_mem_sql)
                    if all_promaker_data is not None:
                        while all_promaker_data is not None:
                            all_promaker_phone = all_promaker_data.get('phone_number')
                            dwmak_sql = "delete from maker_information where phone_no = '%s'" % all_promaker_phone
                            dmaker_sql = "delete from ynby.maker where phone_number = '%s'" % all_promaker_phone
                            dinvite_maker = "delete from ynby.invite_maker_record where phone = '%s'" % all_promaker_phone
                            dmakmem_sql = "delete from skin_care_mgr.c_membership where login_id = '%s'" % \
                                          all_promaker_phone
                            ynby_db(dmaker_sql), ynby_db(dinvite_maker), wami_db(dwmak_sql)
                            self.logout_membership(all_promaker_phone)  # 注 销绑定该省代的所有创客
                            time.sleep(1), ynby_db(dmakmem_sql)
                            all_promaker_data = ynby_db(self.allpro_maker_sql)
                        selpro_data_id = selpro_data.get('id')
                        selpro_data_phone = selpro_data.get('phone')
                        ynby_db(self.delprovin_sql), wami_db(self.dwstore_sql)  # 删除省代
                        logout_data = json.loads(self.logout_membership(self.number))  # 注销该省代会员
                        ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                        if logout_data.get('code') == "K-000000":
                            re = {'msg_code': '00000',
                                  'msg': "省代注销成功:'%s',会员注销成功:'%s'" % (selpro_data_id, selpro_data_phone),
                                  'msg_list': '%s' % logout_data,
                                  'msg_mem': '绑定该省代的所有会员注销成功',
                                  'msg_maker': '绑定该省代的所有创客注销成功'}
                        else:
                            re = {'msg_code': '00000',
                                  'msg': "省代注销成功:'%s',会员注销失败:'%s'" % (selpro_data_id, selpro_data_phone),
                                  'msg_list': '%s' % logout_data,
                                  'msg_mem': '绑定该省代的所有会员注销成功',
                                  'msg_maker': '绑定该省代的所有创客注销成功'}
                    else:
                        selpro_data_id = selpro_data.get('id')
                        selpro_data_phone = selpro_data.get('phone')
                        ynby_db(self.delprovin_sql), wami_db(self.dwstore_sql)  # 万米端删除省代
                        logout_data = json.loads(self.logout_membership(self.number))
                        time.sleep(1), ynby_db(self.delmembership_sql), ynby_db(self.delcell)
                        if logout_data.get('code') == "K-000000":
                            re = {'msg_code': '00000',
                                  'msg': "省代注销成功:'%s',会员注销成功:'%s'" % (selpro_data_id, selpro_data_phone),
                                  'msg_list': '%s' % logout_data}
                        else:
                            re = {'msg_code': '00000',
                                  'msg': "省代注销成功:'%s',会员注销失败:'%s'" % (selpro_data_id, selpro_data_phone),
                                  'msg_list': '%s' % logout_data}
        else:
            re = {'msg': '必填字段未填！', 'msg_code': 'K-444444'}
        return json.dumps(re, ensure_ascii=False)

    """
    查询用户身份信息
    """

    def querymember(self):
        global res
        customer_data = wami_db(self.memsql)
        provin_data = wami_db(self.provin)
        maker_data = wami_db(self.maker)
        if self.phone and customer_data is None:
            res = {'msg_code': '00000', 'msg': "'%s'该手机号暂未成为采之汲会员哦！暂未入驻成为采之汲省代及创客！" % self.phone}
        elif self.phone and customer_data is not None:
            customer_id = customer_data['customer_id']
            growth = customer_data['growth_value']
            num = int(growth)
            points = customer_data['points_available']
            if num < 1:
                if provin_data is None and maker_data is None:
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘非会员’！距离白银会员仅需:'%s'成长值，可用积分为:'%s'暂未入驻成为采之汲省代及创客!" % (1 - num, points),
                           'memberId': '%s' % customer_id}
                elif provin_data is None and maker_data is not None:
                    maker_id = maker_data['maker_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘非会员’！距离白银会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为创客!" % (1 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id}
                elif provin_data is not None and maker_data is None:
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘非会员’！距离白银会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代!" % (1 - num, points),
                           'memberId': '%s' % customer_id,
                           'provincialId': '%s' % provincial_id}
                else:
                    maker_id = maker_data['maker_no']
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘非会员’！距离白银会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代和创客!" % (1 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id,
                           'provincialId': '%s' % provincial_id}
            elif 1 <= num < 3000:
                if provin_data is None and maker_data is None:
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘白银会员’！距离黄金会员仅需:'%s'成长值，可用积分为:'%s'暂未入驻成为采之汲省代及创客!"
                                  % (3000 - num, points),
                           'memberId': '%s' % customer_id}
                elif provin_data is None and maker_data is not None:
                    maker_id = maker_data['maker_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘白银会员’！距离黄金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为创客!" % (3000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id}
                elif provin_data is not None and maker_data is None:
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘白银会员’！距离黄金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代!" % (3000 - num, points),
                           'memberId': '%s' % customer_id,
                           'provincialId': '%s' % provincial_id}
                else:
                    maker_id = maker_data['maker_no']
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘白银会员’！距离黄金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代和创客!" % (3000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id,
                           'provincialId': '%s' % provincial_id}
            elif 3000 <= num < 10000:
                if provin_data is None and maker_data is None:
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黄金会员’！距离铂金会员仅需:'%s'成长值，可用积分为:'%s'暂未入驻成为采之汲省代及创客!" %
                                  (10000 - num, points),
                           'memberId': '%s' % customer_id}
                elif provin_data is None and maker_data is not None:
                    maker_id = maker_data['maker_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黄金会员’！距离铂金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为创客!" % (10000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id}
                elif provin_data is not None and maker_data is None:
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黄金会员’！距离铂金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代!" % (10000 - num, points),
                           'memberId': '%s' % customer_id,
                           'provincialId': '%s' % provincial_id}
                else:
                    maker_id = maker_data['maker_no']
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黄金会员’！距离铂金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代和创客!" % (10000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id,
                           'provincialId': '%s' % provincial_id}
            elif 10000 <= num < 25000:
                if provin_data is None and maker_data is None:
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘铂金会员’！距离黑金会员仅需:'%s'成长值，可用积分为:'%s'暂未入驻成为采之汲省代及创客!" %
                                  (25000 - num, points),
                           'memberId': '%s' % customer_id}
                elif provin_data is None and maker_data is not None:
                    maker_id = maker_data['maker_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘铂金会员’！距离黑金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为创客!" % (25000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id}
                elif provin_data is not None and maker_data is None:
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘铂金会员’！距离黑金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代!" % (25000 - num, points),
                           'memberId': '%s' % customer_id,
                           'provincialId': '%s' % provincial_id}
                else:
                    maker_id = maker_data['maker_no']
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘铂金会员’！距离黑金会员仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代和创客!" % (25000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id,
                           'provincialId': '%s' % provincial_id}
            elif 25000 <= num < 50000:
                if provin_data is None and maker_data is None:
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金会员’！距离黑金PLUS仅需:'%s'成长值，可用积分为:'%s'暂未入驻成为采之汲省代及创客!" %
                                  (50000 - num, points),
                           'memberId': '%s' % customer_id}
                elif provin_data is None and maker_data is not None:
                    maker_id = maker_data['maker_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金会员’！距离黑金PLUS仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为创客!" % (50000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id}
                elif provin_data is not None and maker_data is None:
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金会员’！距离黑金PLUS仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代!" % (50000 - num, points),
                           'memberId': '%s' % customer_id,
                           'provincialId': '%s' % provincial_id}
                else:
                    maker_id = maker_data['maker_no']
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金会员’！距离黑金PLUS仅需:'%s'成长值，可用积分为:'%s'目前已入驻成为省代和创客!" % (50000 - num, points),
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id,
                           'provincialId': '%s' % provincial_id}
            elif num >= 50000:
                if provin_data is None and maker_data is None:
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金PLUS’！可用积分为:'%s'暂未入驻成为采之汲省代及创客!" % points,
                           'memberId': '%s' % customer_id}
                elif provin_data is None and maker_data is not None:
                    maker_id = maker_data['maker_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金PLUS’！可用积分为:'%s'目前已入驻成为创客!" % points,
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id}
                elif provin_data is not None and maker_data is None:
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金PLUS’！可用积分为:'%s'目前已入驻成为省代!" % points,
                           'memberId': '%s' % customer_id,
                           'provincialId': '%s' % provincial_id}
                else:
                    maker_id = maker_data['maker_no']
                    provincial_id = provin_data['store_no']
                    res = {'msg_code': '00000',
                           'msg': "该账号目前为采之汲‘黑金PLUS’！可用积分为:'%s'目前已入驻成为省代和创客!" % points,
                           'memberId': '%s' % customer_id,
                           'makerId': '%s' % maker_id,
                           'provincialId': '%s' % provincial_id}
            else:
                pass
        else:
            res = {'msg_code': '00000',
                   'msg': '缺少必填字段！'}
        return json.dumps(res, ensure_ascii=False)

    """
     调用万米注销会员接口
    """
    def logout_membership(self, num):
        wm_sql = "select customer_id from customer where customer_account = '%s'" % num
        headers = {"phone": "%s" % num,
                   "Content-Type": "application/json;charset=utf-8"}
        customer_data = wami_db(wm_sql)
        if customer_data is not None:
            customer_id = customer_data.get('customer_id')
            data = json.dumps({
                "customerId": "%s" % customer_id
            })
            res = requests.post(self.out_url, data, headers=headers)
        else:
            res = requests.post(self.out_url, headers=headers)
        return json.dumps(res.json(), ensure_ascii=False)

    """
    注销会员
    """
    def logoutmember(self):
        logout_data = json.loads(self.logout_membership(self.phone))
        if logout_data['code'] == "K-000000":
            ynby_db(self.login), ynby_db(self.cell)
            re = {'msg_code': '00000', 'msg': '会员注销成功：%s' % self.phone}
        elif logout_data['code'] == "K-000111":
            ynby_db(self.login), ynby_db(self.cell)
            re = {'msg_code': '00404', 'msg': '会员注销失败：%s,用户不存在！' % self.phone}
        else:
            re = {'msg_code': '00444', 'msg': '会员注销失败', 'msg_list': '%s' % logout_data}
        return json.dumps(re, ensure_ascii=False)


def get_report(current,size,project,env,date):
    current = int(current)
    size = int(size)
    url = "http://192.168.165.38:8088/api/files/prefix"
    querystring = {"filePrefix": "auto-test/htmlReport/%s/%s/%s"%(project,env,date)}
    response = requests.request("GET", url, params=querystring)
    result = response.json()
    result['count'] = len(result['data'])
    data = result['data']
    data_list = []
    for key in data:
        time = key[40:59]
        time_list = list(time)
        time_list[10] = " "
        time_list[13] = ":"
        time_list[16] = ":"
        time_str = ''.join(time_list)
        data_list.append(time_str)
    data_list.sort(reverse=True)
    report = []
    for time in data_list:
        report.append({"time": time})
    pages = math.ceil(len(result['data'])/size)
    if current<pages:
        data = report[(current-1)*size:current*size]
    elif current==pages:
        data = report[(current-1)*size:]
    else:
        data = ""
    current_data = len(data)
    report_data = {"data": data, "count": len(result['data']), "pages": pages, "current_data": current_data
                   }
    return report_data

