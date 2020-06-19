import pprint
import time
import matplotlib.pyplot as plt
from N1081A_sdk import N1081A

pp = pprint.PrettyPrinter(indent=4)

N1081A_device = N1081A("10.128.2.242")
version_json = N1081A_device.get_version()
pp.pprint(version_json)
serial_number = version_json["data"]["serial_number"]
software_version = version_json["data"]["software_version"]
zynq_version = version_json["data"]["zynq_version"]
fpga_version = version_json["data"]["fpga_version"]

response_json = N1081A_device.set_section_function(N1081A.Section.SEC_A, N1081A.FunctionType.FN_LUT)
pp.pprint(response_json)
response_json = N1081A_device.set_section_function(N1081A.Section.SEC_B, N1081A.FunctionType.FN_RATE_METER)
pp.pprint(response_json)
response_json = N1081A_device.set_section_function(N1081A.Section.SEC_C, N1081A.FunctionType.FN_PULSE_GENERATOR)
pp.pprint(response_json)
response_json = N1081A_device.set_section_function(N1081A.Section.SEC_D, N1081A.FunctionType.FN_TIME_OVER_THRESHOLD)
pp.pprint(response_json)

lut_file = '[{"input": 63, "output": 0}, {"input": 0, "output": 15}, {"input": 21, "output": 0}, {"input": 63, "output": 0}]'
response_json = N1081A_device.configure_lut(N1081A.Section.SEC_A, True, True, True, True, True, True, True, True, True, True, N1081A.FileMode.FILE_NEW, "lut2", lut_file, 4)
pp.pprint(response_json)
response_json = N1081A_device.configure_rate_meter(N1081A.Section.SEC_B, True, True, True, True, True)
pp.pprint(response_json)
response_json = N1081A_device.configure_pulse_generator(N1081A.Section.SEC_C, N1081A.StatisticMode.STAT_DETERMINISTIC, 100, 1000, True, True, True, True)
pp.pprint(response_json)
response_json = N1081A_device.configure_time_over_threshold(N1081A.Section.SEC_D, True, True, True, True, 100, 20)
pp.pprint(response_json)

response_json = N1081A_device.set_input_channel_configuration(N1081A.Section.SEC_D, 0, True, True, 300, 100, False)
pp.pprint(response_json)

response_json = N1081A_device.start_acquisition(N1081A.Section.SEC_A, N1081A.FunctionType.FN_LUT)
pp.pprint(response_json)
response_json = N1081A_device.start_acquisition(N1081A.Section.SEC_D, N1081A.FunctionType.FN_TIME_OVER_THRESHOLD)
pp.pprint(response_json)

f = plt.figure()
graph1 = f.add_subplot(221)
graph2 = f.add_subplot(222, sharex=graph1)
graph3 = f.add_subplot(223, sharex=graph1)
graph4 = f.add_subplot(224, sharex=graph1)

while 1:
    rate_meter_json = N1081A_device.get_function_results(N1081A.Section.SEC_B)
    pp.pprint(rate_meter_json)
    rate1 = rate_meter_json["data"]["counters"][0]["value"]
    rate2 = rate_meter_json["data"]["counters"][1]["value"]
    rate3 = rate_meter_json["data"]["counters"][2]["value"]
    rate4 = rate_meter_json["data"]["counters"][3]["value"]

    time_over_threshold_json = N1081A_device.get_function_results(N1081A.Section.SEC_D)
    pp.pprint(time_over_threshold_json)
    spectrum1 = time_over_threshold_json["data"]["spectrum1"]
    spectrum2 = time_over_threshold_json["data"]["spectrum2"]
    spectrum3 = time_over_threshold_json["data"]["spectrum3"]
    spectrum4 = time_over_threshold_json["data"]["spectrum4"]
    time_bins = time_over_threshold_json["data"]["time"]

    x = []
    for t in range(len(time_bins)):
        if t == 0:
            x.append(time_bins[t])
        else:
            x.append(x[t - 1] + time_bins[t])

    graph1.clear()
    graph2.clear()
    graph3.clear()
    graph4.clear()
    graph1.hist(spectrum1, x)
    graph2.hist(spectrum2, x)
    graph3.hist(spectrum3, x)
    graph4.hist(spectrum4, x)
    plt.show()

    time.sleep(1)
