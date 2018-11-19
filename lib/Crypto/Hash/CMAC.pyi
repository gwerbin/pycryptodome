from types import ModuleType
from typing import Union, Dict

Buffer = Union[bytes, bytearray, memoryview]

digest_size: int

class CMAC(object):
    digest_size: int

    def __init__(self,
		 key: Buffer,
                 msg: Buffer,
		 ciphermod: ModuleType,
		 cipher_params: dict,
		 mac_len: int) -> None: ...
    def update(self, data: Buffer) -> CMAC: ...
    def copy(self) -> CMAC: ...
    def digest(self) -> bytes: ...
    def hexdigest(self) -> str: ...
    def verify(self, mac_tag: Buffer) -> None: ...
    def hexverify(self, hex_mac_tag: str) -> None: ...


def new(key: Buffer,
        msg: Buffer = ...,
	ciphermod: ModuleType = ...,
	cipher_params: Dict = ...,
	mac_len: int = ...) -> CMAC: ...
