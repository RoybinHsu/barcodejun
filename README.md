### 项目说明

#### 支持的barcode类型

- CODE11 # Code 11
- C25STANDARD # Standard Code 2 of 5
- C25INTER # Interleaved 2 of 5
- C25IATA # Code 2 of 5 IATA
- C25LOGIC # Code 2 of 5 Data Logic
- C25IND # Code 2 of 5 Industrial
- CODE39 # Code 3 of 9 (Code 39)
- EXCODE39 # Extended Code 3 of 9 (Code 39+)
- EANX # EAN (EAN-2, EAN-5, EAN-8 and EAN-13)
- EANX_CHK # EAN + Check Digit
- GS1_128 # GS1-128 (UCC.EAN-128)
- CODABAR # Codabar
- CODE128 # Code 128 (automatic Code Set switching)
- DPLEIT # Deutsche Post Leitcode
- DPIDENT # Deutsche Post Identcode
- CODE16K # Code 16K
- CODE49 # Code 49
- CODE93 # Code 93
- FLAT # Flattermarken
- DBAR_OMN # GS1 DataBar Omnidirectional (including GS1 DataBar Truncated)
- DBAR_LTD # GS1 DataBar Limited
- DBAR_EXP # GS1 DataBar Expanded
- TELEPEN # Telepen Alpha
- UPCA # UPC-A
- UPCA_CHK # UPC-A + Check Digit
- UPCE # UPC-E
- UPCE_CHK # UPC-E + Check Digit
- POSTNET # POSTNET
- MSI_PLESSEY # MSI Plessey
- FIM # FIM
- LOGMARS # LOGMARS
- PHARMA # Pharmacode One-Track
- PZN # PZN
- PHARMA_TWO # Pharmacode Two-Track
- CEPNET # Brazilian CEPNet
- PDF417 # PDF417
- PDF417COMP # Compact PDF417 (Truncated PDF417)
- MAXICODE # MaxiCode
- QRCODE # QR Code
- CODE128AB # Code 128 (Suppress Code Set C)
- AUSPOST # Australia Post Standard Customer
- AUSREPLY # Australia Post Reply Paid
- AUSROUTE # Australia Post Routing
- AUSDIRECT # Australia Post Redirection
- ISBNX # ISBN (EAN-13 with verification stage)
- RM4SCC # Royal Mail 4-State Customer Code (RM4SCC)
- DATAMATRIX # Data Matrix (ECC200)，GS1 Datamatrix
- EAN14 # EAN-14
- VIN # Vehicle Identification Number
- CODABLOCKF # Codablock-F
- NVE18 # NVE-18 (SSCC-18)
- JAPANPOST # Japanese Postal Code
- KOREAPOST # Korea Post
- DBAR_STK # GS1 DataBar Stacked
- DBAR_OMNSTK # GS1 DataBar Stacked Omnidirectional
- DBAR_EXPSTK # GS1 DataBar Expanded Stacked
- PLANET # PLANET
- MICROPDF417 # MicroPDF417
- USPS_IMAIL # USPS Intelligent Mail (OneCode)
- PLESSEY # UK Plessey
- TELEPEN_NUM # Telepen Numeric
- ITF14 # ITF-14
- KIX # Dutch Post KIX Code
- AZTEC # Aztec Code
- DAFT # DAFT Code
- DPD # DPD Code
- MICROQR # Micro QR Code
- HIBC_128 # HIBC Code 128
- HIBC_39 # HIBC Code 39
- HIBC_DM # HIBC Data Matrix ECC200
- HIBC_QR # HIBC QR Code
- HIBC_PDF # HIBC PDF417
- HIBC_MICPDF # HIBC MicroPDF417
- HIBC_BLOCKF # HIBC Codablock-F
- HIBC_AZTEC # HIBC Aztec Code
- DOTCODE # DotCode
- HANXIN # Han Xin (Chinese Sensible) Code
- MAILMARK_2D # Royal Mail 2D Mailmark (CMDM) (DataMatrix)
- MAILMARK_4S # Royal Mail 4-State Mailmark
- AZRUNE # Aztec Runes
- CODE32 # Code 32
- EANX_CC # GS1 Composite Symbol with EAN linearcomponent
- GS1_128_CC # GS1 Composite Symbol with GS1-128 linearcomponent
- DBAR_OMN_CC # GS1 Composite Symbol with GS1 DataBarOmnidirectional linear component
- DBAR_LTD_CC # GS1 Composite Symbol with GS1 DataBarLimited linear component
- DBAR_EXP_CC # GS1 Composite Symbol with GS1 DataBarExpanded linear component
- UPCA_CC # GS1 Composite Symbol with UPC-A linear component
- UPCE_CC # GS1 Composite Symbol with UPC-E linear
- DBAR_STK_CC # GS1 Composite Symbol with GS1 DataBar Stacked component
- DBAR_OMNSTK_CC # GS1 Composite Symbol with GS1 DataBar Stacked Omnidirectional component
- DBAR_EXPSTK_CC # GS1 Composite Symbol with GS1 DataBar Expanded Stacked component
- CHANNEL # Channel Code
- CODEONE # Code One
- GRIDMATRIX # Grid Matrix
- UPNQR # UPNQR (Univerzalnega Plačilnega Naloga QR)
- ULTRA # Ultracode
- RMQR # Rectangular Micro QR Code (rMQR)
- BC412 # IBM BC412 (SEMI T1-95)

### 安装相应的环境

#### Linux

    ```
    $ sudo apt install git cmake build-essential libpng-dev
    $ git clone https://git.code.sf.net/p/zint/code zint
    $ mkdir build
    $ cd build
    $ cmake ..
    $ make
    $ sudo make install
    ```

#### MacOS

    ```
    # 安装brew 已安装可以忽略
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    $ brew update
    $ brew install zint
    ```

### 使用说明

#### 安装barcodejun库

- 1
  ```
  pip install barcodejun
  ```
- 2
    ```
    # 进入项目目录
    $ cd $YourProjectPath
    $ pip install git+https://github.com/ElevenTreeHole/barcodejun.git@v1.0.0
    ```
- 3
    ```
    # 克隆代码
    $ git clone git@github.com:ElevenTreeHole/barcodejun.git /path/to/barcodejun
    # 进入项目目录
    $ cd $YourProjectPath
    $ pip install /path/to/barcodejun
    ```


#### 示例

```
from barcodejun import BarcodeData, BarcodeType, BarcodeVers, Barcode

barcode_data = BarcodeData(
    data="[420]77030[94]00136105440331666909",
    barcode=BarcodeType.DATAMATRIX,
    gs1=True,
    vers=BarcodeVers.SIZE_20_20,
    notext=True,
    direct=True
)
barcode_creator = Barcode()
barcode_creator.generate(data=barcode_data)

```
