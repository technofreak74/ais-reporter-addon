ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install requirements for add-on
RUN apk add --no-cache python3 py3-pip
RUN pip3 install pyserial

# Copy data for add-on
COPY run.sh UDPbroadcast.py /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
