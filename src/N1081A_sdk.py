import json
from websocket import create_connection
from enum import Enum


class N1081A:

    API_ENDPOINT = ""

    class Section(Enum):
        SEC_A = 0
        SEC_B = 1
        SEC_C = 2
        SEC_D = 3

    class FunctionType(Enum):
        FN_WIRE = "wire"
        FN_AND = "and"
        FN_OR = "or"
        FN_OR_VETO = "or_veto"
        FN_VETO = "veto"
        FN_MAJORITY = "majority"
        FN_MAJORITY_VETO = "majority_veto"
        FN_LUT = "lut"
        FN_COINCIDENCE_GATE = "coincidence_gate"
        FN_SCALER = "scaler"
        FN_COUNTER = "counter"
        FN_COUNTER_TIMER = "counter_timer"
        FN_CHRONOMETER = "chronom"
        FN_RATE_METER = "rate_meter"
        FN_RATE_METER_ADVANCED = "rate_meter_advanced"
        FN_TIME_TAG = "time_tag"
        FN_TIME_OF_FLIGHT = "tof"
        FN_TIME_OVER_THRESHOLD = "tot"
        FN_PULSE_GENERATOR = "pulse_generator"
        FN_DIGITAL_GENERATOR = "digital_generator"
        FN_PATTERN_GENERATOR = "pattern_generator"

    class FileMode(Enum):
        FILE_EXISTING = 0
        FILE_NEW = 1

    class CoincidenceTriggerMode(Enum):
        TRIGGER_FIRST = 0
        TRIGGER_1 = 1
        TRIGGER_2 = 2
        TRIGGER_3 = 3
        TRIGGER_4 = 4
        TRIGGER_5 = 5

    class CounterTimerMode(Enum):
        CT_FREE = 0
        CT_COUNT_DOWN = 1
        CT_TARGET = 2
        CT_WINDOW = 3

    class CounterTimerTime(Enum):
        CT_10ns = 0
        CT_1us = 1
        CT_1ms = 2
        CT_1s = 3

    class CounterTimerSource(Enum):
        CT_INPUT = 0
        CT_TIME = 1

    class ChronometerMode(Enum):
        CM_GATE = 0
        CM_START_STOP = 1

    class FilterMode(Enum):
        FILTER_OFF = 0
        FILTER_VERY_SLOW = 1
        FILTER_SLOW = 2
        FILTER_MEDIUM = 3
        FILTER_FAST = 4
        FILTER_VERY_FAST = 5

    class IntegrationTimeMode(Enum):
        TIME_1ms = 0
        TIME_100ms = 1
        TIME_500ms = 2
        TIME_1s = 3
        TIME_5s = 4
        TIME_10s = 5
        TIME_30s = 6
        TIME_1min = 7
        TIME_10min = 8
        TIME_1h = 9

    class WindowsMode(Enum):
        WINDOWS_FIXED = 0
        WINDOWS_CUSTOM = 1

    class T0Mode(Enum):
        T0_EXTERNAL = 0
        T0_INTERNAL = 1

    class StatisticMode(Enum):
        STAT_DETERMINISTIC = 0
        STAT_POISSON = 1

    class LogicAnalyzerTriggerMode(Enum):
        LA_TRIGGER_AND = 0
        LA_TRIGGER_OR = 1
        LA_TRIGGER_OFF = 2

    class LogicAnalyzerTriggerEdge(Enum):
        LA_EDGE_RISING = 0
        LA_EDGE_FALLING = 1

    class SignalStandard(Enum):
        STANDARD_NIM = 0
        STANDARD_TTL = 1
        STANDARD_DISCRIMINATOR = 2

    class SignalImpedance(Enum):
        IMPEDANCE_50 = "true"
        IMPEDANCE_HIGH = "false"

    def __init__(self, ip):
        self.API_ENDPOINT = "ws://" + ip + ":8080/"

    def __int_to_str(self, value):
        return str(value)

    def __bool_to_str(self, value):
        return (str(value)).lower()

    def set_section_function(self, section, function):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"select_section_function", "callback":"set_fn", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "function":"' + function.value + '"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_sections_function(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_all_sections_function", "callback":"get_fn"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def __config_logic4(self, section, function, enable0, enable1, enable2, enable3):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"' + function + '", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                    + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":'
                    + self.__bool_to_str(enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}]}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def __config_logic5(self, section, function, enable0, enable1, enable2, enable3, enable4, bypass_enable, bypass_ind):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"' + function + '", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                    + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":'
                    + self.__bool_to_str(enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                    + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4) + '}], "bypass_enable":'
                    + self.__bool_to_str(bypass_enable) + ', "bypass_section":' + self.__int_to_str(bypass_ind) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def __config_logic6(self, section, function, enable0, enable1, enable2, enable3, enable4, enable5, bypass_enable, bypass_ind):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"' + function + '", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                    + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":'
                    + self.__bool_to_str(enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                    + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4) + '}, {"lemo":5, "enable":'
                    + self.__bool_to_str(enable5) + '}], "bypass_enable":' + self.__bool_to_str(bypass_enable)
                    + ', "bypass_section":' + self.__int_to_str(bypass_ind) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_wire(self, section, enable0, enable1, enable2, enable3):
        self.__config_logic4(section, "wire", enable0, enable1, enable2, enable3)

    def configure_and(self, section, enable0, enable1, enable2, enable3, enable4, enable5, bypass_enable, bypass_ind):
        self.__config_logic6(section, "and", enable0, enable1, enable2, enable3, enable4, enable5, bypass_enable, bypass_ind)

    def configure_or(self, section, enable0, enable1, enable2, enable3, enable4, enable5, bypass_enable, bypass_ind):
        self.__config_logic6(section, "or", enable0, enable1, enable2, enable3, enable4, enable5, bypass_enable, bypass_ind)

    def configure_or_veto(self, section, enable0, enable1, enable2, enable3, enable4, bypass_enable, bypass_ind):
        self.__config_logic5(section, "or_veto", enable0, enable1, enable2, enable3, enable4, bypass_enable, bypass_ind)

    def configure_veto(self, section, enable0, enable1, enable2, enable3):
        self.__config_logic4(section, "veto", enable0, enable1, enable2, enable3)

    def configure_majority(self, section, enable0, enable1, enable2, enable3, enable4, enable5):
        self.__config_logic6(section, "majority", enable0, enable1, enable2, enable3, enable4, enable5, False, 0)

    def configure_majority_veto(self, section, enable0, enable1, enable2, enable3, enable4):
        self.__config_logic5(section, "majority_veto", enable0, enable1, enable2, enable3, enable4, False, 0)

    def configure_lut(self, section, i_enable0, i_enable1, i_enable2, i_enable3, i_enable4, i_enable5, o_enable0,
                      o_enable1, o_enable2, o_enable3, file_mode, file_name, file_content, file_lines):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if file_mode == self.FileMode.FILE_EXISTING:
                ws.send('{"command":"configure_function", "callback":"lut_old", "params":{"section":' + self.__int_to_str(section.value)
                        + ', "lemo_out_enables":[{"lemo":0, "enable":' + self.__bool_to_str(o_enable0)
                        + '}, {"lemo":1, "enable":' + self.__bool_to_str(o_enable1) + '}, {"lemo":2, "enable":'
                        + self.__bool_to_str(o_enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(o_enable3)
                        + '}], "lemo_in_enables":[{"lemo":0, "enable":' + self.__bool_to_str(i_enable0) + '}, {"lemo":1, "enable":'
                        + self.__bool_to_str(i_enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(i_enable2)
                        + '}, {"lemo":3, "enable":' + self.__bool_to_str(i_enable3) + '}, {"lemo":4, "enable":'
                        + self.__bool_to_str(i_enable4) + '}, {"lemo":5, "enable":' + self.__bool_to_str(i_enable5)
                        + '}], "file_mode":0, "file_name":"' + file_name + '"}}')
            if file_mode == self.FileMode.FILE_NEW:
                ws.send('{"command":"configure_function", "callback":"lut_new", "params":{"section":' + self.__int_to_str(section.value)
                        + ', "lemo_out_enables":[{"lemo":0, "enable":' + self.__bool_to_str(o_enable0)
                        + '}, {"lemo":1, "enable":' + self.__bool_to_str(o_enable1) + '}, {"lemo":2, "enable":'
                        + self.__bool_to_str(o_enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(o_enable3)
                        + '}], "lemo_in_enables":[{"lemo":0, "enable":' + self.__bool_to_str(i_enable0) + '}, {"lemo":1, "enable":'
                        + self.__bool_to_str(i_enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(i_enable2)
                        + '}, {"lemo":3, "enable":' + self.__bool_to_str(i_enable3) + '}, {"lemo":4, "enable":'
                        + self.__bool_to_str(i_enable4) + '}, {"lemo":5, "enable":' + self.__bool_to_str(i_enable5)
                        + '}], "file_mode":1, "file_name":"' + file_name + '", "lut_values":' + file_content
                        + ', "total_number":' + self.__int_to_str(file_lines) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_coincidence_gate(self, section, enable0, enable1, enable2, enable3, enable4, coinc0, coinc1, coinc2,
                                   coinc3, coinc4, enable_gate, close_on_coinc, delay, width, trigger_mode):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"coincidence", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                    + ', "coincidence":' + self.__bool_to_str(coinc0) + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1)
                    + ', "coincidence":' + self.__bool_to_str(coinc1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + ', "coincidence":' + self.__bool_to_str(coinc2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                    + ', "coincidence":' + self.__bool_to_str(coinc3) + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4)
                    + ', "coincidence":' + self.__bool_to_str(coinc4) + '}], "gate":' + self.__bool_to_str(enable_gate)
                    + ', "close_on_coincidence":' + self.__bool_to_str(close_on_coinc) + ', "delay":' + self.__int_to_str(delay)
                    + ', "width":' + self.__int_to_str(width) + ', "trigger":' + self.__int_to_str(trigger_mode.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_scaler(self, section, scale, enable0, enable1, enable2, enable3, enable_gate):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"scaler", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "scale":' + self.__int_to_str(scale) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                    + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}], "gate":' + self.__bool_to_str(enable_gate) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_counter(self, section, enable0, enable1, enable2, enable3, enable_gate):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"counter", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}], "gate":' + self.__bool_to_str(enable_gate) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_counter_timer(self, section, enable0, enable1, enable_gate, auto_reset, gate1_width, gate2_width,
                                source_mode, time, counter_mode, target1, target2):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"counter_timer", "params": {"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}], "gate":' + self.__bool_to_str(enable_gate) + ', "auto_reset":'
                    + self.__bool_to_str(auto_reset) + ', "gate_width1":' + self.__int_to_str(gate1_width) + ', "gate_width2":'
                    + self.__int_to_str(gate2_width) + ', "source":' + self.__int_to_str(source_mode.value)
                    + ', "time":' + self.__int_to_str(time.value) + ', "mode":' + self.__int_to_str(counter_mode.value)
                    + ', "target1":' + self.__int_to_str(target1) + ', "target2":' + self.__int_to_str(target2) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_chronometer(self, section, frequency, chronometer_mode, enable0, enable1, enable_gate, reset_on_gate, reset_on_stop):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"chronometer", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "frequency":' + self.__int_to_str(frequency) + ', "mode":' + self.__int_to_str(chronometer_mode.value)
                    + ', "reset_gate":' + self.__bool_to_str(reset_on_gate) + ', "reset_stop":' + self.__bool_to_str(reset_on_stop)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}], "gate":' + self.__bool_to_str(enable_gate) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_rate_meter(self, section, enable0, enable1, enable2, enable3, enable_gate):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"rate_meter", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}], "gate":' + self.__bool_to_str(enable_gate) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_rate_meter_advanced(self, section, enable0, enable1, enable2, enable3, enable_gate, enable_alarm,
                                      threshold0, threshold1, threshold2, threshold3, filter_mode, integration_time):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"rate_meter_advanced", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}], "thresholds":[{"lemo":0, "threshold":'
                    + self.__int_to_str(threshold0) + '}, {"lemo":1, "threshold":' + self.__int_to_str(threshold1)
                    + '}, {"lemo":2, "threshold":' + self.__int_to_str(threshold2) + '}, {"lemo":3, "threshold":' + self.__int_to_str(threshold3)
                    + '}], "gate":' + self.__bool_to_str(enable_gate) + ', "alarm":' + self.__bool_to_str(enable_alarm)
                    + ', "filter":' + self.__int_to_str(filter_mode.value) + ', "int_time":' + self.__int_to_str(integration_time.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_time_tagging(self, section, enable0, enable1, enable2, enable3, enable4, enable5):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"time_tagging", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4)
                    + '}, {"lemo":5, "enable":' + self.__bool_to_str(enable5) + '}]}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_time_of_flight(self, section, enable0, enable1, enable3, enable4, windows_mode, windows_value, windows_number,
                                 file_mode, file_name, file_content, file_windows_number, t0_mode, t0_frequency, t0_reset):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if windows_mode == self.WindowsMode.WINDOWS_FIXED:
                ws.send('{"command":"configure_function", "callback":"time_of_flight", "params":{"section":' + self.__int_to_str(section.value)
                        + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                        + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":true}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                        + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4) + '}, {"lemo":5, "enable":true}], "win_mode":0'
                        + ', "win_value":' + self.__int_to_str(windows_value) + ', "win_number":' + self.__int_to_str(windows_number)
                        + ', "t0_mode":' + self.__int_to_str(t0_mode.value) + ', "t0_value":' + self.__int_to_str(t0_frequency)
                        + ', "t0_reset":' + self.__bool_to_str(t0_reset) + '}}')
            if windows_mode == self.WindowsMode.WINDOWS_CUSTOM and file_mode == self.FileMode.FILE_EXISTING:
                ws.send('{"command":"configure_function", "callback": "time_of_flight", "params":{"section":' + self.__int_to_str(section.value)
                        + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                        + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":true}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                        + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4) + '}, {"lemo":5, "enable":true}], "win_mode":1'
                        + ', "file_mode":0, "file_name":"' + file_name + '", "t0_mode":' + self.__int_to_str(t0_mode.value)
                        + ', "t0_value":' + self.__int_to_str(t0_frequency) + ', "t0_reset":' + self.__bool_to_str(t0_reset) + '}}')
            if windows_mode == self.WindowsMode.WINDOWS_CUSTOM and file_mode == self.FileMode.FILE_NEW:
                ws.send('{"command":"configure_function", "callback":"time_of_flight", "params":{"section":' + self.__int_to_str(section.value)
                        + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                        + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":true}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                        + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4) + '}, {"lemo":5, "enable":true}], "win_mode":1'
                        + ', "file_mode":1, "file_name":"' + file_name + '", "win_values":' + file_content + ', "win_number":'
                        + self.__int_to_str(file_windows_number) + ', "t0_mode":' + self.__int_to_str(t0_mode.value)
                        + ', "t0_value":' + self.__int_to_str(t0_frequency) + ', "t0_reset":' + self.__bool_to_str(t0_reset) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_time_over_threshold(self, section, enable0, enable1, enable3, enable4, windows_value, windows_number):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"time_over_threshold", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":true}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                    + '}, {"lemo":4, "enable":' + self.__bool_to_str(enable4) + '}, {"lemo":5, "enable":true}], "win_mode":0'
                    + ', "win_value":' + self.__int_to_str(windows_value) + ', "win_number":' + self.__int_to_str(windows_number) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_pulse_generator(self, section, statistics_mode, width, frequency, enable0, enable1, enable2, enable3):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"pulse_generator", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "frequency_type":' + self.__int_to_str(statistics_mode.value) + ', "width":' + self.__int_to_str(width)
                    + ', "frequency":' + self.__int_to_str(frequency) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                    + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}]}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_digital_generator(self, section, enable0, enable1, enable2, enable3):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_function", "callback":"digital_generator", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0) + '}, {"lemo":1, "enable":'
                    + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":' + self.__bool_to_str(enable2)
                    + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3) + '}]}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def configure_pattern_generator(self, section, enable0, enable1, enable2, enable3, frequency,
                                                  file_mode, file_name, file_content, file_lines):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if file_mode == self.FileMode.FILE_EXISTING:
                ws.send('{"command":"configure_function", "callback":"pattern_generator", "params":{"section":'
                        + self.__int_to_str(section.value) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                        + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":'
                        + self.__bool_to_str(enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                        + '}], "frequency":' + self.__int_to_str(frequency) + ', "file_mode":0, "file_name":"' + file_name + '"}}')
            if file_mode == self.FileMode.FILE_NEW:
                ws.send('{"command":"configure_function", "callback":"pattern_generator_new", "params":{"section":'
                        + self.__int_to_str(section.value) + ', "lemo_enables":[{"lemo":0, "enable":' + self.__bool_to_str(enable0)
                        + '}, {"lemo":1, "enable":' + self.__bool_to_str(enable1) + '}, {"lemo":2, "enable":'
                        + self.__bool_to_str(enable2) + '}, {"lemo":3, "enable":' + self.__bool_to_str(enable3)
                        + '}], "frequency":' + self.__int_to_str(frequency) + ', "file_mode":1, "file_name":"' + file_name
                        + '", "pattern_values":' + file_content + ', "total_number":' + self.__int_to_str(file_lines) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_function_configuration(self, section):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_function_config", "callback":"get_config", "params":{"section":' + self.__int_to_str(section.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_function_results(self, section):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_function_results", "callback":"get_results", "params":{"section":' + self.__int_to_str(section.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def reset_channel(self, section, channel, function):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if function == self.FunctionType.FN_CHRONOMETER or function == self.FunctionType.FN_COUNTER or function == self.FunctionType.FN_COUNTER_TIMER or function == self.FunctionType.FN_RATE_METER_ADVANCED or function == self.FunctionType.FN_SCALER:
                ws.send('{"command":"reset_channel", "callback":"reset_ch", "params":{"section":' + self.__int_to_str(section.value)
                        + ', "channel":' + self.__int_to_str(channel) + '}}')
            if function == self.FunctionType.FN_COINCIDENCE_GATE:
                ws.send('{"command":"reset_channel", "callback":"reset_ch", "params":{"section":' + self.__int_to_str(section.value) + ', "channel":0}}')
            if function == self.FunctionType.FN_TIME_OF_FLIGHT or function == self.FunctionType.FN_TIME_OVER_THRESHOLD:
                ws.send('{"command":"reset_channel", "callback":"reset_ch", "params":{"section":' + self.__int_to_str(section.value) + ', "channel":2}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def start_acquisition(self, section, function):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if function == self.FunctionType.FN_LUT or function == self.FunctionType.FN_PATTERN_GENERATOR or function == self.FunctionType.FN_TIME_OF_FLIGHT or function == self.FunctionType.FN_TIME_OVER_THRESHOLD:
                ws.send('{"command":"reset_channel", "callback":"start", "params":{"section":' + self.__int_to_str(section.value) + ', "channel":1}}')
            if function == self.FunctionType.FN_TIME_TAG:
                ws.send('{"command":"reset_channel", "callback":"start", "params":{"section":' + self.__int_to_str(section.value) + ', "channel":1}}')
                ws.send('{"command":"start_tt_data", "callback":"start", "params":{"section":' + self.__int_to_str(section.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def stop_acquisition(self, section, function):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if function == self.FunctionType.FN_LUT or function == self.FunctionType.FN_PATTERN_GENERATOR or function == self.FunctionType.FN_TIME_OF_FLIGHT or function == self.FunctionType.FN_TIME_OVER_THRESHOLD:
                ws.send('{"command":"reset_channel", "callback":"stop", "params":{"section":' + self.__int_to_str(section.value) + ', "channel":0}}')
            if function == self.FunctionType.FN_TIME_TAG:
                ws.send('{"command":"reset_channel", "callback":"stop", "params":{"section":' + self.__int_to_str(section.value) + ', "channel":0}}')
                ws.send('{"command":"stop_tt_data", "callback":"stop", "params":{"section":' + self.__int_to_str(section.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_function_file_list(self, function):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if function == self.FunctionType.FN_LUT:
                ws.send('{"command":"get_config_file", "callback":"get_file", "function":"lut"}')
            if function == self.FunctionType.FN_PATTERN_GENERATOR:
                ws.send('{"command":"get_config_file", "callback":"get_file", "function":"pattern"}')
            if function == self.FunctionType.FN_TIME_OF_FLIGHT:
                ws.send('{"command":"get_config_file", "callback":"get_file", "function":"width"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def download_function_file(self, function, file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if function == self.FunctionType.FN_LUT:
                ws.send('{"command":"download_config", "callback":"download_file", "params":{"file_name":"' + file_name + '", "function":"lut"}}')
            if function == self.FunctionType.FN_PATTERN_GENERATOR:
                ws.send('{"command":"download_config", "callback":"download_file", "params":{"file_name":"' + file_name + '", "function":"pattern"}}')
            if function == self.FunctionType.FN_TIME_OF_FLIGHT:
                ws.send('{"command":"download_config", "callback":"download_file", "params":{"file_name":"' + file_name + '", "function":"width"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def delete_function_file(self, function, file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            if function == self.FunctionType.FN_LUT:
                ws.send('{"command":"delete_config", "callback":"delete_file", "params":{"file_name":"' + file_name + '", "function":"lut"}}')
            if function == self.FunctionType.FN_PATTERN_GENERATOR:
                ws.send('{"command":"delete_config", "callback":"delete_file", "params":{"file_name":"' + file_name + '", "function":"pattern"}}')
            if function == self.FunctionType.FN_TIME_OF_FLIGHT:
                ws.send('{"command":"delete_config", "callback":"delete_file", "params":{"file_name":"' + file_name + '", "function":"width"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_input_configuration(self, section, standard, threshold, impedance):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_input", "callback":"input_cfg", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "standard":' + self.__int_to_str(standard.value) + ', "threshold":' + self.__int_to_str(threshold)
                    + ', "imp":"' + impedance.value + '"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_input_configuration(self, section):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_input_config", "callback":"get_input_config", "params":{"section":' + self.__int_to_str(section.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_input_channel_configuration(self, section, channel, status, enable_gate_delay, gate, delay, invert):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_input_channel", "callback":"set_input_ch_config", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "channel":' + self.__int_to_str(channel) + ', "status":' + self.__bool_to_str(status)
                    + ', "enable_gd":' + self.__bool_to_str(enable_gate_delay) + ', "gate":' + self.__int_to_str(gate)
                    + ', "delay":' + self.__int_to_str(delay) + ', "invert":' + self.__bool_to_str(invert) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_input_channel_configuration(self, section, channel):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_input_channel_config", "callback":"get_input_ch_config", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "channel":' + self.__int_to_str(channel) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_output_configuration(self, section, standard, impedance):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_output", "callback":"output_cfg", "params":{"section":' + self.__int_to_str(section.value)
                    + ', "standard":' + self.__int_to_str(standard.value) + ', "imp":"' + impedance.value + '"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_output_configuration(self, section):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_output_config", "callback":"get_output_config", "params":{"section":' + self.__int_to_str(section.value) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_output_channel_configuration(self, section, channel, status, enable_monostable, monostable, invert):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_output_channel", "callback":"set_output_ch_config", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "channel":' + self.__int_to_str(channel) + ', "status":'
                    + self.__bool_to_str(status) + ', "enable_mono":' + self.__bool_to_str(enable_monostable)
                    + ', "mono_value":' + self.__int_to_str(monostable) + ', "invert":' + self.__bool_to_str(invert) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_output_channel_configuration(self, section, channel):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_output_channel_config", "callback":"get_output_ch_config", "params":{"section":'
                    + self.__int_to_str(section.value) + ', "channel":' + self.__int_to_str(channel) + '}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def start_logic_analyzer(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"la_arm", "callback":"logic_analyzer"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_logic_analyzer_trigger(self, trigger_mode_in, trigger_mode_out, edge, sec1_in1, sec1_in2, sec1_in3, sec1_in4, sec1_in5, sec1_in6,
                                   sec1_out1, sec1_out2, sec1_out3, sec1_out4, sec2_in1, sec2_in2, sec2_in3, sec2_in4, sec2_in5, sec2_in6,
                                   sec2_out1, sec2_out2, sec2_out3, sec2_out4, sec3_in1, sec3_in2, sec3_in3, sec3_in4, sec3_in5, sec3_in6,
                                   sec3_out1, sec3_out2, sec3_out3, sec3_out4, sec4_in1, sec4_in2, sec4_in3, sec4_in4, sec4_in5, sec4_in6,
                                   sec4_out1, sec4_out2, sec4_out3, sec4_out4):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"configure_la_trigger", "callback":"logic_analyzer", "params":{"file_content":{"mode_in":'
                    + self.__int_to_str(trigger_mode_in.value) + ', "mode_out":' + self.__int_to_str(trigger_mode_out.value)
                    + ', "edge":' + self.__int_to_str(edge.value) + ', "auto":0, "sec1_in1":' + self.__bool_to_str(sec1_in1)
                    + ', "sec1_in2":' + self.__bool_to_str(sec1_in2) + ', "sec1_in3":' + self.__bool_to_str(sec1_in3)
                    + ', "sec1_in4":' + self.__bool_to_str(sec1_in4) + ', "sec1_in5":' + self.__bool_to_str(sec1_in5)
                    + ', "sec1_in6":' + self.__bool_to_str(sec1_in6) + ', "sec1_out1":' + self.__bool_to_str(sec1_out1)
                    + ', "sec1_out2":' + self.__bool_to_str(sec1_out2) + ', "sec1_out3":' + self.__bool_to_str(sec1_out3)
                    + ', "sec1_out4":' + self.__bool_to_str(sec1_out4) + ', "sec2_in1":' + self.__bool_to_str(sec2_in1)
                    + ', "sec2_in2":' + self.__bool_to_str(sec2_in2) + ', "sec2_in3":' + self.__bool_to_str(sec2_in3)
                    + ', "sec2_in4":' + self.__bool_to_str(sec2_in4) + ', "sec2_in5":' + self.__bool_to_str(sec2_in5)
                    + ', "sec2_in6":' + self.__bool_to_str(sec2_in6) + ', "sec2_out1":' + self.__bool_to_str(sec2_out1)
                    + ', "sec2_out2":' + self.__bool_to_str(sec2_out2) + ', "sec2_out3":' + self.__bool_to_str(sec2_out3)
                    + ', "sec2_out4":' + self.__bool_to_str(sec2_out4) + ', "sec3_in1":' + self.__bool_to_str(sec3_in1)
                    + ', "sec3_in2":' + self.__bool_to_str(sec3_in2) + ', "sec3_in3":' + self.__bool_to_str(sec3_in3)
                    + ', "sec3_in4":' + self.__bool_to_str(sec3_in4) + ', "sec3_in5":' + self.__bool_to_str(sec3_in5)
                    + ', "sec3_in6":' + self.__bool_to_str(sec3_in6) + ', "sec3_out1":' + self.__bool_to_str(sec3_out1)
                    + ', "sec3_out2":' + self.__bool_to_str(sec3_out2) + ', "sec3_out3":' + self.__bool_to_str(sec3_out3)
                    + ', "sec3_out4":' + self.__bool_to_str(sec3_out4) + ', "sec4_in1":' + self.__bool_to_str(sec4_in1)
                    + ', "sec4_in2":' + self.__bool_to_str(sec4_in2) + ', "sec4_in3":' + self.__bool_to_str(sec4_in3)
                    + ', "sec4_in4":' + self.__bool_to_str(sec4_in4) + ', "sec4_in5":' + self.__bool_to_str(sec4_in5)
                    + ', "sec4_in6":' + self.__bool_to_str(sec4_in6) + ', "sec4_out1":' + self.__bool_to_str(sec4_out1)
                    + ', "sec4_out2":' + self.__bool_to_str(sec4_out2) + ', "sec4_out3":' + self.__bool_to_str(sec4_out3)
                    + ', "sec4_out4":' + self.__bool_to_str(sec4_out4) + '}}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_logic_analyzer_trigger(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_la_trigger_config", "callback":"logic_analyzer"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_logic_analyzer_data(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"la_getdata", "callback":"logic_analyzer"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_ethernet_configuration(self, dhcp, ip, netmask, gateway, dns):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"set_eth_config", "callback":"ethernet_config", "data":{"dhcp":' + self.__int_to_str(dhcp)
                    + ', "ip":"' + ip + '", "nm":"' + netmask + '", "gw":"' + gateway + '", "dns":"' + dns + '"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_ethernet_configuration(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_eth_config", "callback":"ethernet_config"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_configuration_file_list(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_config_file", "callback":"get_cfg_file", "function":"config"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def save_configuration_file(self, file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"create_config", "callback":"save_cfg_file", "params":{"new_name":"' + file_name + '"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def load_configuration_file(self, file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"load_config", "callback":"load_cfg_file", "params":{"file_name":"' + file_name + '"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def upload_configuration_file(self, file_name, file_content):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"upload_config", "callback":"upload_cfg_file", "params":{"file_name":"' + file_name
                    + '", "file_content":' + file_content + ', "function":"config"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def download_configuration_file(self, file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"download_config", "callback":"download_cfg_file", "params":{"file_name":"' + file_name + '", "function":"config"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def delete_configuration_file(self, file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"delete_config", "callback":"delete_cfg_file", "params":{"file_name":"' + file_name + '", "function":"config"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def rename_configuration_file(self, old_file_name, new_file_name):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"rename_config", "callback":"rename_cfg_file", "params":{"old_name":"' + old_file_name
                    + '", "new_name":"' + new_file_name + '", "function":"config"}}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def start_search_device(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"start_alarm", "callback":"search_device"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def stop_search_device(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"stop_alarm", "callback":"search_device"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_search_device_status(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_alarm_status", "callback":"search_device"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def check_clock(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"check_clk", "callback":"clock"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_internal_clock(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"apply_int_clk", "callback":"clock"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def set_external_clock(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"apply_ext_clk", "callback":"clock"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_clock_status(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_clk_status", "callback":"clock"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)

    def get_version(self):
        ws = create_connection(self.API_ENDPOINT)
        if ws.connected:
            ws.send('{"command":"get_version", "callback":"version"}')
            r = ws.recv()
            ws.close()
            return json.loads(r)
