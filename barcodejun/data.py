from barcodejun.vers import BarcodeVers
from barcodejun.file_type import BarcodeFileType
from typing import Union


class BarcodeData:
    """
    参数说明 请参阅
    https://github.com/zint/zint/blob/master/docs/manual.txt
    """
    """
    BarcodeType Number or name of barcode type. Default is 20 (CODE128)
    """
    barcode: int = None
    b: int = None

    """
    Set add-on gap in multiples of X-dimension for EAN/UPC
    """
    addongap: int = None

    """
    Treat each line of an input file specified with i | input as a separate
    data set and produce a barcode image for each one. The barcode images are
    outputted by default to numbered filenames starting with “00001.png”,
    “00002.png” etc., which can be changed by using the -o | output option.
    """
    batch: bool = False

    """
    Specify a background (paper) colour where COLOUR is in hexadecimal RRGGBB or
    RRGGBBAA format or in decimal C,M,Y,K percentages format.
    """
    bg: str = None

    """
    Treat input data as raw 8-bit binary data instead of the default UTF-8.
    Automatic code page translation to an ECI page is disabled, and no
    validation of the data’s character encoding takes place.
    """
    binary: str = None

    """
    Add horizontal boundary bars (also known as bearer bars) to the symbol. The
    width of the boundary bars is specified by the `border` option. `bind` can
    also be used to add row separator bars to symbols stacked with multiple `d` |
    `data` inputs, in which case the width of the separator bars is specified
    with the `separator` option.
    """
    bind: bool = False

    """
    Add a horizontal boundary bar to the top of the symbol. The width of the
    boundary bar is specified by the `border` option.
    """
    bindtop: bool = False

    """
    Use bold text for the Human Readable Text (HRT).
    """
    bold: bool = False

    """ 
    Set the width of boundary bars (`bind` or `bindtop`) or box borders (`box`),
    where INTEGER is in integral multiples of the X-dimension. The default is
    zero.
    """
    border: int = None

    """
    Add a box around the symbol. The width of the borders is specified by the
    `border` option.
    """
    box: bool = False

    """
    Use the CMYK colour space when outputting to Encapsulated PostScript (EPS)
    or TIF files.
    """
    cmyk: bool = False

    """
    Set the number of data columns in the symbol to INTEGER. Affects
    Codablock-F, DotCode, GS1 DataBar Expanded Stacked (DBAR_EXPSTK),
    MicroPDF417 and PDF417 symbols.
    """
    cols: int = None

    """
    Warn if the height specified by the `height` option is not compliant with
    the barcode’s specification, or if `height` is not given, default to the
    height specified by the specification (if any).
    """
    compliant_height: bool = False

    """
    Specify the input DATA to encode. The `esc` option may be used to enter
    non-printing characters using escape sequences. The DATA should be UTF-8,
    unless the `binary` option is given, in which case it can be anything.
    """
    data: str = None
    d: str = None

    """
    Send output to stdout, which in most cases should be re-directed to a pipe
    or a file. Use `filetype` to specify output format."""
    direct: bool = False

    """
    For Data Matrix symbols, allow Data Matrix Rectangular Extended (DMRE) sizes
    when considering automatic sizes.
    """
    dmre: bool = False

    """
    Set the radius of the dots in dotty mode (`dotty`). NUMBER is in
    X-dimensions, and may be floating-point. The default is 0.8.
    """
    dotsize: Union[float, int] = None

    """
    Use dots instead of squares for matrix symbols. DotCode is always in dotty
    mode.
    """
    dotty: bool = False

    """
    Dump a hexadecimal representation of the symbol’s encodation to stdout. The
    same representation may be outputted to a file by using a .txt extension
    with `o` | `output` or by specifying `filetype`=txt.
    """
    dump: bool = False

    """
    Display the table of ECIs (Extended Channel Interpretations).
    """
    e: bool = False
    ecinos: bool = False

    """
    Set the ECI code for the input data to INTEGER. See -e | --ecinos for a list
    of the ECIs available. ECIs are supported by Aztec Code, Code One, Data
    Matrix, DotCode, Grid Matrix, Han Xin Code, MaxiCode, MicroPDF417, PDF417,
    QR Code, rMQR and Ultracode.
    """
    eci: int = None

    """
    For vector output, embed the font in the file for portability. Currently
    only available for SVG output.
    """
    embedfont: bool = False

    r"""
    Process escape characters in the input data. The escape sequences are:
        \0       (0x00)    NUL  Null character
        \E       (0x04)    EOT  End of Transmission
        \a       (0x07)    BEL  Bell
        \b       (0x08)    BS   Backspace
        \t       (0x09)    HT   Horizontal Tab
        \n       (0x0A)    LF   Line Feed
        \v       (0x0B)    VT   Vertical Tab
        \f       (0x0C)    FF   Form Feed
        \r       (0x0D)    CR   Carriage Return
        \e       (0x1B)    ESC  Escape
        \G       (0x1D)    GS   Group Separator
        \R       (0x1E)    RS   Record Separator
        \\       (0x5C)    \    Backslash
        \dNNN    (NNN)          Any 8-bit character where NNN is
                                decimal (000-255)
        \oNNN    (0oNNN)        Any 8-bit character where NNN is
                                octal (000-377)
        \xNN     (0xNN)         Any 8-bit character where NN is
                                hexadecimal (00-FF)
        \uNNNN   (U+NNNN)       Any 16-bit Unicode BMP character
                                where NNNN is hexadecimal
        \UNNNNNN (U+NNNNNN)     Any 21-bit Unicode character where NNNNNN is hexadecimal
    """
    esc: bool = False

    r"""
    Process the special escape sequences \^A, \^B and \^C that allow manual
    switching of Code Sets (Code 128 only). The sequence \^^ can be used to
    encode data that contains special escape sequences.
    """
    extraesc: bool = False

    """
    Use faster if less optimal encodation or other shortcuts (affects Data
    Matrix, MicroPDF417, PDF417, QRCODE & UPNQR only).
    """
    fast: bool = False

    """
    Specify a foreground (ink) colour where COLOUR is in hexadecimal RRGGBB or
    RRGGBBAA format or in decimal C,M,Y,K percentages format.
    """
    fg: str = None

    """
    Set the output file type to TYPE, which is one of BMP, EMF, EPS, GIF, PCX,
    PNG, SVG, TIF, TXT.
    see `BarcodeFileType`
    """
    filetype: str = None

    """
    Use the multibyte modes of Grid Matrix, Han Xin and QR Code for non-ASCII
    data.
    """
    fullmultibyte: bool = False

    """
    reat input as GS1 compatible data. Application Identifiers (AIs) should be
    placed in square brackets "[]" (but see `gs1parens`).
    """
    gs1: bool = False

    """
    Do not check the validity of GS1 data.
    """
    gs1nocheck: bool = False

    """
    Process parentheses "()" as GS1 AI delimiters, rather than square brackets
    "[]". The input data must not otherwise contain parentheses.
    """
    gs1parens: bool = False

    """
    For Data Matrix in GS1 mode, use GS (0x1D) as the GS1 data separator instead
    of FNC1.
    """
    gssep: bool = False

    """
    For EAN/UPC symbols, set the height the guard bars descend below the main
    bars, where NUMBER is in X-dimensions. NUMBER may be floating-point.
    """
    guarddescent: Union[int, float] = None

    """
    For EAN/UPC symbols, add quiet zone indicators "<" and/or ">" to HRT where
    applicable.
    """
    guardwhitespace: bool = False

    """
    Set the height of the symbol in X-dimensions. NUMBER may be floating-point.
    """
    height: Union[int, float] = None

    """
    Treat height as per-row. Affects Codablock-F, Code 16K, Code 49, GS1 DataBar
    Expanded Stacked (DBAR_EXPSTK), MicroPDF417 and PDF417.
    """
    heightperrow: bool = False

    """
    Read the input data from FILE. Specify a single hyphen (-) for FILE to read
    from stdin.
    """
    i: str = None
    input: str = None

    """
    Create a Reader Initialisation (Programming) symbol.
    """
    init: bool = False

    """
    Set the masking pattern to use for DotCode, Han Xin or QR Code to INTEGER,
    overriding the automatic selection.
    """
    mask: int = None

    """
    Use the batch data to determine the filename in batch mode (`batch`). The `o`
    | `output` option can be used to specify an output directory (any filename
    will be ignored).
    """
    mirror: bool = False

    """
    For MaxiCode and GS1 Composite symbols, set the encoding mode to INTEGER.
    For MaxiCode (SCM is Structured Carrier Message, with 3 fields: postcode,
    3-digit ISO 3166-1 country code, 3-digit service code):
        2   SCM with 9-digit numeric postcode
        3   SCM with 6-character alphanumeric postcode
        4   Enhanced ECC for the primary part of the message
        5   Enhanced ECC for all of the message
        6   Reader Initialisation (Programming)
    For GS1 Composite symbols (names end in _CC, i.e. EANX_CC, GS1_128_CC,
    DBAR_OMN_CC etc.):
        1   CC-A
        2   CC-B
        3   CC-C (GS1_128_CC only)
    """
    mode: int = None

    """
    Remove the background colour (EMF, EPS, GIF, PNG, SVG and TIF only).
    """
    nobackground: bool = False

    """
    Disable any quiet zones for symbols that define them by default.
    """
    noquietzones: bool = False

    """
    Remove the Human Readable Text (HRT).
    """
    notext: bool = False

    """
     Send the output to FILE. When not in batch mode, the default is “out.png”
    (or “out.gif” if zint built without PNG support). When in batch mode
    (`batch`), special characters can be used to format the output filenames:
        ~           Insert a number or 0
        #           Insert a number or space
        @           Insert a number or * (+ on Windows)
        Any other   Insert literally
    """
    o: str = None
    output: str = None

    """
    For MaxiCode, set the content of the primary message. For GS1 Composite
    symbols, set the content of the linear symbol.
    """
    primary: str = None

    """
    Add compliant quiet zones for symbols that specify them. This is in addition
    to any whitespace specified by -w | --whitesp or --vwhitesp.
    """
    quietzones: bool = False

    """
    Reverse the foreground and background colours (white on black). Known as
    “reflectance reversal” or “reversed reflectance”.
    """
    r: bool = False
    reverse: bool = False

    """
    Rotate the symbol by INTEGER degrees, where INTEGER can be 0, 90, 270 or
    360.
    """
    rotate: int = None

    """
    Set the number of rows for Codablock-F or PDF417 to INTEGER. It will also
    set the minimum number of rows for Code 16K or Code 49, and the maximum
    number of rows for GS1 DataBar Expanded Stacked (DBAR_EXPSTK).
    """
    rows: int = None

    """
    Adjust the size of the X-dimension. NUMBER may be floating-point, and is
    multiplied by 2 (except for MaxiCode) before being applied. The default
    scale is 1.
    For MaxiCode, the scale is multiplied by 10 for raster output, by 40 for EMF
    output, and by 2 otherwise.
    Increments of 0.5 (half-integers) are recommended for non-MaxiCode raster
    output (BMP, GIF, PCX, PNG and TIF).
    See also `scalexdimdp` below.
    """
    scale: int = None

    """
    Scale the image according to X-dimension X and resolution R, where X is in
    mm and R is in dpmm (dots per mm). X and R may be floating-point. R is
    optional and defaults to 12 dpmm (approximately 300 dpi).
    The scaling takes into account the output filetype, and deals with all the
    details mentioned above. Units may be specified for X by appending “in”
    (inch) or “mm”, and for R by appending “dpi” (dots per inch) or “dpmm” -
    e.g. `scalexdimdp`="0.013in,300dpi".
    """
    scalexdimdp: str = None

    r"""
    For MaxiCode, prefix the Structured Carrier Message (SCM) with
    "[)>\R01\Gvv", where vv is a 2-digit INTEGER.
    """
    scmvv: int = None

    """
    Set the error correction level (ECC) to INTEGER. The meaning is specific to
    the following matrix symbols (all except PDF417 are approximate):
        Aztec Code  1 to 4 (10%, 23%, 36%, 50%)
        Grid Matrix 1 to 5 (10% to 50%)
        Han Xin     1 to 4 (8%, 15%, 23%, 30%)
        Micro QR    1 to 3 (7%, 15%, 25%) (L, M, Q)
        PDF417      0 to 8 (2^(INTEGER + 1) codewords)
        QR Code     1 to 4 (7%, 15%, 25%, 30%) (L, M, Q, H)
        rMQR        2 or 4 (15% or 30%) (M or H)
        Ultracode   1 to 6 (0%, 5%, 9%, 17%, 25%, 33%)
    """
    secure: int = None

    """
    Set the ECI & DATA content for segment N, where N is 1 to 9. `d` | `data`
    must still be given, and counts as segment 0, its ECI given by `eci`.
    Segments must be consecutive.
    """
    segN: str = None

    """
    Set the height of row separator bars for stacked symbologies, where INTEGER
    is in integral multiples of the X-dimension. The default is zero.
    """
    separator: int = None

    """
    Use small text for Human Readable Text (HRT).
    """
    small: bool = False

    """
    For Data Matrix symbols, exclude rectangular sizes when considering
    automatic sizes.
    """
    square: bool = False

    """
    Set Structured Append info, where I is the 1-based index, C is the total
    number of symbols in the sequence, and ID, which is optional, is the
    identifier that all symbols in the sequence share. Structured Append is
    supported by Aztec Code, Code One, Data Matrix, DotCode, Grid Matrix,
    MaxiCode, MicroPDF417, PDF417, QR Code and Ultracode.
    """
    structapp: str = None

    """
    Display the table of barcode types (symbologies). The numbers or names can
    be used with `b` | `barcode`.
    """
    t: bool = False
    types: bool = False

    """
    Adjust the gap between the barcode and the Human Readable Text (HRT). NUMBER
    is in X-dimensions, and may be floating-point. Maximum is 10; zero results
    in the default 1X being used.
    """
    textgap: Union[int, float] = None

    """
    See `BarcodeVers`
    Set the symbol version (size, check digits, other options) to INTEGER. The
    meaning is symbol-specific.
    For most matrix symbols, it specifies size:
        Aztec Code      1 to 36 (1 to 4 compact)
        Code One        1 to 10
        Data Matrix     1 to 48 (31 to 48 DMRE)
        Grid Matrix     1 to 13
        Han Xin         1 to 84
        Micro QR        1 to 4  (M1, M2, M3, M4)
        QR Code         1 to 40
        rMQR            1 to 38 (33 to 38 automatic width)
    For a number of linear symbols, it specifies check character options (“hide”
    or “hidden” means don’t show in HRT, “visible” means do display in HRT):
        C25IATA         1 or 2 (add visible or hidden check digit)
        C25IND          ditto
        C25INTER        ditto
        C25LOGIC        ditto
        C25STANDARD     ditto
        Codabar         1 or 2 (add hidden or visible check digit)
        Code 11         0 to 2 (2 visible check digits to none)
                        0      (default 2 visible check digits)
                        1      (1 visible check digit)
                        2      (no check digits)
        Code 39         1 or 2 (add visible or hidden check digit)
        Code 93         1      (hide the default check characters)
        EXCODE39        1 or 2 (add visible or hidden check digit)
        LOGMARS         1 or 2 (add visible or hidden check digit)
        MSI Plessey     0 to 6 (none to various visible options)
                        1, 2   (mod-10, mod-10 + mod-10)
                        3, 4   (mod-11 IBM, mod-11 IBM + mod-10)
                        5, 6   (mod-11 NCR, mod-11 NCR + mod-10)
                        +10    (hide)
    For a few other symbologies, it specifies other characteristics:

        Channel Code    3 to 8    (no. of channels)
        DAFT            50 to 900 (permille tracker ratio)
        DPD             1         (relabel)
        PZN             1         (PZN7 instead of default PZN8)
        Ultracode       2         (revision 2)
        VIN             1         (add international prefix)
    """
    vers: int = None

    """
    Set the height of vertical whitespace above and below the barcode, where
    INTEGER is in integral multiples of the X-dimension.
    """
    w: int = None
    vwhitesp: int = None

    """
    Convert all warnings into errors.
    """
    werror: bool = False

    __field_short_map = {
        "d": "data",
        "o": "output",
        "i": "input",
        "b": "barcode",
        "w": "whitesp",
        "e": "ecinos",
        "r": "reverse",
        "t": "types",
    }
    __local_kwargs = dict()

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def __filter_fields(self, input_params: dict):
        """
        参数缩写和飞缩写同时存在优先取缩写
        :param input_params:
        :return:
        """
        input_fields = input_params.keys()
        for k, v in input_params.items():
            if k in input_fields and v in input_fields:
                input_params.pop(v)
        return input_params

    def build_params(self):
        kwargs = self.__local_kwargs
        input_fields = self.__filter_fields(kwargs)
        params = []
        for attr in input_fields.keys():
            print(attr, "=+++++++++++", input_fields)
            if attr in input_fields:
                value = getattr(self, attr)
                if attr in self.__field_short_map.keys():
                    print("233333")
                    params += ["-%s" % attr, "%s" % str(input_fields.get(attr))]
                    pass
                else:
                    print(44444)
                    if type(value) in (str, int, float) and input_fields.get(attr) is not None:
                        params += ["--%s=\"%s\"" % (attr, str(input_fields.get(attr)))]
                    elif type(value) in (bool,) and input_fields.get(attr):
                        params += ["--%s" % attr]
                        pass
        return params

    pass
