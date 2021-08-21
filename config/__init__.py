## Ideally, they have one file with the settings for the strat and deployment
## This file would allow them to configure so they can test, deploy and interact with the strategy

BADGER_DEV_MULTISIG = "0xb65cef03b9b89f99517643226d76e286ee999e77"

WANT = "0xba09679ab223c6bdaf44d45ba2d7279959289ab0"  ## Dai/AVAX Pangolin LP
STAKING = "0x63A84F66b8c90841Cb930F2dC3D28799F0c6657B"  ## Dai/AVAX Pangolin LP Staking Contract
REWARD_TOKEN = "0x60781C2586D68229fde47564546784ab3fACA982"  ## PNG

PROTECTED_TOKENS = [WANT, STAKING, REWARD_TOKEN]
## Fees in Basis Points
DEFAULT_GOV_PERFORMANCE_FEE = 1000
DEFAULT_PERFORMANCE_FEE = 1000
DEFAULT_WITHDRAWAL_FEE = 50

FEES = [DEFAULT_GOV_PERFORMANCE_FEE, DEFAULT_PERFORMANCE_FEE, DEFAULT_WITHDRAWAL_FEE]

REGISTRY = "0xFda7eB6f8b7a9e9fCFd348042ae675d1d652454f"  # Multichain BadgerRegistry
