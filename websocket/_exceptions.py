"""
_exceptions.py
websocket - WebSocket client library for Python

Copyright 2026 engn33r

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from typing import Any, Optional, Union


class WebSocketException(Exception):
    """
    WebSocket exception class.
    """

    pass


class WebSocketProtocolException(WebSocketException):
    """
    If the WebSocket protocol is invalid, this exception will be raised.
    """

    pass


class WebSocketPayloadException(WebSocketException):
    """
    If the WebSocket payload is invalid, this exception will be raised.
    """

    pass


class WebSocketConnectionClosedException(WebSocketException):
    """
    If remote host closed the connection or some network error happened,
    this exception will be raised.
    """

    pass


class WebSocketTimeoutException(WebSocketException):
    """
    WebSocketTimeoutException will be raised at socket timeout during read/write data.
    """

    pass


class WebSocketProxyException(WebSocketException):
    """
    WebSocketProxyException will be raised when proxy error occurred.
    """

    pass


class WebSocketBadStatusException(WebSocketException):
    """
    WebSocketBadStatusException will be raised when we get bad handshake status code.
    """

    def __init__(
        self,
        message: str,
        status_code: int,
        status_message: Optional[str] = None,
        resp_headers: Optional[dict] = None,
        resp_body: Optional[bytes] = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.status_message = status_message
        self.resp_headers = resp_headers
        self.resp_body = resp_body

    def __reduce__(self) -> Union[str, tuple[Any, ...]]:
        # The default rebuilds the exception from self.args, which holds only
        # the message, so pickling it (e.g. back from a ProcessPoolExecutor
        # worker) and copying it raised TypeError. Pass every constructor
        # argument; __dict__ keeps any other attributes, as the default does.
        # A subclass with its own __init__ keeps the default.
        if type(self).__init__ is not WebSocketBadStatusException.__init__:
            return super().__reduce__()
        return (
            self.__class__,
            (
                self.args[0],
                self.status_code,
                self.status_message,
                self.resp_headers,
                self.resp_body,
            ),
            self.__dict__,
        )


class WebSocketAddressException(WebSocketException):
    """
    If the websocket address info cannot be found, this exception will be raised.
    """

    pass
