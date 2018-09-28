import json
import urllib

import mitmproxy.http
from mitmproxy import ctx


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("--------------------------------------------------------------------------------------")
        if flow.request.host == 'www.google.com':
            return
        if flow.request.path.find(".") == -1 and flow.request.path.find("track") == -1 and (flow.request.host.find("yeshj") > -1 or flow.request.host.find(
                "hujiang") > -1):
            ctx.log.info("--------------------------------------------------------------------------------------")
            self.num = self.num + 1
            ctx.log.info("url : " + str(self.num) + " : " + flow.request.pretty_url)
            ctx.log.info("method : " + str(flow.request.method))
            ctx.log.info(
                "query : " + urllib.parse.unquote(str(flow.request.query).replace("\\x", "%"), encoding='utf-8',
                                                  errors='replace'))
            ctx.log.info("post data : " + urllib.parse.unquote(str(flow.request.raw_content).replace("\\x", "%"),
                                                               encoding='utf-8',
                                                               errors='replace'))
            ctx.log.info("HJ_UID : " + str(flow.request.cookies.get('HJ_UID')))


addons = [
    Counter()
]
