# N1081A DT1081A SDK  WEB SOCKET API REFERENCE GUIDE AND PYTHON SDK 

### NIM Four-Fold Programmable Logic Unit
-   Double-width NIM unit
-   Wide range of  **user-selectable functionalities:** logic functions, counting, timing, digital pulse generator.
-   4 independent sections, each with:
    -   6 NIM/TTL input
    -   4 NIM/TTL output
-   **Gate&Delay** and  **discriminator**  input stage
-   **2.8” touch screen display** with user-friendly widgets to configure each section and monitor real-time data
-   Ethernet (1 Gbps) and USB2.0 connectivity
-   **Web-based Graphical User Interface** to remotely control the module and access advanced features

![enter image description here](https://www.caen.it/wp-content/uploads/2019/09/N1081A-W5.jpg)
The N1081A is a  **laboratory tool** that incorporates in a single NIM module the most common functionalities that you need to implement the  **logic capabilities** of your experiment.

The module is organized in four sections, with 6 inputs and 4 outputs each (selectable impedance) accepting TTL/NIM signals. Each section is configurable independently according to one of the available  **pre-programmed functions**, like scaler, counter, time stamping, digital pulse generator, etc. The section programming can be done using the  **2.8” touch screen display**  or via the  **web-interface**. Each section integrates a discriminator with programmable threshold and an asynchronous Gate&Delay with 5 ns resolution. This allows the user to trim at best the needed parameters and to perform accurate measurements.

On the touch screen interface, each function is associated to a  **widget**, for quick configuration and monitor purposes, and an online help with cabling instructions is directly accessible on the display.

The  **web-interface** allows the user to remotely configure the instrument, monitor the functions output, dump data on file or history chart and access to the most advanced features, like the logic analyser and the configuration of advanced functions. No software installation is required!

## Websocket interface

N1081A use a JSON based Web Socket API to both configure the device and retrieve data from the instrument.

Web Socket protocol provides a full-duplex communication channel over a single TCP connection. Most browsers support the Web Socket protocol and provide a client to easily communicate with the Web Socket server on the device.

The URL that has to be used to open the web socket communication is: ws://<N1081A_ip>:8080/
The N1081A_ip is shown on the instrument display home page.

All the request that can be sent to the device and all the messages received by the device are in a JSON format.
N1081A API support multiple users simultaneously connected to the instrument. During the developing, it is possible to keep the browser open on the N1081A page in order see in live the effect of the performed operation.

In order to test the Websocket interface use a software like the Google Chrome extension Simple Websocket Client

[Refer to the PDF in docs folder as user guide for the API](https://github.com/NuclearInstruments/N1081A_SDK_Python/blob/master/docs/N1081A_SDK_Python.pdf)

## Python Library

A Python library is provided to remote control the instrument. The Python works with pyton 2.7 and above.

The library depends from:
 - websocket
 - json

In order to install depedancis:

`pip install websocket-client`

json is already integrated in python




	
 
 
  
