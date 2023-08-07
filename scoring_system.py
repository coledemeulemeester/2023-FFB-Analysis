class ScoringSystem:
    """
    Defines the scoring system for a league
    """

    def __init__(
            self,
            PY=0.04,
            PTD=4,
            PTD40=1,
            PTD50=1,
            INT=-2,
            TWPC=2,
            P300=1,
            P400=2,
            # Rushing,
            RY=0.1,
            RTD=6,
            RTD40=1,
            RTD50=1,
            TWPR=2,
            RY100=1,
            RY200=2,
            # Receiving,
            REY=0.1,
            RETD=6,
            RETD40=1,
            RETD50=1,
            TWPRE=2,
            REY100=1,
            REY200=2,
            Kicking,
            PAT=1,
            FGM=-1,
            FG0=3,
            FG40=4,
            FG50=5,
            FG60=5,
            # Team Defense / Special Teams,
            KRTD=6,
            PRTD=6,
            INTTD=6,
            FRTD=6,
            BLKKRTD=6,
            TWPTRET=2,
            PSF = 1,
            SK=1,
            BLKK=2,
            INT=2,
            FR=2,
            SF=2,
            PA0=5,
            PA1=4,
            PA7=3,
            PA14=1,
            PA28=-1,
            PA35=-2,
            PA46=-3,
            YA100=5,
            YA199=3,
            YA299=2,
            YA399=-1,
            YA449=-2,
            YA499=-3,
            YA549=-4,
            YA550=-5,
            # Miscellaneous,
            KR25=1,
            PR25=2.5,
            KRTD=6,
            PRTD=6,
            FTD=6,
            FUML=-2,
            INTTD=6,
            FRTD=6,
            BLKKRTD=6,
            TWPTRET=2
    ):
        self.PY = 0.04
        self.PTD = 4
        self.PTD40 = 1
        self.PTD50 = 1
        self.INT = -2
        self.TWOPC = 2
        self.P300 = 1
        self.P400 = 2
        # Rushing
        self.RY = 0.1
        self.RTD = 6
        self.RTD40 = 1
        self.RTD50 = 1
        self.TWOPR = 2
        self.RY100 = 1
        self.RY200 = 2
        # Receiving
        self.REY = 0.1
        self.RETD = 6
        self.RETD40 = 1
        self.RETD50 = 1
        self.TWOPRE = 2
        self.REY100 = 1
        self.REY200 = 2
        # Kicking
        self.PAT = 1
        self.FGM = -1
        self.FG0 = 3
        self.FG40 = 4
        self.FG50 = 5
        self.FG60 = 5
        # Team Defense / Special Teams
        self.KRTD = 6
        self.PRTD = 6
        self.INTTD = 6
        self.FRTD = 6
        self.BLKKRTD = 6
        self.TWOPTRET = 2
        self.ONEPSF = 1
        self.SK = 1
        self.BLKK = 2
        self.INT = 2
        self.FR = 2
        self.SF = 2
        self.PA0 = 5
        self.PA1 = 4
        self.PA7 = 3
        self.PA14 = 1
        self.PA28 = -1
        self.PA35 = -2
        self.PA46 = -3
        self.YA100 = 5
        self.YA199 = 3
        self.YA299 = 2
        self.YA399 = -1
        self.YA449 = -2
        self.YA499 = -3
        self.YA549 = -4
        self.YA550 = -5
        # Miscellaneous
        self.KR25 = 1
        self.PR25 = 2.5
        self.KRTD = 6
        self.PRTD = 6
        self.FTD = 6
        self.FUML = -2
        self.INTTD = 6
        self.FRTD = 6
        self.BLKKRTD = 6
        self.TWOPTRET = 2

