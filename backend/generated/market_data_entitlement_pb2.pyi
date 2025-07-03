import common_pb2 as _common_pb2
import market_data_entitlement_enums_pb2 as _market_data_entitlement_enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
from common_pb2 import ResponseError as ResponseError
from common_pb2 import ResponseWarning as ResponseWarning
from common_pb2 import ResponseMessage as ResponseMessage
from common_pb2 import MOVEShockInput as MOVEShockInput
from common_pb2 import MOVECreditSpreadShockInput as MOVECreditSpreadShockInput
from common_pb2 import YieldShockInput as YieldShockInput

DESCRIPTOR: _descriptor.FileDescriptor

class MarketDataEntitlementFormQuestions(_message.Message):
    __slots__ = ("MarketDataEntitlementFormQuestion", "Warnings", "Errors")
    MARKETDATAENTITLEMENTFORMQUESTION_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MarketDataEntitlementFormQuestion: _containers.RepeatedCompositeFieldContainer[MarketDataEntitlementFormQuestion]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, MarketDataEntitlementFormQuestion: _Optional[_Iterable[_Union[MarketDataEntitlementFormQuestion, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class MarketDataEntitlementFormQuestion(_message.Message):
    __slots__ = ("Key", "Question", "MarketDataEntitlementFormQuestionType")
    KEY_FIELD_NUMBER: _ClassVar[int]
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTFORMQUESTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    Key: str
    Question: str
    MarketDataEntitlementFormQuestionType: _market_data_entitlement_enums_pb2.MarketDataEntitlementFormQuestionType
    def __init__(self, Key: _Optional[str] = ..., Question: _Optional[str] = ..., MarketDataEntitlementFormQuestionType: _Optional[_Union[_market_data_entitlement_enums_pb2.MarketDataEntitlementFormQuestionType, str]] = ...) -> None: ...

class MarketDataEntitlementFormResponsesResponse(_message.Message):
    __slots__ = ("MarketDataEntitlementFormResponses", "Warnings", "Errors")
    MARKETDATAENTITLEMENTFORMRESPONSES_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    MarketDataEntitlementFormResponses: MarketDataEntitlementFormResponses
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    def __init__(self, MarketDataEntitlementFormResponses: _Optional[_Union[MarketDataEntitlementFormResponses, _Mapping]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ...) -> None: ...

class MarketDataEntitlementFormResponses(_message.Message):
    __slots__ = ("RequestedMarketDataEntitlementTypes", "MarketDataEntitlementFormPersonResponses", "MarketDataEntitlementConsentTypes", "MarketDataEntitlementApprovalStatus", "Reason")
    REQUESTEDMARKETDATAENTITLEMENTTYPES_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTFORMPERSONRESPONSES_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTCONSENTTYPES_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTAPPROVALSTATUS_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    RequestedMarketDataEntitlementTypes: _containers.RepeatedScalarFieldContainer[_market_data_entitlement_enums_pb2.EnumMarketDataEntitlementType]
    MarketDataEntitlementFormPersonResponses: _containers.RepeatedCompositeFieldContainer[MarketDataEntitlementFormResponse]
    MarketDataEntitlementConsentTypes: _containers.RepeatedScalarFieldContainer[_market_data_entitlement_enums_pb2.EnumMarketDataEntitlementConsent]
    MarketDataEntitlementApprovalStatus: _market_data_entitlement_enums_pb2.EnumMarketDataEntitlementApprovalStatus
    Reason: str
    def __init__(self, RequestedMarketDataEntitlementTypes: _Optional[_Iterable[_Union[_market_data_entitlement_enums_pb2.EnumMarketDataEntitlementType, str]]] = ..., MarketDataEntitlementFormPersonResponses: _Optional[_Iterable[_Union[MarketDataEntitlementFormResponse, _Mapping]]] = ..., MarketDataEntitlementConsentTypes: _Optional[_Iterable[_Union[_market_data_entitlement_enums_pb2.EnumMarketDataEntitlementConsent, str]]] = ..., MarketDataEntitlementApprovalStatus: _Optional[_Union[_market_data_entitlement_enums_pb2.EnumMarketDataEntitlementApprovalStatus, str]] = ..., Reason: _Optional[str] = ...) -> None: ...

class MarketDataEntitlementFormResponse(_message.Message):
    __slots__ = ("MarketDataEntitlementFormQuestionKey", "Answer", "MarketDataEntitlementFormQuestionType")
    MARKETDATAENTITLEMENTFORMQUESTIONKEY_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    MARKETDATAENTITLEMENTFORMQUESTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    MarketDataEntitlementFormQuestionKey: str
    Answer: str
    MarketDataEntitlementFormQuestionType: _market_data_entitlement_enums_pb2.MarketDataEntitlementFormQuestionType
    def __init__(self, MarketDataEntitlementFormQuestionKey: _Optional[str] = ..., Answer: _Optional[str] = ..., MarketDataEntitlementFormQuestionType: _Optional[_Union[_market_data_entitlement_enums_pb2.MarketDataEntitlementFormQuestionType, str]] = ...) -> None: ...
