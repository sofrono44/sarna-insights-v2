import common_pb2 as _common_pb2
import search_pb2 as _search_pb2
import search_enums_pb2 as _search_enums_pb2
from admin import admin_reports_enums_pb2 as _admin_reports_enums_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReportSearchRequest(_message.Message):
    __slots__ = ("ReportType", "ReportLevel", "From", "To", "AccountNumbers", "AccountGroupIds", "Page")
    REPORTTYPE_FIELD_NUMBER: _ClassVar[int]
    REPORTLEVEL_FIELD_NUMBER: _ClassVar[int]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPIDS_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ReportType: _admin_reports_enums_pb2.EnumReportType
    ReportLevel: _admin_reports_enums_pb2.EnumReportLevel
    From: _timestamp_pb2.Timestamp
    To: _timestamp_pb2.Timestamp
    AccountNumbers: _containers.RepeatedScalarFieldContainer[str]
    AccountGroupIds: _containers.RepeatedScalarFieldContainer[int]
    Page: _search_pb2.PageRequest
    def __init__(self, ReportType: _Optional[_Union[_admin_reports_enums_pb2.EnumReportType, str]] = ..., ReportLevel: _Optional[_Union[_admin_reports_enums_pb2.EnumReportLevel, str]] = ..., From: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., To: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., AccountNumbers: _Optional[_Iterable[str]] = ..., AccountGroupIds: _Optional[_Iterable[int]] = ..., Page: _Optional[_Union[_search_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ReportsResponse(_message.Message):
    __slots__ = ("Reports", "ReportDefinitions", "Warnings", "Errors", "SearchRequest", "Page")
    REPORTS_FIELD_NUMBER: _ClassVar[int]
    REPORTDEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SEARCHREQUEST_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    Reports: _containers.RepeatedCompositeFieldContainer[Report]
    ReportDefinitions: _containers.RepeatedCompositeFieldContainer[ReportDefinition]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    SearchRequest: ReportSearchRequest
    Page: _search_pb2.PageResponse
    def __init__(self, Reports: _Optional[_Iterable[_Union[Report, _Mapping]]] = ..., ReportDefinitions: _Optional[_Iterable[_Union[ReportDefinition, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ..., SearchRequest: _Optional[_Union[ReportSearchRequest, _Mapping]] = ..., Page: _Optional[_Union[_search_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class Report(_message.Message):
    __slots__ = ("ReportId", "ReportDefinitionId", "Date", "AccountNumber", "AccountGroupId")
    REPORTID_FIELD_NUMBER: _ClassVar[int]
    REPORTDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    ReportId: int
    ReportDefinitionId: int
    Date: _timestamp_pb2.Timestamp
    AccountNumber: str
    AccountGroupId: int
    def __init__(self, ReportId: _Optional[int] = ..., ReportDefinitionId: _Optional[int] = ..., Date: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., AccountNumber: _Optional[str] = ..., AccountGroupId: _Optional[int] = ...) -> None: ...

class ReportDefinition(_message.Message):
    __slots__ = ("ReportDefinitionId", "ReportType", "ReportLevel", "Name", "ReportVariants", "AccountGroupId")
    REPORTDEFINITIONID_FIELD_NUMBER: _ClassVar[int]
    REPORTTYPE_FIELD_NUMBER: _ClassVar[int]
    REPORTLEVEL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REPORTVARIANTS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTGROUPID_FIELD_NUMBER: _ClassVar[int]
    ReportDefinitionId: int
    ReportType: _admin_reports_enums_pb2.EnumReportType
    ReportLevel: _admin_reports_enums_pb2.EnumReportLevel
    Name: str
    ReportVariants: _containers.RepeatedCompositeFieldContainer[ReportVariant]
    AccountGroupId: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ReportDefinitionId: _Optional[int] = ..., ReportType: _Optional[_Union[_admin_reports_enums_pb2.EnumReportType, str]] = ..., ReportLevel: _Optional[_Union[_admin_reports_enums_pb2.EnumReportLevel, str]] = ..., Name: _Optional[str] = ..., ReportVariants: _Optional[_Iterable[_Union[ReportVariant, _Mapping]]] = ..., AccountGroupId: _Optional[_Iterable[int]] = ...) -> None: ...

class ReportVariant(_message.Message):
    __slots__ = ("Name", "IsViewAvailable", "AccountNumberColumnIndex", "OutputType")
    NAME_FIELD_NUMBER: _ClassVar[int]
    ISVIEWAVAILABLE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERCOLUMNINDEX_FIELD_NUMBER: _ClassVar[int]
    OUTPUTTYPE_FIELD_NUMBER: _ClassVar[int]
    Name: str
    IsViewAvailable: bool
    AccountNumberColumnIndex: int
    OutputType: _admin_reports_enums_pb2.EnumReportOutputType
    def __init__(self, Name: _Optional[str] = ..., IsViewAvailable: bool = ..., AccountNumberColumnIndex: _Optional[int] = ..., OutputType: _Optional[_Union[_admin_reports_enums_pb2.EnumReportOutputType, str]] = ...) -> None: ...

class ReportsDownloadRequest(_message.Message):
    __slots__ = ("ReportIds",)
    REPORTIDS_FIELD_NUMBER: _ClassVar[int]
    ReportIds: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ReportIds: _Optional[_Iterable[int]] = ...) -> None: ...

class ReportsDownloadResponse(_message.Message):
    __slots__ = ("ReportDownloads",)
    REPORTDOWNLOADS_FIELD_NUMBER: _ClassVar[int]
    ReportDownloads: _containers.RepeatedCompositeFieldContainer[ReportsDownloadData]
    def __init__(self, ReportDownloads: _Optional[_Iterable[_Union[ReportsDownloadData, _Mapping]]] = ...) -> None: ...

class ReportsDownloadData(_message.Message):
    __slots__ = ("ReportId", "FileName", "FileContent", "Url")
    REPORTID_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    FILECONTENT_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    ReportId: int
    FileName: str
    FileContent: bytes
    Url: str
    def __init__(self, ReportId: _Optional[int] = ..., FileName: _Optional[str] = ..., FileContent: _Optional[bytes] = ..., Url: _Optional[str] = ...) -> None: ...

class ReportRequest(_message.Message):
    __slots__ = ("ReportId",)
    REPORTID_FIELD_NUMBER: _ClassVar[int]
    ReportId: int
    def __init__(self, ReportId: _Optional[int] = ...) -> None: ...

class ReportViewRequest(_message.Message):
    __slots__ = ("ReportId", "SearchCriteria")
    REPORTID_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    ReportId: int
    SearchCriteria: ReportSearchCriteria
    def __init__(self, ReportId: _Optional[int] = ..., SearchCriteria: _Optional[_Union[ReportSearchCriteria, _Mapping]] = ...) -> None: ...

class ReportSearchCriteria(_message.Message):
    __slots__ = ("Filter", "SortOrder", "Page")
    FILTER_FIELD_NUMBER: _ClassVar[int]
    SORTORDER_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    Filter: ReportColumnGroup
    SortOrder: _containers.RepeatedCompositeFieldContainer[ReportColumnSortOrder]
    Page: _search_pb2.PageRequest
    def __init__(self, Filter: _Optional[_Union[ReportColumnGroup, _Mapping]] = ..., SortOrder: _Optional[_Iterable[_Union[ReportColumnSortOrder, _Mapping]]] = ..., Page: _Optional[_Union[_search_pb2.PageRequest, _Mapping]] = ...) -> None: ...

class ReportFilter(_message.Message):
    __slots__ = ("FilterGroup", "FieldFilter")
    FILTERGROUP_FIELD_NUMBER: _ClassVar[int]
    FIELDFILTER_FIELD_NUMBER: _ClassVar[int]
    FilterGroup: ReportColumnGroup
    FieldFilter: ReportColumnFilter
    def __init__(self, FilterGroup: _Optional[_Union[ReportColumnGroup, _Mapping]] = ..., FieldFilter: _Optional[_Union[ReportColumnFilter, _Mapping]] = ...) -> None: ...

class ReportColumnFilter(_message.Message):
    __slots__ = ("ColumnIndex", "Operator", "Values")
    COLUMNINDEX_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ColumnIndex: int
    Operator: _search_enums_pb2.EnumOperator
    Values: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, ColumnIndex: _Optional[int] = ..., Operator: _Optional[_Union[_search_enums_pb2.EnumOperator, str]] = ..., Values: _Optional[_Iterable[str]] = ...) -> None: ...

class ReportColumnGroup(_message.Message):
    __slots__ = ("Filters", "JoinOperator")
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    JOINOPERATOR_FIELD_NUMBER: _ClassVar[int]
    Filters: _containers.RepeatedCompositeFieldContainer[ReportFilter]
    JoinOperator: _search_enums_pb2.EnumJoinOperator
    def __init__(self, Filters: _Optional[_Iterable[_Union[ReportFilter, _Mapping]]] = ..., JoinOperator: _Optional[_Union[_search_enums_pb2.EnumJoinOperator, str]] = ...) -> None: ...

class ReportColumnSortOrder(_message.Message):
    __slots__ = ("ColumnIndex", "SortDirection")
    COLUMNINDEX_FIELD_NUMBER: _ClassVar[int]
    SORTDIRECTION_FIELD_NUMBER: _ClassVar[int]
    ColumnIndex: int
    SortDirection: _search_enums_pb2.EnumSortDirection
    def __init__(self, ColumnIndex: _Optional[int] = ..., SortDirection: _Optional[_Union[_search_enums_pb2.EnumSortDirection, str]] = ...) -> None: ...

class ReportViewResponse(_message.Message):
    __slots__ = ("ReportId", "Report", "AccountNumberColumnIndex", "Headers", "Rows", "Warnings", "Errors", "SearchCriteria", "Page")
    REPORTID_FIELD_NUMBER: _ClassVar[int]
    REPORT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTNUMBERCOLUMNINDEX_FIELD_NUMBER: _ClassVar[int]
    HEADERS_FIELD_NUMBER: _ClassVar[int]
    ROWS_FIELD_NUMBER: _ClassVar[int]
    WARNINGS_FIELD_NUMBER: _ClassVar[int]
    ERRORS_FIELD_NUMBER: _ClassVar[int]
    SEARCHCRITERIA_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    ReportId: int
    Report: Report
    AccountNumberColumnIndex: int
    Headers: _containers.RepeatedScalarFieldContainer[str]
    Rows: _containers.RepeatedCompositeFieldContainer[ReportRow]
    Warnings: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseWarning]
    Errors: _containers.RepeatedCompositeFieldContainer[_common_pb2.ResponseError]
    SearchCriteria: ReportSearchCriteria
    Page: _search_pb2.PageResponse
    def __init__(self, ReportId: _Optional[int] = ..., Report: _Optional[_Union[Report, _Mapping]] = ..., AccountNumberColumnIndex: _Optional[int] = ..., Headers: _Optional[_Iterable[str]] = ..., Rows: _Optional[_Iterable[_Union[ReportRow, _Mapping]]] = ..., Warnings: _Optional[_Iterable[_Union[_common_pb2.ResponseWarning, _Mapping]]] = ..., Errors: _Optional[_Iterable[_Union[_common_pb2.ResponseError, _Mapping]]] = ..., SearchCriteria: _Optional[_Union[ReportSearchCriteria, _Mapping]] = ..., Page: _Optional[_Union[_search_pb2.PageResponse, _Mapping]] = ...) -> None: ...

class ReportRow(_message.Message):
    __slots__ = ("Columns",)
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    Columns: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, Columns: _Optional[_Iterable[str]] = ...) -> None: ...
