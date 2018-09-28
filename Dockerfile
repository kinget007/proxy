FROM python:alpine3.7
WORKDIR /home/rule/
ADD test.py /home/rule/test.py
ADD mitmproxy-4.0.4-py3-none-any.whl /home/mitmproxy/mitmproxy-4.0.4-py3-none-any.whl
RUN apk add --no-cache \
        git \
        g++ \
        libffi \
        libffi-dev \
        libstdc++ \
        openssl \
        openssl-dev \
    && pip3 install -U /home/mitmproxy/mitmproxy-4.0.4-py3-none-any.whl \
	&& apk del --purge \
		git \
        g++ \
        libffi-dev \
        openssl-dev \
        python3-dev \
    && rm -rf ~/.cache/pip /home/mitmproxy/mitmproxy-4.0.4-py3-none-any.whl \
    && mkdir -p /home/mitmproxy/.mitmproxy

VOLUME /home/mitmproxy/.mitmproxy
#RUN pip3 install -I -i https://pypi.mirrors.ustc.edu.cn/simple/ mitmproxy --trusted-host pypi.mirrors.ustc.edu.cn
EXPOSE 8080
CMD mitmdump -s /home/rule/test.py