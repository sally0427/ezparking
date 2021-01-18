# coding:utf-8

class RET:
    OK                  = "0"
    DBERR               = "4001"
    NODATA              = "4002"
    DATAEXIST           = "4003"
    DATAERR             = "4004"
    SESSIONERR          = "4101"
    LOGINERR            = "4102"
    PARAMERR            = "4103"
    USERERR             = "4104"
    ROLEERR             = "4105"
    PWDERR              = "4106"
    REQERR              = "4201"
    IPERR               = "4202"
    THIRDERR            = "4301"
    IOERR               = "4302"
    SERVERERR           = "4500"
    UNKOWNERR           = "4501"

error_map = {
    RET.OK                    : u"成功",
    RET.DBERR                 : u"資料庫查詢錯誤",
    RET.NODATA                : u"無資料",
    RET.DATAEXIST             : u"數據已存在",
    RET.DATAERR               : u"數據錯誤",
    RET.SESSIONERR            : u"使用者未登入",
    RET.LOGINERR              : u"使用者登入失敗",
    RET.PARAMERR              : u"參數錯誤",
    RET.USERERR               : u"使用者不存在",
    RET.ROLEERR               : u"使用者身份錯誤",
    RET.PWDERR                : u"密碼錯誤",
    RET.REQERR                : u"非法請求",
    RET.IPERR                 : u"IP受限",
    RET.THIRDERR              : u"第三方系統錯誤",
    RET.IOERR                 : u"文件讀寫錯誤",
    RET.SERVERERR             : u"內部錯誤",
    RET.UNKOWNERR             : u"未知錯誤",
}
