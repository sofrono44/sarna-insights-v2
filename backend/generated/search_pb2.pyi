import common_pb2 as _common_pb2
import accounts_pb2 as _accounts_pb2
import common_pb2 as _common_pb2_1
import orders_pb2 as _orders_pb2
import positions_pb2 as _positions_pb2
import search_enums_pb2 as _search_enums_pb2
import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchRequest(_message.Message):
    __slots__ = ("Type", "SearchCriteria")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    Type: _search_enums_pb2.EnumSearchType
    SearchCriteria: SearchCriteria
    def __init__(self, Type: _Optional[_Union[_search_enums_pb2.EnumSearchType, str]] = ..., SearchCriteria: _Optional[_Union[SearchCriteria, _Mapping]] = ...) -> None: ...

class SearchCriteria(_message.Message):
    __slots__ = ("Filter", "FieldSortOrder", "Page")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    FIELDSORTORDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    Filter: FilterGroup
    FieldSortOrder: _containers.RepeatedCompositeFieldContainer[FieldSortOrder]
    Page: PageRequest
    def __init__(self, Filter: _Optional[_Union[FilterGroup, _Mapping]] = ..., FieldSortOrder: _Optional[_Iterable[_Union[FieldSortOrder, _Mapping]]] = ..., Page: _Optional[_Union[PageRequest, _Mapping]] = ...) -> None: ...

class PageRequest(_message.Message):
    __slots__ = ("PageRequestId", "Page", "PageSize")
    PAGEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    PageRequestId: str
    Page: int
    PageSize: int
    def __init__(self, PageRequestId: _Optional[str] = ..., Page: _Optional[int] = ..., PageSize: _Optional[int] = ...) -> None: ...

class Filter(_message.Message):
    __slots__ = ("FilterGroup", "FieldFilter")
    FILTERGROUP_FIELD_NUMBER: _ClassVar[int]
    FIELDFILTER_FIELD_NUMBER: _ClassVar[int]
    FilterGroup: FilterGroup
    FieldFilter: FieldFilter
    def __init__(self, FilterGroup: _Optional[_Union[FilterGroup, _Mapping]] = ..., FieldFilter: _Optional[_Union[FieldFilter, _Mapping]] = ...) -> None: ...

class FieldFilter(_message.Message):
    __slots__ = ("Field", "Operator", "Values")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    Field: _search_enums_pb2.EnumField
    Operator: _search_enums_pb2.EnumOperator
    Values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, Field: _Optional[_Union[_search_enums_pb2.EnumField, str]] = ..., Operator: _Optional[_Union[_search_enums_pb2.EnumOperator, str]] = ..., Values: _Optional[_Iterable[str]] = ...) -> None: ...

class FilterGroup(_message.Message):
    __slots__ = ("Filters", "JoinOperator")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    JOINOPERATOR_FIELD_NUMBER: _ClassVar[int]
    Filters: _containers.RepeatedCompositeFieldContainer[Filter]
    JoinOperator: _search_enums_pb2.EnumJoinOperator
    def __init__(self, Filters: _Optional[_Iterable[_Union[Filter, _Mapping]]] = ..., JoinOperator: _Optional[_Union[_search_enums_pb2.EnumJoinOperator, str]] = ...) -> None: ...

class FieldSortOrder(_message.Message):
    __slots__ = ("Field", "SortDirection")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    SORTDIRECTION_FIELD_NUMBER: _ClassVar[int]
    Field: _search_enums_pb2.EnumField
    SortDirection: _search_enums_pb2.EnumSortDirection
    def __init__(self, Field: _Optional[_Union[_search_enums_pb2.EnumField, str]] = ..., SortDirection: _Optional[_Union[_search_enums_pb2.EnumSortDirection, str]] = ...) -> None: ...

class SearchServiceResponse(_message.Message):
    __slots__ = ("Result", "Orders", "Accounts", "OpenPositionLots", "Users", "AdditionalFieldValues", "OpenOrders", "FilledOrders", "CancelledOrders", "OpenOrdersTotal", "FilledOrdersTotal", "CancelledOrdersTotal", "Warnings", "Errors", "SearchCriteria", "Page")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    OPENPOSITIONLOTS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALFIELDVALUES_FIELD_NUMBER: _ClassVar[int]
    OPENORDERS_FIELD_NUMBER: _ClassVar[int]
    FILLEDORDERS_FIELD_NUMBER: _ClassVar[int]
    CANCELLEDORDERS_FIELD_NUMBER: _ClassVar[int]
    OPENORDERSTOTAL_FIELD_NUMBER: _ClassVar[int]
    FILLEDORDERSTOTAL_FIELD_NUMBER: _ClassVar[int]
    CANCELLEDORDERSTOTAL_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    Result: _search_enums_pb2.EnumSearchServiceResponse
    Orders: _containers.RepeatedCompositeFieldContainer[SearchServiceOrderInfo]
    Accounts: _containers.RepeatedCompositeFieldContainer[_accounts_pb2.Account]
    OpenPositionLots: _containers.RepeatedCompositeFieldContainer[_positions_pb2.OpenPositionLot]
    Users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    AdditionalFieldValues: _containers.RepeatedCompositeFieldContainer[AdditionalFieldValue]
    OpenOrders: int
    FilledOrders: int
    CancelledOrders: int
    OpenOrdersTotal: int
    FilledOrdersTotal: int
    CancelledOrdersTotal: int
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    SearchCriteria: SearchCriteria
    Page: PageResponse
    def __init__(self, Result: _Optional[_Union[_search_enums_pb2.EnumSearchServiceResponse, str]] = ..., Orders: _Optional[_Iterable[_Union[SearchServiceOrderInfo, _Mapping]]] = ..., Accounts: _Optional[_Iterable[_Union[_accounts_pb2.Account, _Mapping]]] = ..., OpenPositionLots: _Optional[_Iterable[_Union[_positions_pb2.OpenPositionLot, _Mapping]]] = ..., Users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., AdditionalFieldValues: _Optional[_Iterable[_Union[AdditionalFieldValue, _Mapping]]] = ..., OpenOrders: _Optional[int] = ..., FilledOrders: _Optional[int] = ..., CancelledOrders: _Optional[int] = ..., OpenOrdersTotal: _Optional[int] = ..., FilledOrdersTotal: _Optional[int] = ..., CancelledOrdersTotal: _Optional[int] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ..., SearchCriteria: _Optional[_Union[SearchCriteria, _Mapping]] = ..., Page: _Optional[_Union[PageResponse, _Mapping]] = ...) -> None: ...

