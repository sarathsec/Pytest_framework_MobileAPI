import subprocess
services = ["GetAllAutoRecloser",
            "GetAllCircle",
            "GetAllDCU",
            "GetAllDTR",
            "GetAllDtrTmusByFeederId",
            "GetAllFeeder",
            "GetAllFeedersBySubstationId",
            "GetAllFieldSurvey",
            "GetAllManufacturer",
            "GetAllMeter",
            "GetAllMetersByDcuId",
            "GetAllPole",
            "GetAllRegion",
            "GetAllSection",
            "GetAllService",
            "GetAllSim",
            "GetAllSubstation",
            "GetAllSubstationsBySectionId",
            "GetAllTMU",
            "GetAllTransformer",
            "GetFieldSurveyByAssetTypes"
            ]

print(len(services))

for Service_names in services:
    commands =[
        f"python combo.py regression,sanity,bvt {Service_names}"
            ]

# execute commands one  by one
    for command in commands:
        subprocess.run(command, shell=True)

