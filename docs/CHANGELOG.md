# Changelog

Test fixtures for use by clients are available for each release on the [Github releases page](https://github.com/ethereum/execution-spec-tests/releases).

**Key:** ✨ = New, 🐞 = Fixed, 🔀 = Changed, 💥 = Breaking change.

## 🔜 [Unreleased](https://github.com/ethereum/execution-spec-tests/releases/tag/v-Unreleased) - 2024-xx-xx

### 🧪 Test Cases

- ✨ Add `test_double_kill` and `test_recreate` which test resurrection of accounts killed with `SELFDESTRUCT` ([#488](https://github.com/ethereum/execution-spec-tests/pull/488)).

### 🛠️ Framework

- 🐞 Fix incorrect `!=` operator for `FixedSizeBytes` ([#477](https://github.com/ethereum/execution-spec-tests/pull/477)).
- ✨ Add Macro enum that represents byte sequence of Op instructions ([#457](https://github.com/ethereum/execution-spec-tests/pull/457))
- ✨ Number of parameters used to call opcodes (to generate bytecode) is now checked ([#492](https://github.com/ethereum/execution-spec-tests/pull/492)).
- ✨ Libraries have been refactored to use `pydantic` for type checking in most test types ([#486](https://github.com/ethereum/execution-spec-tests/pull/486), [#501](https://github.com/ethereum/execution-spec-tests/pull/501), [#508](https://github.com/ethereum/execution-spec-tests/pull/508)).
- ✨ Opcodes are now subscriptable and it's used to define the data portion of the opcode: `Op.PUSH1(1) == Op.PUSH1[1]  == b"\x60\x01"` ([#513](https://github.com/ethereum/execution-spec-tests/pull/513))
- ✨ Added EOF fixture format ([#512](https://github.com/ethereum/execution-spec-tests/pull/512)).

### 🔧 EVM Tools

### 📋 Misc

- 🐞 Fix CI by using Golang 1.21 in Github Actions to build geth ([#484](https://github.com/ethereum/execution-spec-tests/pull/484)).
- 💥 "Merge" has been renamed to "Paris" in the "network" field of the Blockchain tests, and in the "post" field of the State tests ([#480](https://github.com/ethereum/execution-spec-tests/pull/480)).
- ✨ Port entry point scripts to use [click](https://click.palletsprojects.com) and add tests ([#483](https://github.com/ethereum/execution-spec-tests/pull/483)).
- 💥 As part of the pydantic conversion, the fixtures have the following (possibly breaking) changes ([#486](https://github.com/ethereum/execution-spec-tests/pull/486)):
  - State test field `transaction` now uses the proper zero-padded hex number format for fields `maxPriorityFeePerGas`, `maxFeePerGas`, and `maxFeePerBlobGas`
  - Fixtures' hashes (in the `_info` field) are now calculated by removing the "_info" field entirely instead of it being set to an empty dict.
- 🐞 Relax minor and patch dependency requirements to avoid conflicting package dependencies ([#510](https://github.com/ethereum/execution-spec-tests/pull/510)).

### 💥 Breaking Change

- Cancun is now the latest deployed fork, and the development fork is now Prague ([#489](https://github.com/ethereum/execution-spec-tests/pull/489)).

## 🔜 [v2.1.1](https://github.com/ethereum/execution-spec-tests/releases/tag/v2.1.1) - 2024-03-09

### 🧪 Test Cases

- 🐞 Dynamic create2 collision from different transactions same block ([#430](https://github.com/ethereum/execution-spec-tests/pull/430)).
- 🐞 Fix beacon root contract deployment tests so the account in the pre-alloc is not empty ([#425](https://github.com/ethereum/execution-spec-tests/pull/425)).
- 🔀 All beacon root contract tests are now contained in tests/cancun/eip4788_beacon_root/test_beacon_root_contract.py, and all state tests have been converted back to blockchain tests format ([#449](https://github.com/ethereum/execution-spec-tests/pull/449))

### 🛠️ Framework

- ✨ Add Prague to forks ([#419](https://github.com/ethereum/execution-spec-tests/pull/419)).
- ✨ Improve handling of the argument passed to `solc --evm-version` when compiling Yul code ([#418](https://github.com/ethereum/execution-spec-tests/pull/418)).
- 🐞 Fix `fill -m yul_test` which failed to filter tests that are (dynamically) marked as a yul test ([#418](https://github.com/ethereum/execution-spec-tests/pull/418)).
- 🔀 Helper methods `to_address`, `to_hash` and `to_hash_bytes` have been deprecated in favor of `Address` and `Hash`, which are automatically detected as opcode parameters and pushed to the stack in the resulting bytecode ([#422](https://github.com/ethereum/execution-spec-tests/pull/422)).
- ✨ `Opcodes` enum now contains docstrings with each opcode description, including parameters and return values, which show up in many development environments ([#424](https://github.com/ethereum/execution-spec-tests/pull/424)) @ThreeHrSleep.
- 🔀 Locally calculate state root for the genesis blocks in the blockchain tests instead of calling t8n ([#450](https://github.com/ethereum/execution-spec-tests/pull/450)).
- 🐞 Fix bug that causes an exception during test collection because the fork parameter contains `None` ([#452](https://github.com/ethereum/execution-spec-tests/pull/452)).
- ✨ The `_info` field in the test fixtures now contains a `hash` field, which is the hash of the test fixture, and a `hasher` script has been added which prints and performs calculations on top of the hashes of all fixtures (see `hasher -h`) ([#454](https://github.com/ethereum/execution-spec-tests/pull/454)).
- ✨ Adds an optional `verify_sync` field to hive blockchain tests (EngineAPI). When set to true a second client attempts to sync to the first client that executed the tests ([#431](https://github.com/ethereum/execution-spec-tests/pull/431)).
- 🐞 Fix manually setting the gas limit in the genesis test env for post genesis blocks in blockchain tests ([#472](https://github.com/ethereum/execution-spec-tests/pull/472)).

### 🔧 EVM Tools

### 📋 Misc

- 🐞 Fix deprecation warnings due to outdated config in recommended VS Code project settings ([#420](https://github.com/ethereum/execution-spec-tests/pull/420)).
- 🐞 Fix typo in the selfdestruct revert tests module ([#421](https://github.com/ethereum/execution-spec-tests/pull/421)).

## [v2.1.0](https://github.com/ethereum/execution-spec-tests/releases/tag/v2.1.0) - 2024-01-29: 🐍🏖️ Cancun

Release [v2.1.0](https://github.com/ethereum/execution-spec-tests/releases/tag/v2.1.0) primarily fixes a small bug introduced within the previous release where transition forks are used within the new `StateTest` format. This was highlighted by @chfast within #405 (https://github.com/ethereum/execution-spec-tests/issues/405), where the fork name `ShanghaiToCancunAtTime15k` was found within state tests.

### 🧪 Test Cases

- ✨ [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Adds `test_blob_gas_subtraction_tx()` verifying the blob gas fee is subtracted from the sender before executing the blob tx ([#407](https://github.com/ethereum/execution-spec-tests/pull/407)).

### 🛠️ Framework

- 🐞 State tests generated with transition forks no longer use the transition fork name in the fixture output, instead they use the actual enabled fork according to the state test's block number and timestamp ([#406](https://github.com/ethereum/execution-spec-tests/pull/406)).

### 📋 Misc

- ✨ Use `run-parallel` and shared wheel packages for `tox` ([#408](https://github.com/ethereum/execution-spec-tests/pull/408)).

## [v2.0.0](https://github.com/ethereum/execution-spec-tests/releases/tag/v2.0.0) - 2024-01-25: 🐍🏖️ Cancun

Release [v2.0.0](https://github.com/ethereum/execution-spec-tests/releases/tag/v2.0.0) contains many important framework changes, including introduction of the `StateTest` format, and some additional Cancun and other test coverage.

Due to changes in the framework, there is a breaking change in the directory structure in the release tarball, please see the dedicated "💥 Breaking Changes" section below for more information.

### 🧪 Test Cases

- ✨ [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Add `test_sufficient_balance_blob_tx()` and `test_sufficient_balance_blob_tx_pre_fund_tx()` ([#379](https://github.com/ethereum/execution-spec-tests/pull/379)).
- ✨ [EIP-6780](https://eips.ethereum.org/EIPS/eip-6780): Add a reentrancy suicide revert test ([#372](https://github.com/ethereum/execution-spec-tests/pull/372)).
- ✨ [EIP-1153](https://eips.ethereum.org/EIPS/eip-1153): Add `test_run_until_out_of_gas()` for transient storage opcodes ([#401](https://github.com/ethereum/execution-spec-tests/pull/401)).
- ✨ [EIP-198](https://eips.ethereum.org/EIPS/eip-198): Add tests for the MODEXP precompile ([#364](https://github.com/ethereum/execution-spec-tests/pull/364)).
- ✨ Tests for nested `CALL` and `CALLCODE` gas consumption with a positive value transfer (previously lacking coverage) ([#371](https://github.com/ethereum/execution-spec-tests/pull/371)).
- 🐞 [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Fixed `test_invalid_tx_max_fee_per_blob_gas()` to account for extra gas required in the case where the account is incorrectly deduced the balance as if it had the correct block blob gas fee ([#370](https://github.com/ethereum/execution-spec-tests/pull/370)).
- 🐞 [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Fixed `test_insufficient_balance_blob_tx()` to correctly calculate the minimum balance required for the accounts ([#379](https://github.com/ethereum/execution-spec-tests/pull/379)).
- 🐞 [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Fix and enable `test_invalid_blob_tx_contract_creation` ([#379](https://github.com/ethereum/execution-spec-tests/pull/379)).
- 🔀 Convert all eligible `BlockchainTest`s to `StateTest`s (and additionally generate corresponding `BlockchainTest`s) ([#368](https://github.com/ethereum/execution-spec-tests/pull/368), [#370](https://github.com/ethereum/execution-spec-tests/pull/370)).

### 🛠️ Framework

- ✨ Add `StateTest` fixture format generation; `StateTests` now generate a `StateTest` and a corresponding `BlockchainTest` test fixture, previously only `BlockchainTest` fixtures were generated ([#368](https://github.com/ethereum/execution-spec-tests/pull/368)).
- ✨ Add `StateTestOnly` fixture format is now available and its only difference with `StateTest` is that it does not produce a `BlockchainTest` ([#368](https://github.com/ethereum/execution-spec-tests/pull/368)).
- ✨ Add `evm_bytes_to_python` command-line utility which converts EVM bytecode to Python Opcodes ([#357](https://github.com/ethereum/execution-spec-tests/pull/357)).
- ✨ Fork objects used to write tests can now be compared using the `>`, `>=`, `<`, `<=` operators, to check for a fork being newer than, newer than or equal, older than, older than or equal, respectively when compared against other fork ([#367](https://github.com/ethereum/execution-spec-tests/pull/367)).
- ✨ Add [solc 0.8.23](https://github.com/ethereum/solidity/releases/tag/v0.8.23) support ([#373](https://github.com/ethereum/execution-spec-tests/pull/373)).
- ✨ Add framework unit tests for post state exception verification ([#350](https://github.com/ethereum/execution-spec-tests/pull/350)).
- ✨ Add a helper class `ethereum_test_tools.TestParameterGroup` to define test parameters as dataclasses and auto-generate test IDs ([#364](https://github.com/ethereum/execution-spec-tests/pull/364)).
- ✨ Add a `--single-fixture-per-file` flag to generate one fixture JSON file per test case ([#331](https://github.com/ethereum/execution-spec-tests/pull/331)).
- 🐞 Storage type iterator is now fixed ([#369](https://github.com/ethereum/execution-spec-tests/pull/369)).
- 🐞 Fix type coercion in `FixtureHeader.join()` ([#398](https://github.com/ethereum/execution-spec-tests/pull/398)).
- 🔀 Locally calculate the transactions list's root instead of using the one returned by t8n when producing BlockchainTests ([#353](https://github.com/ethereum/execution-spec-tests/pull/353)).
- 🔀 Change custom exception classes to dataclasses to improve testability ([#386](https://github.com/ethereum/execution-spec-tests/pull/386)).
- 🔀 Update fork name from "Merge" to "Paris" used within the framework and tests ([#363](https://github.com/ethereum/execution-spec-tests/pull/363)).
- 💥 Replace `=` with `_` in pytest node ids and test fixture names ([#342](https://github.com/ethereum/execution-spec-tests/pull/342)).
- 💥 The `StateTest`, spec format used to write tests, is now limited to a single transaction per test ([#361](https://github.com/ethereum/execution-spec-tests/pull/361)).
- 💥 Tests must now use `BlockException` and `TransactionException` to define the expected exception of a given test, which can be used to test whether the client is hitting the proper exception when processing the block or transaction ([#384](https://github.com/ethereum/execution-spec-tests/pull/384)).
- 💥 `fill`: Remove the `--enable-hive` flag; now all test types are generated by default ([#358](https://github.com/ethereum/execution-spec-tests/pull/358)).
- 💥 Rename test fixtures names to match the corresponding pytest node ID as generated using `fill` ([#342](https://github.com/ethereum/execution-spec-tests/pull/342)).

### 📋 Misc

- ✨ Docs: Add a ["Consuming Tests"](https://ethereum.github.io/execution-spec-tests/main/consuming_tests/) section to the docs, where each test fixture format is described, along with the steps to consume them, and the description of the structures used in each format ([#375](https://github.com/ethereum/execution-spec-tests/pull/375)).
- 🔀 Docs: Update `t8n` tool branch to fill tests for development features in the [readme](https://github.com/ethereum/execution-spec-test) ([#338](https://github.com/ethereum/execution-spec-tests/pull/338)).
- 🔀 Filling tool: Updated the default filling tool (`t8n`) to go-ethereum@master ([#368](https://github.com/ethereum/execution-spec-tests/pull/368)).
- 🐞 Docs: Fix error banner in online docs due to mermaid syntax error ([#398](https://github.com/ethereum/execution-spec-tests/pull/398)).
- 🐞 Docs: Fix incorrectly formatted nested lists in online doc ([#403](https://github.com/ethereum/execution-spec-tests/pull/403)).

### 💥 Breaking Changes

A concrete example of the test name renaming and change in directory structure is provided below.

1. Fixture output, including release tarballs, now contain subdirectories for different test types:

   1. `blockchain_tests`: Contains `BlockchainTest` formatted tests
   2. `blockchain_tests_hive`: Contains `BlockchainTest` with Engine API call directives for use in hive
   3. `state_tests`: Contains `StateTest` formatted tests

2. `StateTest`, spec format used to write tests, is now limited to a single transaction per test.
3. In this release the pytest node ID is now used for fixture names (previously only the test parameters were used), this should not be breaking. However, `=` in both node IDs (and therefore fixture names) have been replaced with `_`, which may break tooling that depends on the `=` character.
4. Produced `blockchain_tests` fixtures and their corresponding `blockchain_tests_hive` fixtures now contain the named exceptions `BlockException` and `TransactionException` as strings in the `expectException` and `validationError` fields, respectively. These exceptions can be used to test whether the client is hitting the proper exception when processing an invalid block.

   Blockchain test:

   ```json
   "blocks": [
         {
            ...
            "expectException": "TransactionException.INSUFFICIENT_ACCOUNT_FUNDS",
            ...
         }
         ...
   ]
   ```

   Blockchain hive test:

   ```json
   "engineNewPayloads": [
         {
            ...
            "validationError": "TransactionException.INSUFFICIENT_ACCOUNT_FUNDS",
            ...
         }
         ...
   ]
   ```

#### Renaming and Release Tarball Directory Structure Change Example

The fixture renaming provides a more consistent naming scheme between the pytest node ID and fixture name and allows the fixture name to be provided directly to pytest 5on the command line to execute individual tests in isolation, e.g. `pytest tests/frontier/opcodes/test_dup.py::test_dup[fork_Frontier]`.

1. Pytest node ID example:

   1. Previous node ID: `tests/frontier/opcodes/test_dup.py::test_dup[fork=Frontier]`.
   2. New node ID: `tests/frontier/opcodes/test_dup.py::test_dup[fork_Frontier]`.

2. Fixture name example:

   1. Previous fixture name: `000-fork=Frontier`
   2. New fixture name: `tests/frontier/opcodes/test_dup.py::test_dup[fork_Frontier]` (now the same as the pytest node ID).

3. Fixture JSON file name example (within the release tarball):

   1. Previous fixture file name: `fixtures/frontier/opcodes/dup/dup.json` (`BlockChainTest` format).
   2. New fixture file names (all present within the release tarball):

     - `fixtures/state_tests/frontier/opcodes/dup/dup.json` (`StateTest` format).
     - `fixtures/blockchain_tests/frontier/opcodes/dup/dup.json` (`BlockChainTest` format).
     - `fixtures/blockchain_tests_hive/frontier/opcodes/dup/dup.json` (a blockchain test in `HiveFixture` format).

## [v1.0.6](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.6) - 2023-10-19: 🐍🏖️ Cancun Devnet 10

### 🧪 Test Cases

- 🔀 [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Update KZG point evaluation test vectors to use data from the official KZG setup and Mainnet Trusted Setup ([#336](https://github.com/ethereum/execution-spec-tests/pull/336)).

### 🛠️ Framework

- 🔀 Fixtures: Add a non-RLP format field (`rlp_decoded`) to invalid blocks ([#322](https://github.com/ethereum/execution-spec-tests/pull/322)).
- 🔀 Spec: Refactor state and blockchain spec ([#307](https://github.com/ethereum/execution-spec-tests/pull/307)).

### 🔧 EVM Tools

- ✨ Run geth's `evm blocktest` command to verify JSON fixtures after test case execution (`--verify-fixtures`) ([#325](https://github.com/ethereum/execution-spec-tests/pull/325)).
- ✨ Enable tracing support for `ethereum-spec-evm` ([#289](https://github.com/ethereum/execution-spec-tests/pull/289)).

### 📋 Misc

- ✨ Tooling: Add Python 3.12 support ([#309](https://github.com/ethereum/execution-spec-tests/pull/309)).
- ✨ Process: Added a Github pull request template ([#308](https://github.com/ethereum/execution-spec-tests/pull/308)).
- ✨ Docs: Changelog updated post release ([#321](https://github.com/ethereum/execution-spec-tests/pull/321)).
- ✨ Docs: Add [a section explaining execution-spec-tests release artifacts](https://ethereum.github.io/execution-spec-tests/main/getting_started/using_fixtures/) ([#334](https://github.com/ethereum/execution-spec-tests/pull/334)).
- 🔀 T8N Tool: Branch used to generate the tests for Cancun is now [lightclient/go-ethereum@devnet-10](https://github.com/lightclient/go-ethereum/tree/devnet-10) ([#336](https://github.com/ethereum/execution-spec-tests/pull/336))

### 💥 Breaking Change

- Fixtures now use the Mainnet Trusted Setup merged on [consensus-specs#3521](https://github.com/ethereum/consensus-specs/pull/3521) ([#336](https://github.com/ethereum/execution-spec-tests/pull/336))

## [v1.0.5](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.5) - 2023-09-26: 🐍🏖️ Cancun Devnet 9 Release 3

This release mainly serves to update the EIP-4788 beacon roots address to `0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02`, as updated in [ethereum/EIPs/pull/7672](https://github.com/ethereum/EIPs/pull/7672).

### 🧪 Test Cases

- 🐞 [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844): Fix invalid blob txs pre-Cancun engine response ([#306](https://github.com/ethereum/execution-spec-tests/pull/306)).
- ✨ [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788): Final update to the beacon root address ([#312](https://github.com/ethereum/execution-spec-tests/pull/312)).

### 📋 Misc

- ✨ Docs: Changelog added ([#305](https://github.com/ethereum/execution-spec-tests/pull/305)).
- ✨ CI/CD: Run development fork tests in Github Actions ([#302](https://github.com/ethereum/execution-spec-tests/pull/302)).
- ✨ CI/CD: Generate test JSON fixtures on push ([#303](https://github.com/ethereum/execution-spec-tests/pull/303)).

### 💥 Breaking Change

Please use development fixtures from now on when testing Cancun. These refer to changes that are currently under development within clients:

- fixtures: All tests until the last stable fork (Shanghai)
- fixtures_develop: All tests until the last development fork (Cancun)
- fixtures_hive: All tests until the last stable fork (Shanghai) in hive format (Engine API directives instead of the usual BlockchainTest format)
- fixtures_develop_hive: All tests until the last development fork (Cancun) in hive format

## [v1.0.4](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.4) - 2023-09-21: 🐍 Cancun Devnet 9 Release 2

This release adds additional coverage to the current set of Cancun tests, up to the [Devnet-9 Cancun specification](https://notes.ethereum.org/@ethpandaops/dencun-devnet-9).

**Note:** Additional EIP-4788 updates from [ethereum/EIPs/pull/7672](https://github.com/ethereum/EIPs/pull/7672) will be included in the next release.

### 🧪 Test Cases

- ✨ [EIP-7516: BLOBBASEFEE opcode](https://eips.ethereum.org/EIPS/eip-7516): Add first and comprehensive tests (@marioevz in [#294](https://github.com/ethereum/execution-spec-tests/pull/294)).
- ✨ [EIP-4788: Beacon block root in the EVM](https://eips.ethereum.org/EIPS/eip-4788): Increase coverage (@spencer-tb in [#297](https://github.com/ethereum/execution-spec-tests/pull/297)).
- 🐞 [EIP-1153: Transient storage opcodes](https://eips.ethereum.org/EIPS/eip-1153): Remove conftest '+1153' in network field (@spencer-tb in [#299](https://github.com/ethereum/execution-spec-tests/pull/299)).

### 🛠️ Framework

- 🔀 [EIP-4788](https://eips.ethereum.org/EIPS/eip-4788): Beacon root contract is pre-deployed at `0xbEAC020008aFF7331c0A389CB2AAb67597567d7a` (@spencer-tb in [#297](https://github.com/ethereum/execution-spec-tests/pull/297)).
- ✨ Deprecate empty accounts within framework (@spencer-tb in [#300](https://github.com/ethereum/execution-spec-tests/pull/300)).
- ✨ Fixture generation split based on hive specificity (@spencer-tb in [#301](https://github.com/ethereum/execution-spec-tests/pull/301)).
- 💥 `fill`: `--disable-hive` flag removed; replaced by `--enable-hive` (@spencer-tb in [#301](https://github.com/ethereum/execution-spec-tests/pull/301)).
- ✨ Add engine API forkchoice updated information in fixtures (@spencer-tb in [#256](https://github.com/ethereum/execution-spec-tests/pull/256)).

## [v1.0.3](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.3) - 2023-09-14: 🐍 Cancun Devnet 9 Release

See [v1.0.3](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.3).

## [v1.0.2](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.2) - 2023-08-11: 🐍 Cancun Devnet 8 + 4788 v2 Pre-Release

See [v1.0.2](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.2).

## [v1.0.1](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.1) - 2023-08-03: 🐍 Cancun Devnet-8 Pre-Release

See [v1.0.1](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.1).

## [v1.0.0](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.0) - 2023-06-27: 🧪 Welcome to the Pytest Era

See [v1.0.0](https://github.com/ethereum/execution-spec-tests/releases/tag/v1.0.0).

Older releases can be found on [the releases page](https://github.com/ethereum/execution-spec-tests/releases).
