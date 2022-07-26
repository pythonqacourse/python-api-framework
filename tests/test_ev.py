from dataclasses import asdict
from http import HTTPStatus

import pytest
from assertpy import assert_that

from framework.models.charging_states import ChargingState
from framework.objects.control_pilot import ControlPilotSignals


class TestEVChargingState:
    """
    Check ev can apply certain voltages after changing its charging state
    """

    @staticmethod
    @pytest.mark.usefixtures("charging_reset")
    def test_connect_is_ok(resources):
        """Connect and check response is OK"""
        r_ev = resources.ev.charging.connect()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.B.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_connect_cp_voltage_integration(resources):
        """Connect and check evse voltage is correspond to state"""
        r_evse = resources.evse.cp.get()
        assert_that(r_evse.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_evse.json).is_equal_to(asdict(ControlPilotSignals.B))

    @staticmethod
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_disconnect_is_ok(resources):
        """Connect and check response is OK"""
        r_ev = resources.ev.charging.disconnect()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.A.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_disconnect")
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_disconnect_cp_voltage_integration(resources):
        """Connect and check evse voltage is correspond to state"""
        r_evse = resources.evse.cp.get()
        assert_that(r_evse.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_evse.json).is_equal_to(asdict(ControlPilotSignals.A))

    @staticmethod
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_start_is_ok(resources):
        """Start and check response is OK"""
        r_ev = resources.ev.charging.start()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.C.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_start")
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_start_cp_voltage_integration(resources):
        """Connect and check evse voltage is correspond to state"""
        r_evse = resources.evse.cp.get()
        assert_that(r_evse.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_evse.json).is_equal_to(asdict(ControlPilotSignals.C))

    @staticmethod
    @pytest.mark.usefixtures("charging_start")
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_stop_is_ok(resources):
        """Stop and check response is OK"""
        r_ev = resources.ev.charging.stop()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.B.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_stop")
    @pytest.mark.usefixtures("charging_start")
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_stop_cp_voltage_integration(resources):
        """Connect and check evse voltage is correspond to state"""
        r_evse = resources.evse.cp.get()
        assert_that(r_evse.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_evse.json).is_equal_to(asdict(ControlPilotSignals.B))

    @staticmethod
    @pytest.mark.usefixtures("charging_reset")
    def test_a_to_error_is_ok(resources):
        """Trigger error from A state and check response is OK"""
        r_ev = resources.ev.charging.error()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.E.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_b_to_error_is_ok(resources):
        """Trigger error from B state and check response is OK"""
        r_ev = resources.ev.charging.error()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.E.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_start")
    @pytest.mark.usefixtures("charging_connect")
    @pytest.mark.usefixtures("charging_reset")
    def test_c_to_error_is_ok(resources):
        """Trigger error from C state and check response is OK"""
        r_ev = resources.ev.charging.error()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_ev.charging_state_name).is_equal_to(ChargingState.E.name)

    @staticmethod
    @pytest.mark.usefixtures("charging_error")
    @pytest.mark.usefixtures("charging_reset")
    def test_error_cp_voltage_integration(resources):
        """Connect and check evse voltage is correspond to state"""
        r_evse = resources.evse.cp.get()
        assert_that(r_evse.status).is_equal_to(HTTPStatus.OK)
        assert_that(r_evse.json).is_equal_to(asdict(ControlPilotSignals.E))

    @staticmethod
    @pytest.mark.usefixtures("charging_reset")
    def test_a_to_c_is_error(resources):
        """Trigger forbidden state transition"""
        r_ev = resources.ev.charging.start()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.BAD_REQUEST)

    @staticmethod
    @pytest.mark.usefixtures("charging_error")
    @pytest.mark.usefixtures("charging_reset")
    def test_connect_from_e_is_error(resources):
        """Trigger forbidden state transition"""
        r_ev = resources.ev.charging.connect()
        assert_that(r_ev.status).is_equal_to(HTTPStatus.BAD_REQUEST)

    @pytest.mark.skip
    def test_ev_evse_integration_manual(self):
        """
        Manual tests might include external parts of the system that actually trigger states
        - Connect the physical socket, check ev state has been changed (check UI, then call /evse/cp API)
        - Disconnect the socket from B state
        - Disconnect the socket from C state
        - Check all error triggers (like electrical current surge etc.)
        - UI tests
        """

    @pytest.mark.skip
    def test_ev_db_unit_intergration(self):
        """
        Unit db integration might calling API endpoints against running database using various db fixtures
        """
