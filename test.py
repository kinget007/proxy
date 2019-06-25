import datetime
import json
import urllib

import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        if flow.request.host == 'www.google.com':
            return
        # if flow.request.path.find(".") == -1 and flow.request.path.find("track") == -1 and (flow.request.host.find("yeshj") > -1 or flow.request.host.find("hujiang") > -1):
        else:
            ctx.log.info("--------------------------------------------------------------------------------------")
            self.num = self.num + 1
            timestamp_ = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            result = {
                "num": self.num,
                "url": flow.request.pretty_url,
                "method": str(flow.request.method),
                "query": urllib.parse.unquote(str(flow.request.query).replace("\\x", "%").replace('MultiDictView', ''), encoding='utf-8',
                                              errors='replace'),
                "post_data": urllib.parse.unquote(str(flow.request.raw_content).replace("\\x", "%"),
                                                  encoding='utf-8',
                                                  errors='replace'),
                # "HJ_UID": str(flow.request.cookies.get('HJ_UID')),
                "time": timestamp_
            }

            import os
            import logging
            logging.basicConfig(filename=os.path.join('/home/log/', 'log.log'), level=logging.INFO, format='')
            logging.info(json.dumps(result))


addons = [
    Counter()
]
