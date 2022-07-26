import json
from dataclasses import asdict
from json import dumps

from bottle import get, put, request, response, run
from transitions import Machine, MachineError

from framework.models.charging_states import ChargingState
from framework.objects.control_pilot import ControlPilotSignals

transitions_list = [
    ["connect", ChargingState.A, ChargingState.B],
    ["disconnect", ChargingState.B, ChargingState.A],
    ["start", ChargingState.B, ChargingState.C],
    ["stop", ChargingState.C, ChargingState.B],
    ["error", "*", ChargingState.E],
]

# noinspection PyTypeChecker
m = Machine(states=ChargingState, transitions=transitions_list, initial=ChargingState.A)


@get("/evse/cp")
def evse_get_cp():
    state = m.state.name
    cp_signal = getattr(ControlPilotSignals, state)
    rv = asdict(cp_signal)
    response.content_type = "application/json"
    return dumps(rv)


@put("/ev/charging")
def ev_set_state():
    trigger_name = json.load(request.body).get("trigger")
    try:
        if trigger_name == "reset":
            m.to_A()
            rv = {"success": f"State reset to {m.state.name}"}
        else:
            m.trigger(trigger_name)
            rv = {"success": f"State changed to {m.state.name}"}
    except (ValueError, AttributeError) as e:
        response.status = 404
        rv = {"error": str(e).strip('"')}
    except MachineError as e:
        response.status = 400
        rv = {"error": str(e).strip('"')}
    finally:
        request.content_type = "application/json"
        response.content_type = "application/json"
    return dumps(rv)


if __name__ == "__main__":
    run(host="localhost", port=8083)
