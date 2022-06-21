from brownie import accounts, network, config


LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache-local",
    "mainnet-fork",
    "hardhat",
    "ganache",
]
FORKED_LOCAL_BLOCKCHAIN = ["mainnet-fork", "mainnet-fork_dev"]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_BLOCKCHAIN
    ):
        return accounts[0]
    if id:
        return accounts.load(id)
    if network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    return None
