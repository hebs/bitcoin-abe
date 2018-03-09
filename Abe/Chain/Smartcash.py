# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

#**thehebs 3/5/2018 Changed ZCoin to Smartcash on line 23

#from . import BaseChain
#from .. import util
#from pprint import pprint

#class Smartcash(BaseChain):
    #"""
    #A blockchain using 256-bit SHA3 (Keccak) as the block header hash.
    #"""
    #def block_header_hash(chain, header):
        #pprint (vars(chain))
        #return util.sha3_256(header)

from .KeccakChain import KeccakChain

class Smartcash(KeccakChain):
    def __init__(chain, **kwargs):
        chain.name = 'Smartcash'
        chain.code3 = 'SMT'
        chain.address_version ='\x00'
        chain.script_addr_vers = '\x05'
        chain.magic = '\x5c\xa1\xab\x1e'
        KeccakChain.__init__(chain, **kwargs)

