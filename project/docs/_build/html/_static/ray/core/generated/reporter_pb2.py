# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/ray/protobuf/reporter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import metrics_pb2 as opencensus_dot_proto_dot_metrics_dot_v1_dot_metrics__pb2
from . import common_pb2 as src_dot_ray_dot_protobuf_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='src/ray/protobuf/reporter.proto',
  package='ray.rpc',
  syntax='proto3',
  serialized_options=b'\370\001\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1fsrc/ray/protobuf/reporter.proto\x12\x07ray.rpc\x1a)opencensus/proto/metrics/v1/metrics.proto\x1a\x1dsrc/ray/protobuf/common.proto\"H\n\x18GetProfilingStatsRequest\x12\x10\n\x03pid\x18\x01 \x01(\rR\x03pid\x12\x1a\n\x08\x64uration\x18\x02 \x01(\x05R\x08\x64uration\"s\n\x16GetProfilingStatsReply\x12\'\n\x0fprofiling_stats\x18\x01 \x01(\tR\x0eprofilingStats\x12\x17\n\x07std_out\x18\x02 \x01(\tR\x06stdOut\x12\x17\n\x07std_err\x18\x03 \x01(\tR\x06stdErr\"S\n\x14ReportMetricsRequest\x12;\n\x0emetrics_points\x18\x01 \x03(\x0b\x32\x14.ray.rpc.MetricPointR\rmetricsPoints\"T\n\x12ReportMetricsReply\x12>\n\x1bmetrcs_description_required\x18\x01 \x01(\x08R\x19metrcsDescriptionRequired\"W\n\x16ReportOCMetricsRequest\x12=\n\x07metrics\x18\x01 \x03(\x0b\x32#.opencensus.proto.metrics.v1.MetricR\x07metrics\"\x16\n\x14ReportOCMetricsReply\"\'\n\x11NodeResourceUsage\x12\x12\n\x04json\x18\x01 \x01(\tR\x04json\"\xa8\x01\n\x10StreamLogRequest\x12\"\n\rlog_file_name\x18\x01 \x01(\tR\x0blogFileName\x12\x1d\n\nkeep_alive\x18\x02 \x01(\x08R\tkeepAlive\x12\x19\n\x05lines\x18\x03 \x01(\x05H\x00R\x05lines\x88\x01\x01\x12\x1f\n\x08interval\x18\x04 \x01(\x02H\x01R\x08interval\x88\x01\x01\x42\x08\n\x06_linesB\x0b\n\t_interval\"$\n\x0eStreamLogReply\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta\"\x11\n\x0fListLogsRequest\",\n\rListLogsReply\x12\x1b\n\tlog_files\x18\x01 \x03(\tR\x08logFiles2\x8a\x02\n\x0fReporterService\x12W\n\x11GetProfilingStats\x12!.ray.rpc.GetProfilingStatsRequest\x1a\x1f.ray.rpc.GetProfilingStatsReply\x12K\n\rReportMetrics\x12\x1d.ray.rpc.ReportMetricsRequest\x1a\x1b.ray.rpc.ReportMetricsReply\x12Q\n\x0fReportOCMetrics\x12\x1f.ray.rpc.ReportOCMetricsRequest\x1a\x1d.ray.rpc.ReportOCMetricsReply2\x8d\x01\n\nLogService\x12<\n\x08ListLogs\x12\x18.ray.rpc.ListLogsRequest\x1a\x16.ray.rpc.ListLogsReply\x12\x41\n\tStreamLog\x12\x19.ray.rpc.StreamLogRequest\x1a\x17.ray.rpc.StreamLogReply0\x01\x42\x03\xf8\x01\x01\x62\x06proto3'
  ,
  dependencies=[opencensus_dot_proto_dot_metrics_dot_v1_dot_metrics__pb2.DESCRIPTOR,src_dot_ray_dot_protobuf_dot_common__pb2.DESCRIPTOR,])




_GETPROFILINGSTATSREQUEST = _descriptor.Descriptor(
  name='GetProfilingStatsRequest',
  full_name='ray.rpc.GetProfilingStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pid', full_name='ray.rpc.GetProfilingStatsRequest.pid', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pid', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='duration', full_name='ray.rpc.GetProfilingStatsRequest.duration', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='duration', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=190,
)


_GETPROFILINGSTATSREPLY = _descriptor.Descriptor(
  name='GetProfilingStatsReply',
  full_name='ray.rpc.GetProfilingStatsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='profiling_stats', full_name='ray.rpc.GetProfilingStatsReply.profiling_stats', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='profilingStats', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std_out', full_name='ray.rpc.GetProfilingStatsReply.std_out', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stdOut', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std_err', full_name='ray.rpc.GetProfilingStatsReply.std_err', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stdErr', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=307,
)


