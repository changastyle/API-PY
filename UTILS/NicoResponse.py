from starlette.responses import JSONResponse

class NicoResponse:

    def __init__(self, obj):

        rtaJSON = "null"

        print("TIPO:", str(type(obj)))
        # print("TIPO NONE:", str(type(None)))

        if str(type(obj)) != "<class 'NoneType'>":
            rtaJSON = JSONResponse(obj.__dict__)

        return rtaJSON