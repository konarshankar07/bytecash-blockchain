from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": ("bytecash_harvester bytecash_timelord_launcher bytecash_timelord " "bytecash_farmer bytecash_full_node bytecash_wallet").split(),
    "node": "bytecash_full_node".split(),
    "harvester": "bytecash_harvester".split(),
    "farmer": "bytecash_harvester bytecash_farmer bytecash_full_node bytecash_wallet".split(),
    "farmer-no-wallet": "bytecash_harvester bytecash_farmer bytecash_full_node".split(),
    "farmer-only": "bytecash_farmer".split(),
    "timelord": "bytecash_timelord_launcher bytecash_timelord bytecash_full_node".split(),
    "timelord-only": "bytecash_timelord".split(),
    "timelord-launcher-only": "bytecash_timelord_launcher".split(),
    "wallet": "bytecash_wallet bytecash_full_node".split(),
    "wallet-only": "bytecash_wallet".split(),
    "introducer": "bytecash_introducer".split(),
    "simulator": "bytecash_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