_REPORTMETRICSREQUEST = _descriptor.Descriptor(
  name='ReportMetricsRequest',
  full_name='ray.rpc.ReportMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics_points', full_name='ray.rpc.ReportMetricsRequest.metrics_points', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metricsPoints', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=309,
  serialized_end=392,
)


_REPORTMETRICSREPLY = _descriptor.Descriptor(
  name='ReportMetricsReply',
  full_name='ray.rpc.ReportMetricsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrcs_description_required', full_name='ray.rpc.ReportMetricsReply.metrcs_description_required', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrcsDescriptionRequired', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=478,
)


_REPORTOCMETRICSREQUEST = _descriptor.Descriptor(
  name='ReportOCMetricsRequest',
  full_name='ray.rpc.ReportOCMetricsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='metrics', full_name='ray.rpc.ReportOCMetricsRequest.metrics', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='metrics', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=480,
  serialized_end=567,
)


_REPORTOCMETRICSREPLY = _descriptor.Descriptor(
  name='ReportOCMetricsReply',
  full_name='ray.rpc.ReportOCMetricsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=569,
  serialized_end=591,
)


_NODERESOURCEUSAGE = _descriptor.Descriptor(
  name='NodeResourceUsage',
  full_name='ray.rpc.NodeResourceUsage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='ray.rpc.NodeResourceUsage.json', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='json', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=593,
  serialized_end=632,
)


_STREAMLOGREQUEST = _descriptor.Descriptor(
  name='StreamLogRequest',
  full_name='ray.rpc.StreamLogRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_file_name', full_name='ray.rpc.StreamLogRequest.log_file_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='logFileName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keep_alive', full_name='ray.rpc.StreamLogRequest.keep_alive', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='keepAlive', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lines', full_name='ray.rpc.StreamLogRequest.lines', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='lines', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='interval', full_name='ray.rpc.StreamLogRequest.interval', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='interval', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_lines', full_name='ray.rpc.StreamLogRequest._lines',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_interval', full_name='ray.rpc.StreamLogRequest._interval',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=635,
  serialized_end=803,
)


_STREAMLOGREPLY = _descriptor.Descriptor(
  name='StreamLogReply',
  full_name='ray.rpc.StreamLogReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='ray.rpc.StreamLogReply.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='data', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=805,
  serialized_end=841,
)


_LISTLOGSREQUEST = _descriptor.Descriptor(
  name='ListLogsRequest',
  full_name='ray.rpc.ListLogsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=843,
  serialized_end=860,
)


_LISTLOGSREPLY = _descriptor.Descriptor(
  name='ListLogsReply',
  full_name='ray.rpc.ListLogsReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='log_files', full_name='ray.rpc.ListLogsReply.log_files', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='logFiles', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=862,
  serialized_end=906,
)

_REPORTMETRICSREQUEST.fields_by_name['metrics_points'].message_type = src_dot_ray_dot_protobuf_dot_common__pb2._METRICPOINT
_REPORTOCMETRICSREQUEST.fields_by_name['metrics'].message_type = opencensus_dot_proto_dot_metrics_dot_v1_dot_metrics__pb2._METRIC
_STREAMLOGREQUEST.oneofs_by_name['_lines'].fields.append(
  _STREAMLOGREQUEST.fields_by_name['lines'])
_STREAMLOGREQUEST.fields_by_name['lines'].containing_oneof = _STREAMLOGREQUEST.oneofs_by_name['_lines']
_STREAMLOGREQUEST.oneofs_by_name['_interval'].fields.append(
  _STREAMLOGREQUEST.fields_by_name['interval'])
_STREAMLOGREQUEST.fields_by_name['interval'].containing_oneof = _STREAMLOGREQUEST.oneofs_by_name['_interval']
DESCRIPTOR.message_types_by_name['GetProfilingStatsRequest'] = _GETPROFILINGSTATSREQUEST
DESCRIPTOR.message_types_by_name['GetProfilingStatsReply'] = _GETPROFILINGSTATSREPLY
DESCRIPTOR.message_types_by_name['ReportMetricsRequest'] = _REPORTMETRICSREQUEST
DESCRIPTOR.message_types_by_name['ReportMetricsReply'] = _REPORTMETRICSREPLY
DESCRIPTOR.message_types_by_name['ReportOCMetricsRequest'] = _REPORTOCMETRICSREQUEST
DESCRIPTOR.message_types_by_name['ReportOCMetricsReply'] = _REPORTOCMETRICSREPLY
DESCRIPTOR.message_types_by_name['NodeResourceUsage'] = _NODERESOURCEUSAGE
DESCRIPTOR.message_types_by_name['StreamLogRequest'] = _STREAMLOGREQUEST
DESCRIPTOR.message_types_by_name['StreamLogReply'] = _STREAMLOGREPLY
DESCRIPTOR.message_types_by_name['ListLogsRequest'] = _LISTLOGSREQUEST
DESCRIPTOR.message_types_by_name['ListLogsReply'] = _LISTLOGSREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetProfilingStatsRequest = _reflection.GeneratedProtocolMessageType('GetProfilingStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETPROFILINGSTATSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetProfilingStatsRequest)
  })
