# -*- coding: utf-8 -*-
# @Time    : 2022/7/20 10:50
# @Author  : 焦海俊
# @File    : queryMsg.py
# @Software: PyCharm
from platForm.Utill.Wanmi_DB import wanmidb


def queryBySkuId(input_data):
    global res
    skuid_sql = "select goods_info_id AS skuId,goods_info_name AS '商品名称',goods_info_no AS sku,goods_info_barcode AS '条形码',stock AS '库存',added_flag AS '上下架状态,0:下架1:上架',distribution_goods_audit AS '分销状态 0:普通商品 1:待审核 2:已审核 3:审核不通过 4:禁止分销',commission_rate AS '佣金比例',service_number AS '服务次数',package_flag AS '0 商品 1 套餐',package_type AS '套餐类型 0:全部 1:普通 2:MIS 3:积分',check_status AS '0未审核,1审核过' from `sbc-goods`.goods_info where goods_info_id = '%s' " % (
        input_data)
    skuid_data = wanmidb.select(skuid_sql)
    if skuid_data is None:
        res = None
    else:
        goods_skuid = skuid_data['skuId']
        goods_name = skuid_data['商品名称']
        goods_sku = skuid_data['sku']
        goods_barcode = skuid_data['条形码']
        goods_stock = skuid_data['库存']
        added_flag = skuid_data['上下架状态,0:下架1:上架']
        service_num = skuid_data['服务次数']
        goods_type = skuid_data['0 商品 1 套餐']
        res = ({'code': '0000', 'msg': '根据skuId查询信息成功',
                'skuId': '%s' % goods_skuid,
                '商品名称': '%s' % goods_name,
                'sku编码': '%s' % goods_sku,
                '条形码': '%s' % goods_barcode,
                '库存': '%s' % goods_stock,
                "状态('0:下架1:上架')": '%s' % added_flag,
                '服务次数': '%s' % service_num,
                "类型('0:商品1:套餐')": '%s' % goods_type,
                })
    return res


def queryBySkuNo(input_data):
    global res
    sku_sql = "select goods_info_id AS skuId,goods_info_name AS '商品名称',goods_info_no AS sku,goods_info_barcode AS '条形码',stock AS '库存',added_flag AS '上下架状态,0:下架1:上架',distribution_goods_audit AS '分销状态 0:普通商品 1:待审核 2:已审核 3:审核不通过 4:禁止分销',commission_rate AS '佣金比例',service_number AS '服务次数',package_flag AS '0 商品 1 套餐',package_type AS '套餐类型 0:全部 1:普通 2:MIS 3:积分',check_status AS '0未审核,1审核过' from `sbc-goods`.goods_info where goods_info_no = '%s' " % (
        input_data)
    sku_data = wanmidb.select(sku_sql)
    if sku_data is None:
        res = None
    else:
        goods_skuid = sku_data['skuId']
        goods_name = sku_data['商品名称']
        goods_sku = sku_data['sku']
        goods_barcode = sku_data['条形码']
        goods_stock = sku_data['库存']
        added_flag = sku_data['上下架状态,0:下架1:上架']
        service_num = sku_data['服务次数']
        goods_type = sku_data['0 商品 1 套餐']
        res = ({'code': '0000', 'msg': '根据sku编码查询信息成功',
                'skuId': '%s' % goods_skuid,
                '商品名称': '%s' % goods_name,
                'sku编码': '%s' % goods_sku,
                '条形码': '%s' % goods_barcode,
                '库存': '%s' % goods_stock,
                "状态('0:下架1:上架')": '%s' % added_flag,
                '服务次数': '%s' % service_num,
                "类型('0:商品1:套餐')": '%s' % goods_type,
                })
    return res


def queryByName(input_data):
    global res
    name_sql = "select goods_info_id AS skuId,goods_info_name AS '商品名称',goods_info_no AS sku,goods_info_barcode AS '条形码',stock AS '库存',added_flag AS '上下架状态,0:下架1:上架',distribution_goods_audit AS '分销状态 0:普通商品 1:待审核 2:已审核 3:审核不通过 4:禁止分销',commission_rate AS '佣金比例',service_number AS '服务次数',package_flag AS '0 商品 1 套餐',package_type AS '套餐类型 0:全部 1:普通 2:MIS 3:积分',check_status AS '0未审核,1审核过' from `sbc-goods`.goods_info where goods_info_name = '%s' " % (
        input_data)
    name_data = wanmidb.select(name_sql)
    if name_data is None:
        res = None
    else:
        goods_skuid = name_data['skuId']
        goods_name = name_data['商品名称']
        goods_sku = name_data['sku']
        goods_barcode = name_data['条形码']
        goods_stock = name_data['库存']
        added_flag = name_data['上下架状态,0:下架1:上架']
        service_num = name_data['服务次数']
        goods_type = name_data['0 商品 1 套餐']
        res = ({'code': '0000', 'msg': '根据商品名称查询信息成功',
                'skuId': '%s' % goods_skuid,
                '商品名称': '%s' % goods_name,
                'sku编码': '%s' % goods_sku,
                '条形码': '%s' % goods_barcode,
                '库存': '%s' % goods_stock,
                "状态('0:下架1:上架')": '%s' % added_flag,
                '服务次数': '%s' % service_num,
                "类型('0:商品1:套餐')": '%s' % goods_type,
                })
    return res


def queryByBarcode(input_data):
    global res
    barcode_sql = "select goods_info_id AS skuId,goods_info_name AS '商品名称',goods_info_no AS sku,goods_info_barcode AS '条形码',stock AS '库存',added_flag AS '上下架状态,0:下架1:上架',distribution_goods_audit AS '分销状态 0:普通商品 1:待审核 2:已审核 3:审核不通过 4:禁止分销',commission_rate AS '佣金比例',service_number AS '服务次数',package_flag AS '0 商品 1 套餐',package_type AS '套餐类型 0:全部 1:普通 2:MIS 3:积分',check_status AS '0未审核,1审核过' from `sbc-goods`.goods_info where goods_info_barcode = '%s' " % (
        input_data)
    barcode_data = wanmidb.select(barcode_sql)
    if barcode_data is None:
        res = None
    else:
        goods_skuid = barcode_data['skuId']
        goods_name = barcode_data['商品名称']
        goods_sku = barcode_data['sku']
        goods_barcode = barcode_data['条形码']
        goods_stock = barcode_data['库存']
        added_flag = barcode_data['上下架状态,0:下架1:上架']
        service_num = barcode_data['服务次数']
        goods_type = barcode_data['0 商品 1 套餐']
        res = ({'code': '0000', 'msg': '根据条形码查询信息成功',
                'skuId': '%s' % goods_skuid,
                '商品名称': '%s' % goods_name,
                'sku编码': '%s' % goods_sku,
                '条形码': '%s' % goods_barcode,
                '库存': '%s' % goods_stock,
                "状态('0:下架1:上架')": '%s' % added_flag,
                '服务次数': '%s' % service_num,
                "类型('0:商品1:套餐')": '%s' % goods_type,
                })
    return res