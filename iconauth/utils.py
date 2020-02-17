import base64
from iconservice.iconscore.icon_score_base2 import _create_address_with_key, _recover_key


def recover_to_addr(msg, sig):
	signature: bytes = base64.b64decode(sig)
	msg_hash: bytes = bytes.fromhex(msg)
	pubkey = _recover_key(msg_hash, signature, compressed=True)
	address = str(_create_address_with_key(pubkey))
	return address
