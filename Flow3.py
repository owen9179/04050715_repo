[
    {
        "id": "a7aab26a.ab97f",
        "type": "tab",
        "label": "Flow 3"
    },
    {
        "id": "9fdb2351.71a92",
        "type": "inject",
        "z": "a7aab26a.ab97f",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "x": 165,
        "y": 84.00000190734863,
        "wires": [
            [
                "4457b6f3.7017c8",
                "18eef3f5.5eff5c"
            ]
        ]
    },
    {
        "id": "4457b6f3.7017c8",
        "type": "function",
        "z": "a7aab26a.ab97f",
        "name": "Payload",
        "func": "msg.headers={\n  deviceKey: \"vkILIBPxtr1yONXe\"\n};\nmsg.payload= \"Humidity,,25.3\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 140,
        "wires": [
            [
                "ab568721.087828"
            ]
        ]
    },
    {
        "id": "ab568721.087828",
        "type": "http request",
        "z": "a7aab26a.ab97f",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/Do0e4SFa/datapoints.csv",
        "tls": "",
        "x": 510,
        "y": 140,
        "wires": [
            [
                "82e7d520.d3c6e8",
                "44aad084.777d3"
            ]
        ]
    },
    {
        "id": "82e7d520.d3c6e8",
        "type": "http response",
        "z": "a7aab26a.ab97f",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 733.1000366210938,
        "y": 183,
        "wires": []
    },
    {
        "id": "44aad084.777d3",
        "type": "debug",
        "z": "a7aab26a.ab97f",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "payload",
        "x": 749.1000366210938,
        "y": 244,
        "wires": []
    },
    {
        "id": "18eef3f5.5eff5c",
        "type": "function",
        "z": "a7aab26a.ab97f",
        "name": "Payload",
        "func": "msg.headers={\n  deviceKey: \"vkILIBPxtr1yONXe\"\n};\nmsg.payload= \"Temperature,,87.7\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 320,
        "y": 220,
        "wires": [
            [
                "ab568721.087828"
            ]
        ]
    }
]
