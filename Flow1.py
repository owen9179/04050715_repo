[
    {
        "id": "ea3e76be.217cc8",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "819fcafc.5e9af8",
        "type": "rpi-gpio out",
        "z": "ea3e76be.217cc8",
        "name": "LED",
        "pin": "7",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 730,
        "y": 220,
        "wires": []
    },
    {
        "id": "12396ce8.607383",
        "type": "debug",
        "z": "ea3e76be.217cc8",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 750,
        "y": 300,
        "wires": []
    },
    {
        "id": "33e6e353.8d138c",
        "type": "rpi-gpio in",
        "z": "ea3e76be.217cc8",
        "name": "BUTTON",
        "pin": "16",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 100,
        "y": 280,
        "wires": [
            [
                "e8587927.8e61c8"
            ]
        ]
    },
    {
        "id": "e8587927.8e61c8",
        "type": "switch",
        "z": "ea3e76be.217cc8",
        "name": "SWITCH",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 300,
        "y": 280,
        "wires": [
            [
                "224f4c1e.ea1904"
            ],
            [
                "6cdef6f0.8c1fb8"
            ]
        ]
    },
    {
        "id": "224f4c1e.ea1904",
        "type": "change",
        "z": "ea3e76be.217cc8",
        "name": "CHANGE TO 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 460,
        "y": 240,
        "wires": [
            [
                "819fcafc.5e9af8",
                "12396ce8.607383"
            ]
        ]
    },
    {
        "id": "6cdef6f0.8c1fb8",
        "type": "change",
        "z": "ea3e76be.217cc8",
        "name": "CHANGE TO 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 531,
        "y": 328,
        "wires": [
            [
                "819fcafc.5e9af8",
                "12396ce8.607383"
            ]
        ]
    }
]
