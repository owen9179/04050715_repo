[
    {
        "id": "252f54b7.de80ac",
        "type": "tab",
        "label": "Flow 2"
    },
    {
        "id": "95034056.360ad",
        "type": "inject",
        "z": "252f54b7.de80ac",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": false,
        "x": 175.10000610351562,
        "y": 98.00000286102295,
        "wires": [
            [
                "fa01ad18.f09c1"
            ]
        ]
    },
    {
        "id": "fa01ad18.f09c1",
        "type": "function",
        "z": "252f54b7.de80ac",
        "name": "Payload",
        "func": "msg.headers={\n    deviceKey: \"vkILIBPxtr1yONXe\"\n};\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 160,
        "wires": [
            [
                "7d5a4f99.b2da1"
            ]
        ]
    },
    {
        "id": "7d5a4f99.b2da1",
        "type": "http request",
        "z": "252f54b7.de80ac",
        "name": "",
        "method": "GET",
        "ret": "txt",
        "url": "http://api.mediatek.com/mcs/v2/devices/Do0e4SFa/datachannels/Humidity/datapoints.csv",
        "tls": "",
        "x": 450,
        "y": 240,
        "wires": [
            [
                "fec68268.2ae87",
                "5dcf56c8.2d4158"
            ]
        ]
    },
    {
        "id": "fec68268.2ae87",
        "type": "http response",
        "z": "252f54b7.de80ac",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 770,
        "y": 280,
        "wires": []
    },
    {
        "id": "5dcf56c8.2d4158",
        "type": "debug",
        "z": "252f54b7.de80ac",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 730,
        "y": 360,
        "wires": []
    }
]
