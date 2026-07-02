# flake8: noqa
from enum import Enum


class GMWWellStabilityEnum(str, Enum):
    instabiel = "instabiel"
    onbekend = "onbekend"
    stabielNAP = "stabielNAP"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWWellHeadProtectorEnum(str, Enum):
    geen = "geen"
    koker = "koker"
    kokerMetaal = "kokerMetaal"
    kokerNietMetaal = "kokerNietMetaal"
    onbekend = "onbekend"
    pot = "pot"
    potNietWaterdicht = "potNietWaterdicht"
    potWaterdicht = "potWaterdicht"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWVerticalDatumEnum(str, Enum):
    NAP = "NAP"


class GMWTubeTypeEnum(str, Enum):
    filterlozeBuis = "filterlozeBuis"
    minifilter = "minifilter"
    standaardbuis = "standaardbuis"
    volledigFilter = "volledigFilter"


class GMWTubeTopPositioningMethodEnum(str, Enum):
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

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWTubeStatusEnum(str, Enum):
    gebruiksklaar = "gebruiksklaar"
    nietGebruiksklaar = "nietGebruiksklaar"
    onbekend = "onbekend"
    onbruikbaar = "onbruikbaar"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWTubePackingMaterialEnum(str, Enum):
    bentoniet = "bentoniet"
    bentonietFiltergrind = "bentonietFiltergrind"
    boorgatmateriaal = "boorgatmateriaal"
    filtergrind = "filtergrind"
    grind = "grind"
    grout = "grout"
    onbekend = "onbekend"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWTubeMaterialEnum(str, Enum):
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

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWSockMaterialEnum(str, Enum):
    geen = "geen"
    nylon = "nylon"
    onbekend = "onbekend"
    pp = "pp"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWLocalVerticalReferencePointEnum(str, Enum):
    NAP = "NAP"


class GMWInitialFunctionEnum(str, Enum):
    brandput = "brandput"
    kwaliteit = "kwaliteit"
    kwaliteitStand = "kwaliteitStand"
    onbekend = "onbekend"
    onttrekking = "onttrekking"
    stand = "stand"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWHorizontalPositioningMethodEnum(str, Enum):
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

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWHorizontalCrsEnum(str, Enum):
    ETRS89 = "ETRS89"
    RD = "RD"


class GMWGroundLevelPositioningMethodEnum(str, Enum):
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

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWGlueEnum(str, Enum):
    geen = "geen"
    onbekend = "onbekend"
    ongespecificeerd = "ongespecificeerd"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWEventNameEnum(str, Enum):
    Put_ingericht = "Put ingericht"
    Maaiveld_verlaagd = "Maaiveld verlaagd"
    Maaiveld_opgehoogd = "Maaiveld opgehoogd"
    Maaiveld_gedaald = "Maaiveld gedaald"
    Maaiveld_gestegen = "Maaiveld gestegen"
    Maaiveld_ingemeten = "Maaiveld ingemeten"
    Buis_gedaald = "Buis gedaald"
    Buis_gestegen = "Buis gestegen"
    ZPosities_ingemeten = "ZPosities ingemeten"
    XYPositie_ingemeten = "XYPositie ingemeten"
    XYZPositie_ingemeten = "XYZPositie ingemeten"
    Buis_ingekort = "Buis ingekort"
    Buis_opgelengd = "Buis opgelengd"
    Buisdeel_ingeplaatst = "Buisdeel ingeplaatst"
    Beschermconstructie_veranderd = "Beschermconstructie veranderd"
    Elektrodestatus_veranderd = "Elektrodestatus veranderd"
    Eigenaar_veranderd = "Eigenaar veranderd"
    Onderhouder_veranderd = "Onderhouder veranderd"
    Leverancier_veranderd = "Leverancier veranderd"
    Buisstatus_veranderd = "Buisstatus veranderd"
    Put_opgeruimd = "Put opgeruimd"
    Uit_registratie = "Uit registratie"
    Buis_bijgeplaatst = "Buis bijgeplaatst"
    Buis_vervangen = "Buis vervangen"
    Put_vervangen = "Put vervangen"
    Correctie__datumtijd_ = "Correctie (datumtijd)"
    Correctie__attribuut_ = "Correctie (attribuut)"
    Correctie__invoeging_ = "Correctie (invoeging)"
    Correctie__verwijdering_ = "Correctie (verwijdering)"
    Logger_geplaatst = "Logger geplaatst"
    Logger_verwijderd = "Logger verwijderd"
    Logger_vervangen = "Logger vervangen"
    Logger_verlaagd_ = "Logger verlaagd "
    Logger_verhoogd = "Logger verhoogd"
    Buis_schoongemaakt = "Buis schoongemaakt"


class GMWElectrodeStatusEnum(str, Enum):
    gebruiksklaar = "gebruiksklaar"
    nietGebruiksklaar = "nietGebruiksklaar"
    onbekend = "onbekend"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWElectrodePackingMaterialEnum(str, Enum):
    filtergrind = "filtergrind"
    klei = "klei"
    onbekend = "onbekend"
    zand = "zand"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMWDeliveryContextEnum(str, Enum):
    GBM = "GBM"
    KRW = "KRW"
    NBW = "NBW"
    NR = "NR"
    OGW = "OGW"
    OW = "OW"
    WW = "WW"
    archiefoverdracht = "archiefoverdracht"
    publiekeTaak = "publiekeTaak"


