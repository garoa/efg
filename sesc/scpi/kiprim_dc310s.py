"""HP/Agilent 3362B specific device implementation and helpers"""
from typing import Any
import logging
import decimal

from scpi.scpi import SCPIDevice, SCPIProtocol
from scpi.transports.rs232 import RS232Transport
from scpi.transports.rs232 import get as get_rs232
from scpi.devices.generic import MultiMeter, PowerSupply

LOGGER = logging.getLogger(__name__)


class KiprimDC310S(PowerSupply, MultiMeter, SCPIDevice):
	pass

def rs232(serial_url: str, **kwargs: Any) -> KiprimDC310S:
    """Quick helper to connect via RS232 port"""
    transport = get_rs232(serial_url, **kwargs)
    protocol = SCPIProtocol(transport)
    dev = KiprimDC310S(protocol)
    return dev
