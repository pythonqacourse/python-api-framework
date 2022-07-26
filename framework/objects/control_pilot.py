from framework.models.control_pilot import ControlPilotSignal
from framework.models.electrical_voltage import DirectCurrent, PulseWidthModulation, PWMModulationCurve, Voltage


class ControlPilotSignals:
    """Class to emulate all possible signals in tests"""

    A: ControlPilotSignal = ControlPilotSignal(electrical_voltage_type=DirectCurrent(voltage=Voltage(value=12.0)))
    B: ControlPilotSignal = ControlPilotSignal(
        electrical_voltage_type=PulseWidthModulation(
            modulation=PWMModulationCurve(frequency=1, width=0.5),
            voltage=Voltage(value=9.0),
        )
    )
    C: ControlPilotSignal = ControlPilotSignal(
        electrical_voltage_type=PulseWidthModulation(
            modulation=PWMModulationCurve(frequency=1, width=0.5),
            voltage=Voltage(value=6.0),
        )
    )
    E: ControlPilotSignal = ControlPilotSignal(electrical_voltage_type=DirectCurrent(voltage=Voltage(value=0)))