class GMWCorrectionReasonEnum(str, Enum):
    bronhouder = "bronhouder"
    eigenCorrectie = "eigenCorrectie"
    inOnderzoek = "inOnderzoek"
    kwaliteitsregime = "kwaliteitsregime"


class GMWCoordTransformationEnum(str, Enum):
    RDNAPTRANS2008 = "RDNAPTRANS2008"
    RDNAPTRANS2008MV0 = "RDNAPTRANS2008MV0"
    nietGetransformeerd = "nietGetransformeerd"


class GMWConstructionStandardEnum(str, Enum):
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

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMNMonitoringPurposeEnum(str, Enum):
    beheersingStedelijkGebied = "beheersingStedelijkGebied"
    gevolgenOntgronding = "gevolgenOntgronding"
    gevolgenOnttrekkingKwaliteit = "gevolgenOnttrekkingKwaliteit"
    gevolgenOnttrekkingKwantiteit = "gevolgenOnttrekkingKwantiteit"
    gevolgenPeilbeheer = "gevolgenPeilbeheer"
    gevolgenWaterstaatswerkKwaliteit = "gevolgenWaterstaatswerkKwaliteit"
    gevolgenWaterstaatswerkKwantiteit = "gevolgenWaterstaatswerkKwantiteit"
    natuurbeheer = "natuurbeheer"
    natuurbescherming = "natuurbescherming"
    onbekend = "onbekend"
    strategischBeheerKwaliteitLandelijk = "strategischBeheerKwaliteitLandelijk"
    strategischBeheerKwaliteitRegionaal = "strategischBeheerKwaliteitRegionaal"
    strategischBeheerKwantiteitLandelijk = "strategischBeheerKwantiteitLandelijk"
    strategischBeheerKwantiteitRegionaal = "strategischBeheerKwantiteitRegionaal"
    veiligstellingDrinkwatervoorzieningKwaliteit = "veiligstellingDrinkwatervoorzieningKwaliteit"
    veiligstellingDrinkwatervoorzieningKwantiteit = "veiligstellingDrinkwatervoorzieningKwantiteit"
    veiligstellingGrondwaterKwaliteit = "veiligstellingGrondwaterKwaliteit"
    veiligstellingGrondwaterKwantiteit = "veiligstellingGrondwaterKwantiteit"
    waterstaatkundigeVerzorgingKwaliteit = "waterstaatkundigeVerzorgingKwaliteit"
    waterstaatkundigeVerzorgingKwantiteit = "waterstaatkundigeVerzorgingKwantiteit"
    waterstaatswerkBeheerKwaliteit = "waterstaatswerkBeheerKwaliteit"
    waterstaatswerkBeheerKwantiteit = "waterstaatswerkBeheerKwantiteit"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMNGroundwaterAspectEnum(str, Enum):
    kwaliteit = "kwaliteit"
    kwantiteit = "kwantiteit"
    onbekend = "onbekend"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GMNEventNameEnum(str, Enum):
    Start_meetnet = "Start meetnet"
    Meetpunt_toegevoegd = "Meetpunt toegevoegd"
    Meetpunt_beëindigd = "Meetpunt beëindigd"
    Meetpunt_verplaatst = "Meetpunt verplaatst"
    Buis_vervangen = "Buis vervangen"
    Buis_bijgeplaatst = "Buis bijgeplaatst"
    leverancierVeranderd = "leverancierVeranderd"
    Einde_meetnet = "Einde meetnet"
    Uit_registratie = "Uit registratie"
    Correctie__attribuut_ = "Correctie (attribuut)"
    Correctie__datumtijd_ = "Correctie (datumtijd)"
    Correctie__invoeging_ = "Correctie (invoeging)"
    Correctie__verwijdering_ = "Correctie (verwijdering)"


class GMNDeliveryContextEnum(str, Enum):
    archiefoverdracht = "archiefoverdracht"
    drinkwaterwet = "drinkwaterwet"
    kaderrichtlijnWater = "kaderrichtlijnWater"
    ontgrondingenwet = "ontgrondingenwet"
    waterschapswet = "waterschapswet"
    waterwetGrondwaterzorgplicht = "waterwetGrondwaterzorgplicht"
    waterwetOnttrekkingInfiltratie = "waterwetOnttrekkingInfiltratie"
    waterwetPeilbeheer = "waterwetPeilbeheer"
    waterwetStrategischGrondwaterbeheer = "waterwetStrategischGrondwaterbeheer"
    waterwetWaterstaatswerkAanlegWijziging = "waterwetWaterstaatswerkAanlegWijziging"
    waterwetWaterstaatswerkBeheer = "waterwetWaterstaatswerkBeheer"
    waterwetWaterstaatswerkIngreep = "waterwetWaterstaatswerkIngreep"
    wetNatuurbescherming = "wetNatuurbescherming"


class GMNCorrectionReasonEnum(str, Enum):
    bronhouder = "bronhouder"
    eigenCorrectie = "eigenCorrectie"
    inOnderzoek = "inOnderzoek"
    kwaliteitsregime = "kwaliteitsregime"


