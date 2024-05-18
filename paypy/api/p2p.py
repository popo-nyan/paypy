from ..client import BaseClient
from ..models import (P2PLinkInfoRequestParamModel)


class P2PLinkAPI(object):

    def __init__(self,
                 base: BaseClient):
        self.__base = base

    async def get_p2p_link_info(self,
                                params: P2PLinkInfoRequestParamModel):
        pass
