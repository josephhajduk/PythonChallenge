__author__ = 'jhajduk'

import string

message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

transl = string.maketrans(
    "abcdefghijklmnopqrstuvwxyz",
    "cdefghijklmnopqrstuvwxyzab"
)

print string.translate(message,transl)

print string.translate("map",transl)