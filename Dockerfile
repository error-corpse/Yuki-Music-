FROM nikolaik/python-nodejs:python3.10-nodejs19

RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


RUN pip3 install --upgrade pip setuptools

RUN git clone https://github.com/error-corpse/Yuki-Music- /root/YukiMusic
WORKDIR /root/YukiMusic

#Copy config file to /root/
COPY ./YukiMusic/config.py ./YukiMusic/config.py* /root/YukiMusic/YukiMusic/

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/bot/bin:$PATH"

# Starting Worker
CMD ["python3","-m","YukiMusic"]

