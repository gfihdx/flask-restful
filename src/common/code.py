from flask import jsonify


class Code:
    # 成功
    SUCCESS = 0
    # 失败
    FAIL = -1
    # 参数为空
    PARAM_FAIL = -2
    # 数据库操作失败
    DATA_FAIL = -3
    # 文件为空
    FILE_NULL = -4
    # 不存在此条数据
    NOT_DATA = -5

    msg = {
        SUCCESS: "success",
        FAIL: "fail",
        PARAM_FAIL: "param is not null",
        DATA_FAIL: "数据库操作失败",
        FILE_NULL: '上传文件为空',
        NOT_DATA: '没有此条数据'
    }


def make_result(data=None, code=Code.SUCCESS):
    return jsonify({"code": code, "msg": Code.msg[code], "data": data})
