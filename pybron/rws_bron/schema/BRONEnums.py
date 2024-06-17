from enum import Enum


class DeliveryContextEnum(str, Enum):
    publiekeTaak = "publiekeTaak"
    GBM = "GBM"
    KRW = "KRW"
    NBW = "NBW"
    NR = "NR"
    OGW = "OGW"
    OW = "OW"
    WW = "WW"
    archiefoverdracht = "archiefoverdracht"


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


class InitialFunctionEnum(str, Enum):
    brandput = "brandput"
    kwaliteit = "kwaliteit"
    kwaliteitStand = "kwaliteitStand"
    onttrekking = "onttrekking"
    stand = "stand"
    onbekend = "onbekend"


class HeadProtectorEnum(str, Enum):
    geen = "geen"
    kokerMetaal = "kokerMetaal"
    kokerNietMetaal = "kokerNietMetaal"
    potNietWaterdicht = "potNietWaterdicht"
    potWaterdicht = "potWaterdicht"
    onbekend = "onbekend"
    koker = "koker"
    pot = "pot"


class VertPosMethodSurfEnum(str, Enum):
    AHN2 = "AHN2"
    AHN3 = "AHN3"
    RTKGPS0tot4cm = "RTKGPS0tot4cm"
    RTKGPS4tot10cm = "RTKGPS4tot10cm"
    RTKGPS10tot20cm = "RTKGPS10tot20cm"
    RTKGPS20tot100cm = "RTKGPS20tot100cm"
    tachymetrie0tot10cm = "tachymetrie0tot10cm"
    tachymetrie10tot50cm = "tachymetrie10tot50cm"
    waterpassing0tot2cm = "waterpassing0tot2cm"
    waterpassing2tot4cm = "waterpassing2tot4cm"
    waterpassing4tot10cm = "waterpassing4tot10cm"
    AHN1 = "AHN1"
    onbekend = "onbekend"
    geen = "geen"
    GPSOnbekend = "GPSOnbekend"
    kaartOnbekend = "kaartOnbekend"


class HorPosMethodEnum(str, Enum):
    DGPS50tot200cm = "DGPS50tot200cm"
    GPS200tot1000cm = "GPS200tot1000cm"
    PPPGPS0tot2cm = "PPPGPS0tot2cm"
    PPPGPS10tot50cm = "PPPGPS10tot50cm"
    PPPGPS2tot5cm = "PPPGPS2tot5cm"
    PPPGPS5tot10cm = "PPPGPS5tot10cm"
    RTKGPS0tot2cm = "RTKGPS0tot2cm"
    RTKGPS10tot50cm = "RTKGPS10tot50cm"
    RTKGPS2tot5cm = "RTKGPS2tot5cm"
    RTKGPS5tot10cm = "RTKGPS5tot10cm"
    tachymetrie0tot10cm = "tachymetrie0tot10cm"
    tachymetrie10tot50cm = "tachymetrie10tot50cm"
    onbekend = "onbekend"
    GBKNOnbekend = "GBKNOnbekend"
    GPSOnbekend = "GPSOnbekend"
    kaartOnbekend = "kaartOnbekend"


class TypeEnum(str, Enum):
    minifilter = "minifilter"
    standaardbuis = "standaardbuis"
    volledigFilter = "volledigFilter"
    filterlozeBuis = "filterlozeBuis"


class StatusEnum(str, Enum):
    gebruiksklaar = "gebruiksklaar"
    nietGebruiksklaar = "nietGebruiksklaar"
    onbruikbaar = "onbruikbaar"
    onbekend = "onbekend"


class VertPosMethodTopEnum(str, Enum):
    AHN2 = "AHN2"
    AHN3 = "AHN3"
    RTKGPS0tot4cm = "RTKGPS0tot4cm"
    RTKGPS10tot20cm = "RTKGPS10tot20cm"
    RTKGPS20tot100cm = "RTKGPS20tot100cm"
    RTKGPS4tot10cm = "RTKGPS4tot10cm"
    afgeleidSbl = "afgeleidSbl"
    tachymetrie0tot10cm = "tachymetrie0tot10cm"
    tachymetrie10tot50cm = "tachymetrie10tot50cm"
    waterpassing0tot2cm = "waterpassing0tot2cm"
    waterpassing2tot4cm = "waterpassing2tot4cm"
    waterpassing4tot10cm = "waterpassing4tot10cm"
    AHN1 = "AHN1"
    onbekend = "onbekend"
    geen = "geen"
    GPSOnbekend = "GPSOnbekend"
    kaartOnbekend = "kaartOnbekend"


class PackingMaterialEnum(str, Enum):
    bentoniet = "bentoniet"
    bentonietFiltergrind = "bentonietFiltergrind"
    boorgatmateriaal = "boorgatmateriaal"
    filtergrind = "filtergrind"
    grind = "grind"
    grout = "grout"
    onbekend = "onbekend"


class GlueEnum(str, Enum):
    geen = "geen"
    ongespecificeerd = "ongespecificeerd"
    onbekend = "onbekend"


class MaterialEnum(str, Enum):
    beton = "beton"
    gres = "gres"
    hout = "hout"
    ijzer = "ijzer"
    koper = "koper"
    messing = "messing"
    pe = "pe"
    peHighDensity = "peHighDensity"
    peLowDensity = "peLowDensity"
    pePvc = "pePvc"
    pvc = "pvc"
    staal = "staal"
    staalGegalvaniseerd = "staalGegalvaniseerd"
    staalRoestvrij = "staalRoestvrij"
    teflon = "teflon"
    onbekend = "onbekend"
    asbest = "asbest"
    houtStaal = "houtStaal"
    koperStaal = "koperStaal"
    pvcStaal = "pvcStaal"


class SockMaterialEnum(str, Enum):
    geen = "geen"
    nylon = "nylon"
    pp = "pp"
    onbekend = "onbekend"


class GeenEnum(str, Enum):
    gebruiksklaar = "gebruiksklaar"
    nietGebruiksklaar = "nietGebruiksklaar"


class EventNameEnum(str, Enum):
    putIngericht = "putIngericht"
    inmetenPosities = "inmetenPosities"
    inmetenMaaiveld = "inmetenMaaiveld"
    maaiveldVerlegd = "maaiveldVerlegd"
    positiesVeranderdNatuurlijkProces = "positiesVeranderdNatuurlijkProces"
    maaiveldVeranderdNatuurlijkProces = "maaiveldVeranderdNatuurlijkProces"
    buisIngekort = "buisIngekort"
    buisOpgelengd = "buisOpgelengd"
    buisdeelIngeplaatst = "buisdeelIngeplaatst"
    buisstatusVeranderd = "buisstatusVeranderd"
    elektrodestatusVeranderd = "elektrodestatusVeranderd"
    beschermconstructieVeranderd = "beschermconstructieVeranderd"
    eigenaarVeranderd = "eigenaarVeranderd"
    onderhouderVeranderd = "onderhouderVeranderd"
    putOpgeruimd = "putOpgeruimd"
