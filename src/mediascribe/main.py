from starlite import Starlite
from .controllers.asr import ASRController


app = Starlite(route_handlers=[ASRController])
