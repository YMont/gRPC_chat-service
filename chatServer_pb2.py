# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chatServer.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x63hatServer.proto\x12\x04grpc\"%\n\x04Note\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x07\n\x05\x45mpty2Z\n\nChatServer\x12\'\n\nChatStream\x12\x0b.grpc.Empty\x1a\n.grpc.Note0\x01\x12#\n\x08SendNote\x12\n.grpc.Note\x1a\x0b.grpc.Emptyb\x06proto3')



_NOTE = DESCRIPTOR.message_types_by_name['Note']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
Note = _reflection.GeneratedProtocolMessageType('Note', (_message.Message,), {
  'DESCRIPTOR' : _NOTE,
  '__module__' : 'chatServer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Note)
  })
_sym_db.RegisterMessage(Note)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'chatServer_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

_CHATSERVER = DESCRIPTOR.services_by_name['ChatServer']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOTE._serialized_start=26
  _NOTE._serialized_end=63
  _EMPTY._serialized_start=65
  _EMPTY._serialized_end=72
  _CHATSERVER._serialized_start=74
  _CHATSERVER._serialized_end=164
# @@protoc_insertion_point(module_scope)
