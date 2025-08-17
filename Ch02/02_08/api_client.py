import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%dT%H:%M:%S',
)


class APIClient:
    def __init__(self, host):
        self.host = host
        logging.info('client connected to %r', host)
        # TODO: connect to host

    def metrics(self):
        # FIXME: Call real server
        return data
    
    def close(self):
        logging.info('client (%r) closing', self.host)


data = [
    {"time":"2021-07-13T14:36:52.380Z","metric":"mem","value":227551548.0},
    {"time":"2021-07-13T14:36:52.380Z","metric":"cpu","value":30.04},
    {"time":"2021-07-13T14:36:53.337Z","metric":"mem","value":227567864.0},
    {"time":"2021-07-13T14:36:53.337Z","metric":"cpu","value":30.93},
    {"time":"2021-07-13T14:36:54.294Z","metric":"mem","value":227574696.0},
    {"time":"2021-07-13T14:36:54.294Z","metric":"cpu","value":32.61},
    {"time":"2021-07-13T14:36:55.251Z","metric":"mem","value":227567135.0},
    {"time":"2021-07-13T14:36:55.251Z","metric":"cpu","value":32.24},
    {"time":"2021-07-13T14:36:56.208Z","metric":"mem","value":227561333.0},
    {"time":"2021-07-13T14:36:56.208Z","metric":"cpu","value":31.27},
    {"time":"2021-07-13T14:36:57.165Z","metric":"cpu","value":31.33},
    {"time":"2021-07-13T14:36:57.165Z","metric":"mem","value":227586440.0},
]

