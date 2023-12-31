class BarcodeType(object):
    CODE11 = 1  # Code 11
    C25STANDARD = 2  # Standard Code 2 of 5
    C25INTER = 3  # Interleaved 2 of 5
    C25IATA = 4  # Code 2 of 5 IATA
    C25LOGIC = 6  # Code 2 of 5 Data Logic
    C25IND = 7  # Code 2 of 5 Industrial
    CODE39 = 8  # Code 3 of 9 (Code 39)
    EXCODE39 = 9  # Extended Code 3 of 9 (Code 39+)
    EANX = 13  # EAN (EAN-2, EAN-5, EAN-8 and EAN-13)
    EANX_CHK = 14  # EAN + Check Digit
    GS1_128 = 16  # GS1-128 (UCC.EAN-128)
    CODABAR = 18  # Codabar
    CODE128 = 20  # Code 128 (automatic Code Set switching)
    DPLEIT = 21  # Deutsche Post Leitcode
    DPIDENT = 22  # Deutsche Post Identcode
    CODE16K = 23  # Code 16K
    CODE49 = 24  # Code 49
    CODE93 = 25  # Code 93
    FLAT = 28  # Flattermarken
    DBAR_OMN = 29  # GS1 DataBar Omnidirectional (including GS1 DataBar Truncated)
    DBAR_LTD = 30  # GS1 DataBar Limited
    DBAR_EXP = 31  # GS1 DataBar Expanded
    TELEPEN = 32  # Telepen Alpha
    UPCA = 34  # UPC-A
    UPCA_CHK = 35  # UPC-A + Check Digit
    UPCE = 37  # UPC-E
    UPCE_CHK = 38  # UPC-E + Check Digit
    POSTNET = 40  # POSTNET
    MSI_PLESSEY = 47  # MSI Plessey
    FIM = 49  # FIM
    LOGMARS = 50  # LOGMARS
    PHARMA = 51  # Pharmacode One-Track
    PZN = 52  # PZN
    PHARMA_TWO = 53  # Pharmacode Two-Track
    CEPNET = 54  # Brazilian CEPNet
    PDF417 = 55  # PDF417
    PDF417COMP = 56  # Compact PDF417 (Truncated PDF417)
    MAXICODE = 57  # MaxiCode
    QRCODE = 58  # QR Code
    CODE128AB = 60  # Code 128 (Suppress Code Set C)
    AUSPOST = 63  # Australia Post Standard Customer
    AUSREPLY = 66  # Australia Post Reply Paid
    AUSROUTE = 67  # Australia Post Routing
    AUSDIRECT = 68  # Australia Post Redirection
    ISBNX = 69  # ISBN (EAN-13 with verification stage)
    RM4SCC = 70  # Royal Mail 4-State Customer Code (RM4SCC)
    DATAMATRIX = 71  # Data Matrix (ECC200)
    EAN14 = 72  # EAN-14
    VIN = 73  # Vehicle Identification Number
    CODABLOCKF = 74  # Codablock-F
    NVE18 = 75  # NVE-18 (SSCC-18)
    JAPANPOST = 76  # Japanese Postal Code
    KOREAPOST = 77  # Korea Post
    DBAR_STK = 79  # GS1 DataBar Stacked
    DBAR_OMNSTK = 80  # GS1 DataBar Stacked Omnidirectional
    DBAR_EXPSTK = 81  # GS1 DataBar Expanded Stacked
    PLANET = 82  # PLANET
    MICROPDF417 = 84  # MicroPDF417
    USPS_IMAIL = 85  # USPS Intelligent Mail (OneCode)
    PLESSEY = 86  # UK Plessey
    TELEPEN_NUM = 87  # Telepen Numeric
    ITF14 = 89  # ITF-14
    KIX = 90  # Dutch Post KIX Code
    AZTEC = 92  # Aztec Code
    DAFT = 93  # DAFT Code
    DPD = 96  # DPD Code
    MICROQR = 97  # Micro QR Code
    HIBC_128 = 98  # HIBC Code 128
    HIBC_39 = 99  # HIBC Code 39
    HIBC_DM = 102  # HIBC Data Matrix ECC200
    HIBC_QR = 104  # HIBC QR Code
    HIBC_PDF = 106  # HIBC PDF417
    HIBC_MICPDF = 108  # HIBC MicroPDF417
    HIBC_BLOCKF = 110  # HIBC Codablock-F
    HIBC_AZTEC = 112  # HIBC Aztec Code
    DOTCODE = 115  # DotCode
    HANXIN = 116  # Han Xin (Chinese Sensible) Code
    MAILMARK_2D = 119  # Royal Mail 2D Mailmark (CMDM) (DataMatrix)
    MAILMARK_4S = 121  # Royal Mail 4-State Mailmark
    AZRUNE = 128  # Aztec Runes
    CODE32 = 129  # Code 32
    EANX_CC = 130  # GS1 Composite Symbol with EAN linearcomponent
    GS1_128_CC = 131  # GS1 Composite Symbol with GS1-128 linearcomponent
    DBAR_OMN_CC = 132  # GS1 Composite Symbol with GS1 DataBarOmnidirectional linear component
    DBAR_LTD_CC = 133  # GS1 Composite Symbol with GS1 DataBarLimited linear component
    DBAR_EXP_CC = 134  # GS1 Composite Symbol with GS1 DataBarExpanded linear component
    UPCA_CC = 135  # GS1 Composite Symbol with UPC-A linear component
    UPCE_CC = 136  # GS1 Composite Symbol with UPC-E linear
    DBAR_STK_CC = 137  # GS1 Composite Symbol with GS1 DataBar Stacked component
    DBAR_OMNSTK_CC = 138  # GS1 Composite Symbol with GS1 DataBar Stacked Omnidirectional component
    DBAR_EXPSTK_CC = 139  # GS1 Composite Symbol with GS1 DataBar Expanded Stacked component
    CHANNEL = 140  # Channel Code
    CODEONE = 141  # Code One
    GRIDMATRIX = 142  # Grid Matrix
    UPNQR = 143  # UPNQR (Univerzalnega Plačilnega Naloga QR)
    ULTRA = 144  # Ultracode
    RMQR = 145  # Rectangular Micro QR Code (rMQR)
    BC412 = 146  # IBM BC412 (SEMI T1-95)
