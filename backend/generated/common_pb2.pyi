from google.protobuf import any_pb2 as _any_pb2
import common_enums_pb2 as _common_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseError(_message.Message):
    __slots__ = ("ErrorCode", "ErrorName", "ErrorMessage", "ErrorArguments")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORNAME_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    ERRORARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    ErrorCode: str
    ErrorName: str
    ErrorMessage: str
    ErrorArguments: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, ErrorCode: _Optional[str] = ..., ErrorName: _Optional[str] = ..., ErrorMessage: _Optional[str] = ..., ErrorArguments: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class ResponseWarning(_message.Message):
    __slots__ = ("WarningCode", "WarningName", "WarningMessage", "WarningArguments")
    WARNINGCODE_FIELD_NUMBER: _ClassVar[int]
    WARNINGNAME_FIELD_NUMBER: _ClassVar[int]
    WARNINGMESSAGE_FIELD_NUMBER: _ClassVar[int]
    WARNINGARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    WarningCode: str
    WarningName: str
    WarningMessage: str
    WarningArguments: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, WarningCode: _Optional[str] = ..., WarningName: _Optional[str] = ..., WarningMessage: _Optional[str] = ..., WarningArguments: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class ResponseMessage(_message.Message):
    __slots__ = ("MessageCode", "MessageName", "Message")
    MESSAGECODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGENAME_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    MessageCode: str
    MessageName: str
    Message: str
    def __init__(self, MessageCode: _Optional[str] = ..., MessageName: _Optional[str] = ..., Message: _Optional[str] = ...) -> None: ...

class MOVEShockInput(_message.Message):
    __slots__ = ("IndexChangePercent", "ProductCodes")
    INDEXCHANGEPERCENT_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODES_FIELD_NUMBER: _ClassVar[int]
    IndexChangePercent: float
    ProductCodes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, IndexChangePercent: _Optional[float] = ..., ProductCodes: _Optional[_Iterable[str]] = ...) -> None: ...

class MOVECreditSpreadShockInput(_message.Message):
    __slots__ = ("TreasuryBPS", "CorporateDebtBPS", "ProductCodes", "IndexChangePercent")
    TREASURYBPS_FIELD_NUMBER: _ClassVar[int]
    CORPORATEDEBTBPS_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODES_FIELD_NUMBER: _ClassVar[int]
    INDEXCHANGEPERCENT_FIELD_NUMBER: _ClassVar[int]
    TreasuryBPS: float
    CorporateDebtBPS: float
    ProductCodes: _containers.RepeatedScalarFieldContainer[str]
    IndexChangePercent: float
    def __init__(self, TreasuryBPS: _Optional[float] = ..., CorporateDebtBPS: _Optional[float] = ..., ProductCodes: _Optional[_Iterable[str]] = ..., IndexChangePercent: _Optional[float] = ...) -> None: ...

class YieldShockInput(_message.Message):
    __slots__ = ("InterestRateChangeBPS", "IVPercentDown", "IVPercentUp", "MaturityTerm", "ProductCodes")
    INTERESTRATECHANGEBPS_FIELD_NUMBER: _ClassVar[int]
    IVPERCENTDOWN_FIELD_NUMBER: _ClassVar[int]
    IVPERCENTUP_FIELD_NUMBER: _ClassVar[int]
    MATURITYTERM_FIELD_NUMBER: _ClassVar[int]
    PRODUCTCODES_FIELD_NUMBER: _ClassVar[int]
    InterestRateChangeBPS: float
    IVPercentDown: float
    IVPercentUp: float
    MaturityTerm: _common_enums_pb2.EnumMaturityTerm
    ProductCodes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, InterestRateChangeBPS: _Optional[float] = ..., IVPercentDown: _Optional[float] = ..., IVPercentUp: _Optional[float] = ..., MaturityTerm: _Optional[_Union[_common_enums_pb2.EnumMaturityTerm, str]] = ..., ProductCodes: _Optional[_Iterable[str]] = ...) -> None: ...
