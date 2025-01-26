#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import requests, json, os
import time
import log

# 消息推送 url
SEND_MSG_URL = "https://qmsg.zendee.cn/jgroup/"

# 推送的qq
QMSG_QQ = os.getenv("QMSG_QQ")

#qmsg的key
QMSG_KEY = os.getenv("QMSG_KEY")

def send_text(content):    
    payload = {
        "qq": QMSG_QQ,
        "msg": content,
    }
    log.logger.debug(log.SensitiveData(json.dumps(payload, ensure_ascii=False)))
    
    send_msg_url = SEND_MSG_URL + QMSG_KEY
    try:
        res = requests.post(send_msg_url, json=payload)
        res.raise_for_status()

        log.logger.debug(f"Send text message successful. Response: {res.json()}")
    except requests.exceptions.ConnectionError as e:
        log.logger.error(f"Send text message failed. Check network connection: {e}")
        raise e
    except Exception as e:
        log.logger.error(f"Send text message failed. Error: {e}")
        raise e

