
FROM ubuntu:16.04
RUN apt-get update && apt-get install -y apt-utils \
    python3 python3-pip wget firefox chromium-browser
RUN apt-get upgrade
RUN pip3 install selenium
RUN pip3 install requests
COPY . .
CMD ["python3", "AutomationFlow.py"]