class GLDStatusQualityControlEnum(str, Enum):
    afgekeurd = "afgekeurd"
    goedgekeurd = "goedgekeurd"
    nogNietBeoordeeld = "nogNietBeoordeeld"
    onbekend = "onbekend"
    onbeslist = "onbeslist"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GLDStatusCodeEnum(str, Enum):
    onbekend = "onbekend"
    volledigBeoordeeld = "volledigBeoordeeld"
    voorlopig = "voorlopig"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GLDProcessTypeEnum(str, Enum):
    algoritme = "algoritme"


class GLDProcessReferenceEnum(str, Enum):
    NEN5120v1991 = "NEN5120v1991"
    NEN_EN_ISO22475v2006_C11v2010 = "NEN_EN_ISO22475v2006_C11v2010"
    NEN_ISO21413v2005 = "NEN_ISO21413v2005"
    NPR_ISO_TR23211v2009 = "NPR_ISO.TR23211v2009"
    RWSgwmon = "RWSgwmon"
    STOWAgwst = "STOWAgwst"
    onbekend = "onbekend"
    vitensMeetprotocolGrondwater = "vitensMeetprotocolGrondwater"
    waternetMeetprocedure = "waternetMeetprocedure"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GLDObservationTypeEnum(str, Enum):
    controlemeting = "controlemeting"
    reguliereMeting = "reguliereMeting"


class GLDMeasurementInstrumentTypeEnum(str, Enum):
    akoestischHandapparaat = "akoestischHandapparaat"
    akoestischeSensor = "akoestischeSensor"
    analoogPeilklokje = "analoogPeilklokje"
    druksensor = "druksensor"
    elektronischPeilklokje = "elektronischPeilklokje"
    onbekend = "onbekend"
    onbekendPeilklokje = "onbekendPeilklokje"
    opzetStuk = "opzetStuk"
    radarsensor = "radarsensor"
    stereoDruksensor = "stereoDruksensor"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GLDInterpolationTypeEnum(str, Enum):
    discontinu = "discontinu"


class GLDEvaluationProcedureEnum(str, Enum):
    PMBProtocolDatakwaliteitscontroleQC2018v2_0 = "PMBProtocolDatakwaliteitscontroleQC2018v2.0"
    RWSAATGrondwaterv1_0 = "RWSAATGrondwaterv1.0"
    brabantWater2013 = "brabantWater2013"
    eijkelkampDataValidatiev0_0_9 = "eijkelkampDataValidatiev0.0.9"
    onbekend = "onbekend"
    oordeelDeskundige = "oordeelDeskundige"
    validatieprocedureEvidesWaterbedrijf = "validatieprocedureEvidesWaterbedrijf"
    vitensBeoordelingsprotocolGrondwater = "vitensBeoordelingsprotocolGrondwater"
    warecoWaterDataValidatieProtocolv20200219 = "warecoWaterDataValidatieProtocolv20200219"
    waternetBeoordelingsprocedure = "waternetBeoordelingsprocedure"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GLDCorrectionReasonEnum(str, Enum):
    bronhouder = "bronhouder"
    eigenCorrectie = "eigenCorrectie"
    inOnderzoek = "inOnderzoek"
    kwaliteitsregime = "kwaliteitsregime"


