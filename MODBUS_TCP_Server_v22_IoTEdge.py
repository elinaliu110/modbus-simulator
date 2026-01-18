import time
import random
import modbus_tk
import modbus_tk.defines as mtk
import modbus_tk.modbus_tcp as modbus_tcp

print('==================================================================')
print('|         MODBUS TCP Server Simulator V2.2 (20250324)            |')
print('|              Build by ATW Advantech Institute                  |')
print('==================================================================')

print(' ')
print('MODBUS TCP Server Start with localhost , Port: 502 ')
print('4X Slave ID = 1~3 Wrieable,  Slave ID = 4~8 Random \n')

logger = modbus_tk.utils.create_logger('console')

class ModbusSimulator:
    def __init__(self, port=502, address='', update_intervals=None):
        self.tcpserver = modbus_tcp.TcpServer(port=port, address=address, timeout_in_sec=3)
        self.tcpserver.start()
        self.slave = self.tcpserver.add_slave(1)
        self.slave.add_block('holding_registers', mtk.HOLDING_REGISTERS, 0, 8)

        # 40001~40003 可寫，初始值為 0
        self.writable_registers = {idx: 0 for idx in range(3)}

        # 40004~40008 根據規則隨機變動
        self.data = {idx: self.init_random_value(*params) for idx, params in update_intervals.items()}

    @staticmethod
    def init_random_value(interval, min_val, max_val):
        return {"interval": interval, "range": (min_val, max_val), "last_update": time.time(), "value": random.randint(min_val, max_val)}

    def update_random_values(self):
        """更新 40004~40008 的隨機數據"""
        current_time = time.time()
        for reg, info in self.data.items():
            if "interval" in info and current_time - info["last_update"] >= info["interval"]:
                info["value"] = random.randint(*info["range"])
                info["last_update"] = current_time

    def handle_writes(self):
        """檢查客戶端是否寫入 40001~40003"""
        for reg in self.writable_registers:
            new_value = self.slave.get_values("holding_registers", reg)[0]
            if new_value != self.writable_registers[reg]:  # 如果值變了，就更新
                self.writable_registers[reg] = new_value
                print(f"Register 4X{reg+1} updated by client: {new_value}")

    def run(self):
        try:
            while True:
                time.sleep(1)
                self.update_random_values()
                self.handle_writes()

                # 更新 Modbus 寄存器值
                for reg, value in self.writable_registers.items():
                    self.slave.set_values("holding_registers", reg, value)

                for reg, info in self.data.items():
                    self.slave.set_values("holding_registers", reg, info["value"])

                # 讀取所有 Holding Registers 並輸出
                read_values = self.slave.get_values("holding_registers", 0, 8)
                print(f'Poll 4X={read_values}')
        except Exception as e:
            print(f"Error: {e}")
        finally:
            print('Server Stop!')
            self.tcpserver.stop()

if __name__ == "__main__":
    update_intervals = {
        3: (60, 50, 55),
        4: (60, 20, 23),
        5: (60, 24, 26),
        6: (60, 60, 65),
        7: (120, 650, 665)
    }
    simulator = ModbusSimulator(update_intervals=update_intervals)
    simulator.run()
