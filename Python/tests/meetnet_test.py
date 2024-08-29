from datetime import datetime
from pybron.schema.BRON import GMN, GMNAdm, GMNHistory, GMNNet, GMNPoint
from pybron.schema.BRONEnums import GMNDeliveryContextEnum, GMNGroundwaterAspectEnum, GMNMonitoringPurposeEnum
from pybron.schema.matlabbasemodel import datetime2matlab


def test_meetnet():
    adm = GMNAdm(**{"NetID": None, "BROID": None, "ObjRgstrDateTime": datetime2matlab(datetime.now()), "AccParty": "", "QualityRegime": "bla", "DvRespParty": "bla", "LastRgstrEvent": None})
    net = GMNNet(Name="KRW Oost", startDateMonitoring=datetime2matlab(datetime.now()), DeliveryContext=GMNDeliveryContextEnum.waterwetPeilbeheer, MonitoringPurpose=GMNMonitoringPurposeEnum.onbekend, GroundwaterAspect=GMNGroundwaterAspectEnum.kwantiteit, endDateMonitoring=None)
    point = {0: GMNPoint(MeasuringPointCode="PB A", GMWBROID=None, TubeNo=1)}
    history = None  # GMNHistory(EventName="Plaatsing", EventDate=datetime2matlab(datetime.now()), PointID=0, EventData=None)
    gmn = GMN(adm=adm, net=net, point=point, history=history)
    assert gmn