class GLDCensoredReasonEnum(str, Enum):
    groterDanLimietwaarde = "groterDanLimietwaarde"
    kleinerDanLimietwaarde = "kleinerDanLimietwaarde"
    onbekend = "onbekend"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GLDAirPressureCompensationTypeEnum(str, Enum):
    KNMImeting = "KNMImeting"
    capillair = "capillair"
    gecorrigeerdLokaleMeting = "gecorrigeerdLokaleMeting"
    monitoringnetmeting = "monitoringnetmeting"
    onbekend = "onbekend"
    putlocatiemeting = "putlocatiemeting"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GARValuationMethodEnum(str, Enum):
    AQUOKIT = "AQUOKIT"
    AUTOMATISCH = "AUTOMATISCH"
    BLAUWAP_2012 = "BLAUWAP:2012"
    CIW = "CIW"
    D1485_96 = "D1485.96"
    D38405_26_89 = "D38405-26.89"
    D38405_27_92 = "D38405-27.92"
    D38406_29_99 = "D38406-29.99"
    D38407_30_07 = "D38407-30.07"
    D38407_42_11 = "D38407-42.11"
    D38409_23_10 = "D38409-23.10"
    D4030_2_08 = "D4030-2.08"
    D51577_1_82 = "D51577-1.82"
    DESK = "DESK"
    EBEO = "EBEO"
    EPA8270CD = "EPA8270CD"
    GWPROTEU_13 = "GWPROTEU.13"
    GWPROTNL_13 = "GWPROTNL.13"
    HH_W10B_2010 = "HH-W10B:2010"
    HH_W11A_2010 = "HH-W11A:2010"
    HH_W12B_2010 = "HH-W12B:2010"
    HH_W13A_2010 = "HH-W13A:2010"
    HH_W7B_2010 = "HH-W7B:2010"
    HH_W8B_2010 = "HH-W8B:2010"
    HH_W8C_2010 = "HH-W8C:2010"
    HH_W9B_2010 = "HH-W9B:2010"
    I10048_91 = "I10048.91"
    I10260_92 = "I10260.92"
    I10301_97 = "I10301.97"
    I10304_1_09 = "I10304-1.09"
    I10304_1_95 = "I10304-1.95"
    I10304_2_96 = "I10304-2.96"
    I10304_3_97 = "I10304-3.97"
    I10304_4_99 = "I10304-4.99"
    I10359_1_92 = "I10359-1.92"
    I10359_2_94 = "I10359-2.94"
    I10382_03 = "I10382.03"
    I10523_08 = "I10523.08"
    I10523_12 = "I10523.12"
    I10523_94 = "I10523.94"
    I10530_92 = "I10530.92"
    I10566_94 = "I10566.94"
    I10695_00 = "I10695.00"
    I10704_12 = "I10704.12"
    I11083_06 = "I11083.06"
    I11083_94 = "I11083.94"
    I11369_97 = "I11369.97"
    I11423_1_97 = "I11423-1.97"
    I11423_2_97 = "I11423-2.97"
    I11731_2_08 = "I11731-2.08"
    I11731_98 = "I11731.98"
    I11732_05 = "I11732.05"
    I11885_07 = "I11885.07"
    I11885_98 = "I11885.98"
    I11905_1_98 = "I11905-1.98"
    I11923_97 = "I11923.97"
    I11969_97 = "I11969.97"
    I12010_14 = "I12010.14"
    I12020_00 = "I12020.00"
    I12846_12 = "I12846.12"
    I13358_97 = "I13358.97"
    I13395_97 = "I13395.97"
    I14402_99 = "I14402.99"
    I14403_2_09 = "I14403-2.09"
    I14403_2_12 = "I14403-2.12"
    I14403_02 = "I14403.02"
    I14911_99 = "I14911.99"
    I15061_01 = "I15061.01"
    I15089_00 = "I15089.00"
    I15586_03 = "I15586.03"
    I15587_1_02 = "I15587-1.02"
    I15587_2_02 = "I15587-2.02"
    I15680_03 = "I15680.03"
    I15681_1_05 = "I15681-1.05"
    I15681_2_05 = "I15681-2.05"
    I15682_01 = "I15682.01"
    I15705_03 = "I15705.03"
    I15913_03 = "I15913.03"
    I15923_1_13 = "I15923-1.13"
    I16264_02 = "I16264.02"
    I16264_04 = "I16264.04"
    I16588_03 = "I16588.03"
    I16590_00 = "I16590.00"
    I17294_1_06 = "I17294-1.06"
    I17294_2_04 = "I17294-2.04"
    I17294_2_16 = "I17294-2.16"
    I17353_05 = "I17353.05"
    I17380_06 = "I17380.06"
    I17495_03 = "I17495.03"
    I17852_06 = "I17852.06"
    I17852_08 = "I17852.08"
    I17858_07 = "I17858.07"
    I17993_04 = "I17993.04"
    I18073_04 = "I18073.04"
    I18412_06 = "I18412.06"
    I18856_05 = "I18856.05"
    I18857_1_06 = "I18857-1.06"
    I20179_05 = "I20179.05"
    I22032_06 = "I22032.06"
    I22155_05 = "I22155.05"
    I22478_06 = "I22478.06"
    I22743_06 = "I22743.06"
    I23631_06 = "I23631.06"
    I23913_06 = "I23913.06"
    I25101_09 = "I25101.09"
    I5663_93 = "I5663.93"
    I5664_04 = "I5664.04"
    I5666_99 = "I5666.99"
    I5667_1_94 = "I5667-1.94"
    I5667_11_09 = "I5667-11.09"
    I5667_11_93 = "I5667-11.93"
    I5667_2_93 = "I5667-2.93"
    I5667_3_12 = "I5667-3.12"
    I5813_93 = "I5813.93"
    I5814_93 = "I5814.93"
    I5815_1_03 = "I5815-1.03"
    I5815_2_03 = "I5815-2.03"
    I5961_95 = "I5961.95"
    I6058_84 = "I6058.84"
    I6059_05 = "I6059.05"
    I6060_89 = "I6060.89"
    I6332_04 = "I6332.04"
    I6333_88 = "I6333.88"
    I6340_93 = "I6340.93"
    I6439_90 = "I6439.90"
    I6468_97 = "I6468.97"
    I6595_93 = "I6595.93"
    I6703_1_84 = "I6703-1.84"
    I6703_2_84 = "I6703-2.84"
    I6703_3_84 = "I6703-3.84"
    I6777_93 = "I6777.93"
    I6778_84 = "I6778.84"
    I6878_04 = "I6878.04"
    I7027_00 = "I7027.00"
    I7027_16 = "I7027.16"
    I7027_94 = "I7027.94"
    I7150_1_02 = "I7150-1.02"
    I7393_1_00 = "I7393-1.00"
    I7393_2_00 = "I7393-2.00"
    I7393_3_00 = "I7393-3.00"
    I7875_1_96 = "I7875-1.96"
    I7875_2_84 = "I7875-2.84"
    I7887_12 = "I7887.12"
    I7887_94 = "I7887.94"
    I7888_94 = "I7888.94"
    I7890_3_99 = "I7890-3.99"
    I7899_1_98 = "I7899-1.98"
    I7980_00 = "I7980.00"
    I7981_1_05 = "I7981-1.05"
    I7981_2_05 = "I7981-2.05"
    I8165_1_92 = "I8165-1.92"
    I8165_2_99 = "I8165-2.99"
    I8245_99 = "I8245.99"
    I8288_86 = "I8288.86"
    I8467_95 = "I8467.95"
    I9174_98 = "I9174.98"
    I9297_89 = "I9297.89"
    I9308_3_99 = "I9308-3.99"
    I9377_1_00 = "I9377-1.00"
    I9377_2_00 = "I9377-2.00"
    I9377_4_99 = "I9377-4.99"
    I9390_90 = "I9390.90"
    I9562_04 = "I9562.04"
    I9697_92 = "I9697.92"
    I9698_89 = "I9698.89"
    I9963_1_94 = "I9963-1.94"
    I9963_1_96 = "I9963-1.96"
    I9963_2_94 = "I9963-2.94"
    I9963_2_96 = "I9963-2.96"
    I9964_1_93 = "I9964-1.93"
    I9964_2_93 = "I9964-2.93"
    I9964_3_93 = "I9964-3.93"
    I9965_93 = "I9965.93"
    KNMI5WIND_01 = "KNMI5WIND.01"
    KRW = "KRW"
    LEIDDPS_2012 = "LEIDDPS:2012"
    MODEL = "MODEL"
    N12260_03 = "N12260.03"
    N1233_97 = "N1233.97"
    N12338_98 = "N12338.98"
    N12673_99 = "N12673.99"
    N12880_01 = "N12880.01"
    N12918_99 = "N12918.99"
    N13506_01 = "N13506.01"
    N13577_07 = "N13577.07"
    N14207_03 = "N14207.03"
    N14486_05 = "N14486.05"
    N1483_07 = "N1483.07"
    N1484_97 = "N1484.97"
    N15216_07 = "N15216.07"
    N1622_06 = "N1622.06"
    N1899_1_98 = "N1899-1.98"
    N1899_2_98 = "N1899-2.98"
    N3106_86 = "N3106.86"
    N5622_06 = "N5622.06"
    N5623_02 = "N5623.02"
    N5627_06 = "N5627.06"
    N5694_C1_11 = "N5694+C1.11"
    N5707_C1_06 = "N5707+C1.06"
    N5731_94 = "N5731.94"
    N5734_95 = "N5734.95"
    N5734_99 = "N5734.99"
    N5735_94 = "N5735.94"
    N5742_00 = "N5742.00"
    N5742_91 = "N5742.91"
    N5747_90 = "N5747.90"
    N5748_90 = "N5748.90"
    N5750_89 = "N5750.89"
    N5751_89 = "N5751.89"
    N5753_06 = "N5753.06"
    N5754_05 = "N5754.05"
    N5757_91 = "N5757.91"
    N5758_90 = "N5758.90"
    N5759_90 = "N5759.90"
    N5761_90 = "N5761.90"
    N5762_91 = "N5762.91"
    N5763_91 = "N5763.91"
    N5764_89 = "N5764.89"
    N5765_91 = "N5765.91"
    N5767_91 = "N5767.91"
    N5769_91 = "N5769.91"
    N5777_94 = "N5777.94"
    N5779_94 = "N5779.94"
    N5897_14 = "N5897.14"
    N6265_07 = "N6265.07"
    N6274_95 = "N6274.95"
    N6401_91 = "N6401.91"
    N6402_10 = "N6402.10"
    N6402_91 = "N6402.91"
    N6403_98 = "N6403.98"
    N6407_97 = "N6407.97"
    N6408_99 = "N6408.99"
    N6411_06 = "N6411.06"
    N6411_81 = "N6411.81"
    N6412_79 = "N6412.79"
    N6414_07 = "N6414.07"
    N6414_08 = "N6414.08"
    N6414_88 = "N6414.88"
    N6415_82 = "N6415.82"
    N6420_86 = "N6420.86"
    N6421_06 = "N6421.06"
    N6424_88 = "N6424.88"
    N6426_95 = "N6426.95"
    N6427_99 = "N6427.99"
    N6429_94 = "N6429.94"
    N6430_94 = "N6430.94"
    N6432_93 = "N6432.93"
    N6433_93 = "N6433.93"
    N6434_93 = "N6434.93"
    N6435_97 = "N6435.97"
    N6436_97 = "N6436.97"
    N6437_82 = "N6437.82"
    N6441_79 = "N6441.79"
    N6442_79 = "N6442.79"
    N6443_77 = "N6443.77"
    N6444_77 = "N6444.77"
    N6445_97 = "N6445.97"
    N6448_81 = "N6448.81"
    N6449_81 = "N6449.81"
    N6451_80 = "N6451.80"
    N6452_80 = "N6452.80"
    N6453_80 = "N6453.80"
    N6454_94 = "N6454.94"
    N6455_81 = "N6455.81"
    N6456_81 = "N6456.81"
    N6457_94 = "N6457.94"
    N6458_83 = "N6458.83"
    N6460_81 = "N6460.81"
    N6461_81 = "N6461.81"
    N6462_82 = "N6462.82"
    N6463_97 = "N6463.97"
    N6465_92 = "N6465.92"
    N6467_82 = "N6467.82"
    N6468_94 = "N6468.94"
    N6470_97 = "N6470.97"
    N6471_81 = "N6471.81"
    N6472_83 = "N6472.83"
    N6476_81 = "N6476.81"
    N6480_82 = "N6480.82"
    N6481_83 = "N6481.83"
    N6482_82 = "N6482.82"
    N6483_82 = "N6483.82"
    N6484_06 = "N6484.06"
    N6484_07 = "N6484.07"
    N6484_82 = "N6484.82"
    N6485_83 = "N6485.83"
    N6486_84 = "N6486.84"
    N6487_97 = "N6487.97"
    N6490_82 = "N6490.82"
    N6493_87 = "N6493.87"
    N6494_84 = "N6494.84"
    N6495_84 = "N6495.84"
    N6499_05 = "N6499.05"
    N6499_10 = "N6499.10"
    N6520_06 = "N6520.06"
    N6521_91 = "N6521.91"
    N6523_90 = "N6523.90"
    N6524_84 = "N6524.84"
    N6526_06 = "N6526.06"
    N6527_00 = "N6527.00"
    N6530_86 = "N6530.86"
    N6531_86 = "N6531.86"
    N6532_86 = "N6532.86"
    N6533_90 = "N6533.90"
    N6535_86 = "N6535.86"
    N6536_90 = "N6536.90"
    N6539_91 = "N6539.91"
    N6541_91 = "N6541.91"
    N6542_96 = "N6542.96"
    N6544_90 = "N6544.90"
    N6545_85 = "N6545.85"
    N6547_86 = "N6547.86"
    N6548_88 = "N6548.88"
    N6549_88 = "N6549.88"
    N6563_82 = "N6563.82"
    N6567_85 = "N6567.85"
    N6576_85 = "N6576.85"
    N6577_85 = "N6577.85"
    N6578_85 = "N6578.85"
    N6579_85 = "N6579.85"
    N6580_85 = "N6580.85"
    N6581_85 = "N6581.85"
    N6582_85 = "N6582.85"
    N6587_90 = "N6587.90"
    N6589_05 = "N6589.05"
    N6591_90 = "N6591.90"
    N6594_93 = "N6594.93"
    N6604_07 = "N6604.07"
    N6606_07 = "N6606.07"
    N6606_09 = "N6606.09"
    N6606_92 = "N6606.92"
    N6608_96 = "N6608.96"
    N6609_97 = "N6609.97"
    N6611_97 = "N6611.97"
    N6612_97 = "N6612.97"
    N6619_92 = "N6619.92"
    N6620_86 = "N6620.86"
    N6621_88 = "N6621.88"
    N6623_05 = "N6623.05"
    N6633_06 = "N6633.06"
    N6633_98 = "N6633.98"
    N6634_91 = "N6634.91"
    N6641_83 = "N6641.83"
    N6642_92 = "N6642.92"
    N6643_03 = "N6643.03"
    N6644_83 = "N6644.83"
    N6645_05 = "N6645.05"
    N6646_C1_15 = "N6646+C1.15"
    N6646_06 = "N6646.06"
    N6646_15 = "N6646.15"
    N6651_92 = "N6651.92"
    N6652_92 = "N6652.92"
    N6653_92 = "N6653.92"
    N6654_92 = "N6654.92"
    N6655_92 = "N6655.92"
    N6655_97 = "N6655.97"
    N6662_85 = "N6662.85"
    N6663_87 = "N6663.87"
    N6669_81 = "N6669.81"
    N6670_03 = "N6670.03"
    N6671_13 = "N6671.13"
    N6671_94 = "N6671.94"
    N6672_94 = "N6672.94"
    N6674_81 = "N6674.81"
    N6675_89 = "N6675.89"
    N6676_94 = "N6676.94"
    N6953_05 = "N6953.05"
    N6953_17 = "N6953.17"
    N6961_05 = "N6961.05"
    N6961_13 = "N6961.13"
    N6963_05 = "N6963.05"
    N6964_C1_06 = "N6964+C1.06"
    N6964_05 = "N6964.05"
    N6965_C1_06 = "N6965+C1.06"
    N6965_05 = "N6965.05"
    N6966_C1_06 = "N6966+C1.06"
    N6966_05 = "N6966.05"
    N6970_08 = "N6970.08"
    N6975_08 = "N6975.08"
    N6978_08 = "N6978.08"
    N6980_C1_10 = "N6980+C1.10"
    N7341_95 = "N7341.95"
    N7343_95 = "N7343.95"
    N7345_95 = "N7345.95"
    N7349_95 = "N7349.95"
    N872_05 = "N872.05"
    N903_94 = "N903.94"
    Notove = "Notove"
    OVAM2IB1 = "OVAM2IB1"
    OVAM2IC2_3 = "OVAM2IC2.3"
    OVAM2IIA3 = "OVAM2IIA3"
    OVAM2IIA6 = "OVAM2IIA6"
    OVAM3B = "OVAM3B"
    OVAM3I = "OVAM3I"
    OVAM3N = "OVAM3N"
    OVAM3R1 = "OVAM3R1"
    P3210_1_16 = "P3210-1.16"
    P3210_2_16 = "P3210-2.16"
    P3210_3_16 = "P3210-3.16"
    P3210_4_16 = "P3210-4.16"
    P3210_5_16 = "P3210-5.16"
    P3210_6_16 = "P3210-6.16"
    P3210_7_16 = "P3210-7.16"
    P3220_1_16 = "P3220-1.16"
    P3220_2_16 = "P3220-2.16"
    P3250_1_16 = "P3250-1.16"
    P3260_1_11 = "P3260-1.11"
    P5637_06 = "P5637.06"
    P5638_06 = "P5638.06"
    P6266_14 = "P6266.14"
    P6266_91 = "P6266.91"
    P6400_88 = "P6400.88"
    P6416_95 = "P6416.95"
    P6417_97 = "P6417.97"
    P6425_95 = "P6425.95"
    P6537_88 = "P6537.88"
    P6538_90 = "P6538.90"
    P6546_88 = "P6546.88"
    P6600_93 = "P6600.93"
    P6616_82 = "P6616.82"
    PZMJK_A = "PZMJK-A"
    PZMJK_C = "PZMJK-C"
    PZMJK_D = "PZMJK-D"
    RWS_RMI_10 = "RWS-RMI.10"
    RWSV_A1_002 = "RWSV-A1.002"
    RWSV_A1_019 = "RWSV-A1.019"
    RWSV_A1_032 = "RWSV-A1.032"
    RWSV_A1_033 = "RWSV-A1.033"
    RWSV_A1_035 = "RWSV-A1.035"
    RWSV_A1_040 = "RWSV-A1.040"
    RWSV_A1_072 = "RWSV-A1.072"
    RWSV_A1_085 = "RWSV-A1.085"
    RWSV_A1_086 = "RWSV-A1.086"
    RWSV_A3_010 = "RWSV-A3.010"
    RWSV_A4_411 = "RWSV-A4.411"
    RWSV_A5_380 = "RWSV-A5.380"
    RWSV_A5_390 = "RWSV-A5.390"
    RWSV_A5_393 = "RWSV-A5.393"
    RWSV_A5_398 = "RWSV-A5.398"
    RWSV_A5_427 = "RWSV-A5.427"
    RWSV_W006 = "RWSV-W006"
    RWSV_W007 = "RWSV-W007"
    RWSV_W008 = "RWSV-W008"
    RWSV_W009 = "RWSV-W009"
    RWSV_W012 = "RWSV-W012"
    T11370_00 = "T11370.00"
    T11905_2_97 = "T11905-2.97"
    T8200_02 = "T8200.02"
    T8204_03 = "T8204.03"
    Towabo = "Towabo"
    V2946_89 = "V2946.89"
    V5694_96 = "V5694.96"
    V5718_94 = "V5718.94"
    V5730_91 = "V5730.91"
    V5732_99 = "V5732.99"
    V5770_93 = "V5770.93"
    V6404_00 = "V6404.00"
    V6409_97 = "V6409.97"
    V6419_06 = "V6419.06"
    V6590_90 = "V6590.90"
    V6592_90 = "V6592.90"
    V6678_97 = "V6678.97"
    V6982_06 = "V6982.06"
    V6983_06 = "V6983.06"
    V6984_06 = "V6984.06"
    V7321_97 = "V7321.97"
    V7322_97 = "V7322.97"
    V7324_97 = "V7324.97"
    V7350_95 = "V7350.95"
    VOORLOPIG = "VOORLOPIG"
    ZINTUIGLIJK = "ZINTUIGLIJK"
    iWSR = "iWSR"


