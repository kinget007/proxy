FROM alpine:3.8
ENV LANG=en_US.UTF-8

ADD log.log /home/log/log.log
ADD test.py /home/rule/test.py
ADD mitmproxy-4.0.4-py3-none-any.whl /home/mitmproxy/mitmproxy-4.0.4-py3-none-any.whl

# Add our user first to make sure the ID get assigned consistently,
# regardless of whatever dependencies get added.
RUN apk add --no-cache \
        git \
        g++ \
        libffi \
        libffi-dev \
        libstdc++ \
        openssl \
        openssl-dev \
        python3 \
        python3-dev \
    && python3 -m ensurepip \
    && LDFLAGS=-L/lib pip3 install -U /home/mitmproxy/mitmproxy-4.0.4-py3-none-any.whl \
    && apk del --purge \
        git \
        g++ \
        libffi-dev \
        openssl-dev \
        python3-dev \
    && rm -rf ~/.cache/pip /home/mitmproxy/mitmproxy-4.0.4-py3-none-any.whl \
    && mkdir -p /home/mitmproxy/.mitmproxy

VOLUME /root/.mitmproxy
VOLUME /home/log/

EXPOSE 8080

CMD mitmdump -s /home/rule/test.py