class PageResponse(_message.Message):
    __slots__ = ("PageRequestId", "Page", "PageSize", "TotalCount")
    PAGEREQUESTID_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    TOTALCOUNT_FIELD_NUMBER: _ClassVar[int]
    PageRequestId: str
    Page: int
    PageSize: int
    TotalCount: int
    def __init__(self, PageRequestId: _Optional[str] = ..., Page: _Optional[int] = ..., PageSize: _Optional[int] = ..., TotalCount: _Optional[int] = ...) -> None: ...

class AdditionalFieldValue(_message.Message):
    __slots__ = ("FieldValuePairs",)
    FIELDVALUEPAIRS_FIELD_NUMBER: _ClassVar[int]
    FieldValuePairs: _containers.RepeatedCompositeFieldContainer[FieldValuePair]
    def __init__(self, FieldValuePairs: _Optional[_Iterable[_Union[FieldValuePair, _Mapping]]] = ...) -> None: ...

class FieldValuePair(_message.Message):
    __slots__ = ("Key", "Value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Key: _search_enums_pb2.EnumField
    Value: str
    def __init__(self, Key: _Optional[_Union[_search_enums_pb2.EnumField, str]] = ..., Value: _Optional[str] = ...) -> None: ...

class SearchServiceOrderInfo(_message.Message):
    __slots__ = ("Order", "AllowedActions")
    ORDER_FIELD_NUMBER: _ClassVar[int]
    ALLOWEDACTIONS_FIELD_NUMBER: _ClassVar[int]
    Order: _orders_pb2.Order
    AllowedActions: _containers.RepeatedScalarFieldContainer[bool]
    def __init__(self, Order: _Optional[_Union[_orders_pb2.Order, _Mapping]] = ..., AllowedActions: _Optional[_Iterable[bool]] = ...) -> None: ...

class SearchServiceDefinitionResponse(_message.Message):
    __slots__ = ("SearchTypeDefinitions", "Warnings", "Errors")
    SEARCHTYPEDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SearchTypeDefinitions: _containers.RepeatedCompositeFieldContainer[SearchTypeDefinition]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2_1.ResponseError]
    def __init__(self, SearchTypeDefinitions: _Optional[_Iterable[_Union[SearchTypeDefinition, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2_1.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2_1.ResponseError, _Mapping]]] = ...) -> None: ...

class SearchTypeDefinition(_message.Message):
    __slots__ = ("Group", "FieldDefinitions")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    FIELDDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    Group: str
    FieldDefinitions: _containers.RepeatedCompositeFieldContainer[FieldDefinition]
    def __init__(self, Group: _Optional[str] = ..., FieldDefinitions: _Optional[_Iterable[_Union[FieldDefinition, _Mapping]]] = ...) -> None: ...

class FieldDefinition(_message.Message):
    __slots__ = ("Field", "FieldType", "FieldOptions")
    FIELD_FIELD_NUMBER: _ClassVar[int]
    FIELDTYPE_FIELD_NUMBER: _ClassVar[int]
    FIELDOPTIONS_FIELD_NUMBER: _ClassVar[int]
    Field: _search_enums_pb2.EnumField
    FieldType: _search_enums_pb2.EnumFieldType
    FieldOptions: _containers.RepeatedCompositeFieldContainer[FieldOption]
    def __init__(self, Field: _Optional[_Union[_search_enums_pb2.EnumField, str]] = ..., FieldType: _Optional[_Union[_search_enums_pb2.EnumFieldType, str]] = ..., FieldOptions: _Optional[_Iterable[_Union[FieldOption, _Mapping]]] = ...) -> None: ...

class FieldOption(_message.Message):
    __slots__ = ("Label", "Value")
    LABEL_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Label: str
    Value: str
    def __init__(self, Label: _Optional[str] = ..., Value: _Optional[str] = ...) -> None: ...

class SearchPerson(_message.Message):
    __slots__ = ("Name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    Name: str
    def __init__(self, Name: _Optional[str] = ...) -> None: ...