class GARSamplingStandardEnum(str, Enum):
    NEN5744v1991 = "NEN5744v1991"
    NEN5744v2011_A1v2013 = "NEN5744v2011-A1v2013"
    NEN5745v1997 = "NEN5745v1997"
    NTA8017v2008 = "NTA8017v2008"
    NTA8017v2016 = "NTA8017v2016"
    SIKBProtocol2002vanafV4 = "SIKBProtocol2002vanafV4"
    onbekend = "onbekend"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GARQualityControlStatusEnum(str, Enum):
    afgekeurd = "afgekeurd"
    goedgekeurd = "goedgekeurd"
    onbekend = "onbekend"
    onbeslist = "onbeslist"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GARQualityControlMethodEnum(str, Enum):
    handboekProvinciesRIVMv2017 = "handboekProvinciesRIVMv2017"
    onbekend = "onbekend"
    oordeelDeskundige = "oordeelDeskundige"
    qCProtocolProvinciesEnRIVMv2021 = "qCProtocolProvinciesEnRIVMv2021"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GARPumpTypeEnum(str, Enum):
    anders = "anders"
    onbekend = "onbekend"
    onderwaterpomp = "onderwaterpomp"
    peristaltischePomp = "peristaltischePomp"
    vacuumpomp = "vacuumpomp"

    @classmethod
    def _missing_(cls, value):
        return cls.onbekend


