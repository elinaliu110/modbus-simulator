FROM python:3.9

# 設定工作目錄
WORKDIR /app

COPY MODBUS_TCP_Server_v22_IoTEdge.py /app

RUN pip install modbus-tk numpy

# 暴露 Modbus TCP 端口 502
EXPOSE 502

CMD ["python", "MODBUS_TCP_Server_v22_IoTEdge.py"]