_sym_db.RegisterMessage(GetProfilingStatsRequest)

GetProfilingStatsReply = _reflection.GeneratedProtocolMessageType('GetProfilingStatsReply', (_message.Message,), {
  'DESCRIPTOR' : _GETPROFILINGSTATSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.GetProfilingStatsReply)
  })
_sym_db.RegisterMessage(GetProfilingStatsReply)

ReportMetricsRequest = _reflection.GeneratedProtocolMessageType('ReportMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETRICSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportMetricsRequest)
  })
_sym_db.RegisterMessage(ReportMetricsRequest)

ReportMetricsReply = _reflection.GeneratedProtocolMessageType('ReportMetricsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTMETRICSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportMetricsReply)
  })
_sym_db.RegisterMessage(ReportMetricsReply)

ReportOCMetricsRequest = _reflection.GeneratedProtocolMessageType('ReportOCMetricsRequest', (_message.Message,), {
  'DESCRIPTOR' : _REPORTOCMETRICSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportOCMetricsRequest)
  })
_sym_db.RegisterMessage(ReportOCMetricsRequest)

ReportOCMetricsReply = _reflection.GeneratedProtocolMessageType('ReportOCMetricsReply', (_message.Message,), {
  'DESCRIPTOR' : _REPORTOCMETRICSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ReportOCMetricsReply)
  })
_sym_db.RegisterMessage(ReportOCMetricsReply)

NodeResourceUsage = _reflection.GeneratedProtocolMessageType('NodeResourceUsage', (_message.Message,), {
  'DESCRIPTOR' : _NODERESOURCEUSAGE,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.NodeResourceUsage)
  })
_sym_db.RegisterMessage(NodeResourceUsage)

StreamLogRequest = _reflection.GeneratedProtocolMessageType('StreamLogRequest', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.StreamLogRequest)
  })
_sym_db.RegisterMessage(StreamLogRequest)

StreamLogReply = _reflection.GeneratedProtocolMessageType('StreamLogReply', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLOGREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.StreamLogReply)
  })
_sym_db.RegisterMessage(StreamLogReply)

ListLogsRequest = _reflection.GeneratedProtocolMessageType('ListLogsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGSREQUEST,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ListLogsRequest)
  })
_sym_db.RegisterMessage(ListLogsRequest)

ListLogsReply = _reflection.GeneratedProtocolMessageType('ListLogsReply', (_message.Message,), {
  'DESCRIPTOR' : _LISTLOGSREPLY,
  '__module__' : 'src.ray.protobuf.reporter_pb2'
  # @@protoc_insertion_point(class_scope:ray.rpc.ListLogsReply)
  })
_sym_db.RegisterMessage(ListLogsReply)


DESCRIPTOR._options = None

_REPORTERSERVICE = _descriptor.ServiceDescriptor(
  name='ReporterService',
  full_name='ray.rpc.ReporterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=909,
  serialized_end=1175,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetProfilingStats',
    full_name='ray.rpc.ReporterService.GetProfilingStats',
    index=0,
    containing_service=None,
    input_type=_GETPROFILINGSTATSREQUEST,
    output_type=_GETPROFILINGSTATSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportMetrics',
    full_name='ray.rpc.ReporterService.ReportMetrics',
    index=1,
    containing_service=None,
    input_type=_REPORTMETRICSREQUEST,
    output_type=_REPORTMETRICSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReportOCMetrics',
    full_name='ray.rpc.ReporterService.ReportOCMetrics',
    index=2,
    containing_service=None,
    input_type=_REPORTOCMETRICSREQUEST,
    output_type=_REPORTOCMETRICSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_REPORTERSERVICE)

DESCRIPTOR.services_by_name['ReporterService'] = _REPORTERSERVICE


_LOGSERVICE = _descriptor.ServiceDescriptor(
  name='LogService',
  full_name='ray.rpc.LogService',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1178,
  serialized_end=1319,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListLogs',
    full_name='ray.rpc.LogService.ListLogs',
    index=0,
    containing_service=None,
    input_type=_LISTLOGSREQUEST,
    output_type=_LISTLOGSREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='StreamLog',
    full_name='ray.rpc.LogService.StreamLog',
    index=1,
    containing_service=None,
    input_type=_STREAMLOGREQUEST,
    output_type=_STREAMLOGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LOGSERVICE)

DESCRIPTOR.services_by_name['LogService'] = _LOGSERVICE

# @@protoc_insertion_point(module_scope)