class GARLimitSymbolEnum(str, Enum):
    GT = "GT"
    LT = "LT"


class GARCorrectionReasonEnum(str, Enum):
    bronhouder = "bronhouder"
    eigenCorrectie = "eigenCorrectie"
    inOnderzoek = "inOnderzoek"
    kwaliteitsregime = "kwaliteitsregime"


class GARColourStrengthEnum(str, Enum):
    donker = "donker"
    licht = "licht"
    neutraal = "neutraal"
    zeer_donker = "zeer donker"
    zeer_licht = "zeer licht"


class GARColourEnum(str, Enum):
    beige = "beige"
    blauw = "blauw"
    bruin = "bruin"
    creme = "creme"
    geel = "geel"
    grijs = "grijs"
    groen = "groen"
    kleurloos = "kleurloos"
    oranje = "oranje"
    paars = "paars"
    roestbruin = "roestbruin"
    rood = "rood"
    wit = "wit"
    zwart = "zwart"


class GARAnalyticalTechniqueEnum(str, Enum):
    AA = "AA"
    AA_FOTM = "AA-FOTM"
    AAS = "AAS"
    AAS_F = "AAS-F"
    AAS_GF = "AAS-GF"
    AAS_HG = "AAS-HG"
    AAS_KD = "AAS-KD"
    AERO = "AERO"
    AES_F = "AES-F"
    AES_KD = "AES-KD"
    AF = "AF"
    AF_KD = "AF-KD"
    BACT = "BACT"
    CALO = "CALO"
    COND = "COND"
    COUL = "COUL"
    CUVT = "CUVT"
    DA = "DA"
    DA_S = "DA-S"
    ELCH = "ELCH"
    ELMSR = "ELMSR"
    FL = "FL"
    FOTM = "FOTM"
    GAMMAS = "GAMMAS"
    GC = "GC"
    GC_ECD = "GC-ECD"
    GC_ECD_ECD = "GC-ECD/ECD"
    GC_ECD_MS = "GC-ECD/MS"
    GC_FID = "GC-FID"
    GC_FID_ECD = "GC-FID/ECD"
    GC_FID_IR = "GC-FID/IR"
    GC_FPD = "GC-FPD"
    GC_HRMS = "GC-HRMS"
    GC_LRMS = "GC-LRMS"
    GC_MS = "GC-MS"
    GC_MS_HS = "GC-MS-HS"
    GC_MS_LV_PTV = "GC-MS-LV-PTV"
    GC_MS_MS = "GC-MS-MS"
    GC_MS_PT = "GC-MS-PT"
    GC_MS_PTV = "GC-MS-PTV"
    GC_MS_TD = "GC-MS-TD"
    GC_NPD = "GC-NPD"
    GENEPSLCFRSE = "GENEPSLCFRSE"
    GRAV = "GRAV"
    HPLC = "HPLC"
    HPLC_APCI_MS = "HPLC-APCI-MS"
    HPLC_DAD = "HPLC-DAD"
    HPLC_FL = "HPLC-FL"
    HPLC_MS_ESI = "HPLC-MS-ESI"
    HPLC_UV = "HPLC-UV"
    HPLC_UV_FL = "HPLC-UV-FL"
    IC = "IC"
    ICP_AES = "ICP-AES"
    ICP_HRMS = "ICP-HRMS"
    ICP_MS = "ICP-MS"
    IR = "IR"
    IR_FT = "IR-FT"
    JODM = "JODM"
    LC_FL = "LC-FL"
    LC_GC_MS = "LC-GC-MS"
    LC_MS = "LC-MS"
    LC_MS_MS = "LC-MS-MS"
    LC_TQMS = "LC-TQMS"
    LDO = "LDO"
    LSC = "LSC"
    MEMBF = "MEMBF"
    MICCOUL = "MICCOUL"
    MICCOUL_PT = "MICCOUL-PT"
    MICSCOP = "MICSCOP"
    MICTTPT = "MICTTPT"
    NEFLMTE = "NEFLMTE"
    ORGNLTSCH = "ORGNLTSCH"
    POTM = "POTM"
    POTM_TITM = "POTM_TITM"
    RADOMT_BWHH = "RADOMT-BWHH"
    RADOMT_BWHHG = "RADOMT-BWHHG"
    RADOMT_BWVO = "RADOMT-BWVO"
    RONTGDF = "RONTGDF"
    RONTGTM = "RONTGTM"
    RONTGTM_GRAV = "RONTGTM_GRAV"
    SEDI = "SEDI"
    STER_POLMIC = "STER/POLMIC"
    THERMG = "THERMG"
    THERMM = "THERMM"
    TITM = "TITM"
    UV_VIS = "UV/VIS"
    VISL = "VISL"
    VOL = "VOL"
    qPCR = "qPCR"


class COMQualityRegimeEnum(int, Enum):
    Bron = 0
    IMBRO_A = 1
    IMBRO = 2


class GLDEventNameEnum(str, Enum):
    Start_registratie = "Start registratie"
    Meetreeks = "Meetreeks"
    Controlereeks = "Controlereeks"
    Einde_registratie = "Einde registratie"
    Leverancier_veranderd = "Leverancier veranderd"
    Uit_registratie = "Uit registratie"
    Correctie__attribuut_ = "Correctie (attribuut)"
    Correctie__metingen_ = "Correctie (metingen)"
    Correctie__datumtijd_ = "Correctie (datumtijd)"
    Correctie__invoeging_ = "Correctie (invoeging)"
    Correctie__verwijdering_ = "Correctie (verwijdering)"
