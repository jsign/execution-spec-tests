"""
abstract: Tests [EIP-7748: State conversion to Verkle Tree]
(https://eips.ethereum.org/EIPS/eip-7748)
    Tests for [EIP-7748: State conversion to Verkle Tree]
    (https://eips.ethereum.org/EIPS/eip-7748).
"""

import pytest

from ethereum_test_tools import (
    Account,
    Address,
    Block,
    BlockchainTestFiller,
    Environment,
)
from ethereum_test_tools.vm.opcode import Opcodes as Op

REFERENCE_SPEC_GIT_PATH = "EIPS/eip-7748.md"
REFERENCE_SPEC_VERSION = "TODO"

# List of addressed ordered by MPT tree key.
# 03601462093b5945d1676df093446790fd31b20e7b12a2e8e5e09d068109616b
Account0 = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0b")
# 0e195438d9f92eb191032b5f660d42a22255c9c417248f092c1f83f3a36b29ba
Account1 = Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0e")
# 6a7fc6037f7a0dca7004c2cd41d87bfd929be7eb0d31903b238839e8e7aaf897
Account2 = Address("0xa94f5374fce5edbc8e2a8697c15331677e6ebf0a")
# 6a8737909ea3e92b0d47328d70aff338c526832b32362eca8692126c1f399846
Account3 = Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0d")
# d3bd43970708294fd4d78893c4e7c2fed43c8cd505e9c9516e1f11e79f574598
Account4 = Address("0xd94f5374fce5edbc8e2a8697c15331677e6ebf0f")


@pytest.mark.valid_from("Verkle")
@pytest.mark.parametrize("stride", [1, 2, 3])
def test_eoa(blockchain_test: BlockchainTestFiller, stride: int):
    """
    Test only EOA account conversion.
    """
    pre_state = {
        Account0: Account(balance=1000),
        Account1: Account(balance=2000),
        Account2: Account(balance=3000),
    }
    _state_conversion(blockchain_test, pre_state, stride)


@pytest.mark.valid_from("Verkle")
@pytest.mark.parametrize(
    "contract_length",
    [
        1,
        128 * 31,
        130 * 31,
    ],
    ids=[
        "in_header",
        "header_perfect_fit",
        "bigger_than_header",
    ],
)
@pytest.mark.parametrize("convert_in_first_block", [True, False])
@pytest.mark.parametrize("stride", [1, 2, 3])
def test_full_contract(
    blockchain_test: BlockchainTestFiller,
    contract_length: int,
    convert_in_first_block: int,
    stride: int,
):
    """
    Test contract account full/partial migration cases.
    """
    if convert_in_first_block:
        pre_state = {}
    else:
        pre_state = {
            Account0: Account(balance=1000),
            Account1: Account(balance=1001),
            Account2: Account(balance=1002),
        }

    pre_state[Account3] = Account(
        balance=2000,
        code=Op.STOP * contract_length,
        storage={0: 0x1, 1: 0x2},
    )

    _state_conversion(blockchain_test, pre_state, stride)


def _state_conversion(
    blockchain_test: BlockchainTestFiller, pre_state: dict[Address, Account], stride: int
):
    env = Environment(
        fee_recipient="0x2adc25665018aa1fe0e6bc666dac8fc2697ff9ba",
        difficulty=0x20000,
        gas_limit=10000000000,
    )

    # TODO future features:
    # - txs list per block to test writes overlap
    # - vkt pre-state to test stale-values
    # - reorg support
    # - witness assertion
    # - assert conversion finished

    blocks = [Block(txs=[])]

    blockchain_test(
        genesis_environment=env,
        pre=pre_state,
        post=pre_state.copy(),
        blocks=blocks,
    )
