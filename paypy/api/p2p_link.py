from ..client import BaseClient


class P2PLinkAPI(object):

    def __init__(self,
                 base: BaseClient):
        self.__base = base

    async def get_p2p_link_info(self,
                                verification_code: str):
        pass
