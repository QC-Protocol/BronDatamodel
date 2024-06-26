from enum import Enum


class WellStabilityEnum(str, Enum):
    instabiel = "instabiel"
    onbekend = "onbekend"
    stabielNAP = "stabielNAP"


class HeadProtectorEnum(str, Enum):
    geen = "geen"
    koker = "koker"
    kokerMetaal = "kokerMetaal"
    kokerNietMetaal = "kokerNietMetaal"
    onbekend = "onbekend"
    pot = "pot"
    potNietWaterdicht = "potNietWaterdicht"
    potWaterdicht = "potWaterdicht"


class TypeEnum(str, Enum):
    filterlozeBuis = "filterlozeBuis"
    minifilter = "minifilter"
    standaardbuis = "standaardbuis"
    volledigFilter = "volledigFilter"


class VertPosMethodTopEnum(str, Enum):
    AHN1 = "AHN1"
    AHN2 = "AHN2"
    AHN3 = "AHN3"
    GPSOnbekend = "GPSOnbekend"
    RTKGPS0tot4cm = "RTKGPS0tot4cm"
    RTKGPS10tot20cm = "RTKGPS10tot20cm"
    RTKGPS20tot100cm = "RTKGPS20tot100cm"
    RTKGPS4tot10cm = "RTKGPS4tot10cm"
    afgeleidSbl = "afgeleidSbl"
    kaartOnbekend = "kaartOnbekend"
    onbekend = "onbekend"
    tachymetrie0tot10cm = "tachymetrie0tot10cm"
    tachymetrie10tot50cm = "tachymetrie10tot50cm"
    waterpassing0tot2cm = "waterpassing0tot2cm"
    waterpassing2tot4cm = "waterpassing2tot4cm"
    waterpassing4tot10cm = "waterpassing4tot10cm"


class StatusEnum(str, Enum):
    gebruiksklaar = "gebruiksklaar"
    nietGebruiksklaar = "nietGebruiksklaar"
    onbekend = "onbekend"
    onbruikbaar = "onbruikbaar"


class PackingMaterialEnum(str, Enum):
    bentoniet = "bentoniet"
    bentonietFiltergrind = "bentonietFiltergrind"
    boorgatmateriaal = "boorgatmateriaal"
    filtergrind = "filtergrind"
    grind = "grind"
    grout = "grout"
    onbekend = "onbekend"


class MaterialEnum(str, Enum):
    asbest = "asbest"
    beton = "beton"
    gres = "gres"
    hout = "hout"
    houtStaal = "houtStaal"
    ijzer = "ijzer"
    koper = "koper"
    koperStaal = "koperStaal"
    messing = "messing"
    onbekend = "onbekend"
    pe = "pe"
    peHighDensity = "peHighDensity"
    peLowDensity = "peLowDensity"
    pePvc = "pePvc"
    pvc = "pvc"
    pvcStaal = "pvcStaal"
    staal = "staal"
    staalGegalvaniseerd = "staalGegalvaniseerd"
    staalRoestvrij = "staalRoestvrij"
    teflon = "teflon"


class SockMaterialEnum(str, Enum):
    geen = "geen"
    nylon = "nylon"
    onbekend = "onbekend"
    pp = "pp"


class InitialFunctionEnum(str, Enum):
    brandput = "brandput"
    kwaliteit = "kwaliteit"
    kwaliteitStand = "kwaliteitStand"
    onbekend = "onbekend"
    onttrekking = "onttrekking"
    stand = "stand"


class HorPosMethodEnum(str, Enum):
    DGPS50tot200cm = "DGPS50tot200cm"
    GBKNOnbekend = "GBKNOnbekend"
    GPS200tot1000cm = "GPS200tot1000cm"
    GPSOnbekend = "GPSOnbekend"
    RTKGPS0tot2cm = "RTKGPS0tot2cm"
    RTKGPS10tot50cm = "RTKGPS10tot50cm"
    RTKGPS2tot5cm = "RTKGPS2tot5cm"
    RTKGPS5tot10cm = "RTKGPS5tot10cm"
    kaartOnbekend = "kaartOnbekend"
    onbekend = "onbekend"
    tachymetrie0tot10cm = "tachymetrie0tot10cm"
    tachymetrie10tot50cm = "tachymetrie10tot50cm"


class VertPosMethodSurfEnum(str, Enum):
    AHN1 = "AHN1"
    AHN2 = "AHN2"
    AHN3 = "AHN3"
    GPSOnbekend = "GPSOnbekend"
    RTKGPS0tot4cm = "RTKGPS0tot4cm"
    RTKGPS10tot20cm = "RTKGPS10tot20cm"
    RTKGPS20tot100cm = "RTKGPS20tot100cm"
    RTKGPS4tot10cm = "RTKGPS4tot10cm"
    geen = "geen"
    kaartOnbekend = "kaartOnbekend"
    onbekend = "onbekend"
    tachymetrie0tot10cm = "tachymetrie0tot10cm"
    tachymetrie10tot50cm = "tachymetrie10tot50cm"
    waterpassing0tot2cm = "waterpassing0tot2cm"
    waterpassing2tot4cm = "waterpassing2tot4cm"
    waterpassing4tot10cm = "waterpassing4tot10cm"


class GlueEnum(str, Enum):
    geen = "geen"
    onbekend = "onbekend"
    ongespecificeerd = "ongespecificeerd"


class GeenEnum(str, Enum):
    filtergrind = "filtergrind"
    klei = "klei"
    onbekend = "onbekend"
    zand = "zand"


class DeliveryContextEnum(str, Enum):
    GBM = "GBM"
    KRW = "KRW"
    NBW = "NBW"
    NR = "NR"
    OGW = "OGW"
    OW = "OW"
    WW = "WW"
    archiefoverdracht = "archiefoverdracht"
    publiekeTaak = "publiekeTaak"


class ConstructionStandardEnum(str, Enum):
    BWsb = "BWsb"
    IBR = "IBR"
    NEN5104 = "NEN5104"
    NEN5744 = "NEN5744"
    NEN5766 = "NEN5766"
    RWSgwmon = "RWSgwmon"
    STOWAgwst = "STOWAgwst"
    VKB2001 = "VKB2001"
    geen = "geen"
    onbekend = "onbekend"
