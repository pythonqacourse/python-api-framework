from dataclasses import dataclass


@dataclass
class Voltage:
    """
    Represent Voltage parameter of any electrical current type
    value: voltage value in Volt
    """

    value: float


@dataclass
class PWMModulationCurve:
    """
    Represents characteristics of PWM Modulation curve
    width:: modulation width
    frequency:: signal frequency in kHz
    """

    frequency: int
    width: float


@dataclass
class DirectCurrent:
    """
    voltage: Voltage object
    type: Class name
    """

    voltage: Voltage
    name: str = "DirectCurrent"


@dataclass
class PulseWidthModulation:
    """
    Represent PWM modulation signal type
    voltage: Voltage object
    modulation: PWMModulation object
    type: class name
    """

    modulation: PWMModulationCurve
    voltage: Voltage
    name: str = "PulseWidthModulation"
