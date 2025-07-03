from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_bp_enums_pb2 as _common_bp_enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_bp_enums_pb2 import EnumBpOptionTradingLevel as EnumBpOptionTradingLevel

DESCRIPTOR: _descriptor.FileDescriptor
EnumBpOptionTradingLevel_Undefined: _common_bp_enums_pb2.EnumBpOptionTradingLevel
EnumBpOptionTradingLevel_WritingCoveredCalls: _common_bp_enums_pb2.EnumBpOptionTradingLevel
EnumBpOptionTradingLevel_BuyingCallsAndPuts: _common_bp_enums_pb2.EnumBpOptionTradingLevel
EnumBpOptionTradingLevel_SpreadingCallsAndPuts: _common_bp_enums_pb2.EnumBpOptionTradingLevel
EnumBpOptionTradingLevel_UncoveredPutWriting: _common_bp_enums_pb2.EnumBpOptionTradingLevel
EnumBpOptionTradingLevel_UncoveredCallWriting: _common_bp_enums_pb2.EnumBpOptionTradingLevel
EnumBpOptionTradingLevel_UncoveredIndexWriting: _common_bp_enums_pb2.EnumBpOptionTradingLevel

class AdminSearchAccount(_message.Message):
    __slots__ = ("id", "accountNumber", "tradingLevel", "CreatedTime")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    TRADINGLEVEL_FIELD_NUMBER: _ClassVar[int]
    CREATEDTIME_FIELD_NUMBER: _ClassVar[int]
    id: int
    accountNumber: str
    tradingLevel: _common_bp_enums_pb2.EnumBpOptionTradingLevel
    CreatedTime: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., accountNumber: _Optional[str] = ..., tradingLevel: _Optional[_Union[_common_bp_enums_pb2.EnumBpOptionTradingLevel, str]] = ..., CreatedTime: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
