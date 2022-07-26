from dataclasses import dataclass
from typing import Union

from framework.models.electrical_voltage import DirectCurrent, PulseWidthModulation


@dataclass
class ControlPilotSignal:
    """
    Represents a control pilot signal
    """

    electrical_voltage_type: Union[DirectCurrent, PulseWidthModulation]
