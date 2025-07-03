from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class EnumReportType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumReportType_Undefined: _ClassVar[EnumReportType]
    EnumReportType_Risk: _ClassVar[EnumReportType]

class EnumReportLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumReportLevel_Undefined: _ClassVar[EnumReportLevel]
    EnumReportLevel_Aggregate: _ClassVar[EnumReportLevel]
    EnumReportLevel_Account: _ClassVar[EnumReportLevel]

class EnumReportOutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EnumReportOutputType_Undefined: _ClassVar[EnumReportOutputType]
    EnumReportOutputType_C_S_V: _ClassVar[EnumReportOutputType]
    EnumReportOutputType_Excel: _ClassVar[EnumReportOutputType]
    EnumReportOutputType_P_D_F: _ClassVar[EnumReportOutputType]
EnumReportType_Undefined: EnumReportType
EnumReportType_Risk: EnumReportType
EnumReportLevel_Undefined: EnumReportLevel
EnumReportLevel_Aggregate: EnumReportLevel
EnumReportLevel_Account: EnumReportLevel
EnumReportOutputType_Undefined: EnumReportOutputType
EnumReportOutputType_C_S_V: EnumReportOutputType
EnumReportOutputType_Excel: EnumReportOutputType
EnumReportOutputType_P_D_F: EnumReportOutputType
