# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: client.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='client.proto',
  package='',
  serialized_pb='\n\x0c\x63lient.proto\"\x80\x01\n\x0cStateMessage\x12#\n\nrobotState\x18\x01 \x03(\x0b\x32\x0f.RobotFullState\x12\"\n\x05\x65vent\x18\x02 \x01(\x0e\x32\x13.StateMessage.Event\"\'\n\x05\x45vent\x12\x08\n\x04STOP\x10\x01\x12\t\n\x05START\x10\x02\x12\t\n\x05RESET\x10\x03\"o\n\x0eRobotFullState\x12\x11\n\trobotName\x18\x01 \x02(\t\x12\t\n\x01x\x18\x02 \x02(\x01\x12\t\n\x01y\x18\x03 \x02(\x01\x12\r\n\x05theta\x18\x04 \x02(\x01\x12\x11\n\ttimestamp\x18\x05 \x02(\x03\x12\x12\n\nfearFactor\x18\x06 \x02(\x01\"!\n\x0cSetupMessage\x12\x11\n\trobotName\x18\x01 \x02(\t\"\x05\n\x03\x41\x63k\"\x87\x01\n\x0e\x43ommandMessage\x12\"\n\x04type\x18\x01 \x02(\x0e\x32\x14.CommandMessage.Type\x12#\n\x0crobotCommand\x18\x02 \x01(\x0b\x32\r.RobotCommand\",\n\x04Type\x12\x11\n\rREQUEST_STATE\x10\x01\x12\x11\n\rROBOT_COMMAND\x10\x02\"n\n\x0cRobotCommand\x12\x11\n\tfrontLeft\x18\x01 \x02(\x01\x12\x12\n\nfrontRight\x18\x02 \x02(\x01\x12\x10\n\x08rearLeft\x18\x03 \x02(\x01\x12\x11\n\trearRight\x18\x04 \x02(\x01\x12\x12\n\nfearFactor\x18\x05 \x02(\x01')



_STATEMESSAGE_EVENT = _descriptor.EnumDescriptor(
  name='Event',
  full_name='StateMessage.Event',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STOP', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='START', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=2, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=106,
  serialized_end=145,
)

_COMMANDMESSAGE_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='CommandMessage.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='REQUEST_STATE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ROBOT_COMMAND', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=394,
  serialized_end=438,
)


_STATEMESSAGE = _descriptor.Descriptor(
  name='StateMessage',
  full_name='StateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robotState', full_name='StateMessage.robotState', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='StateMessage.event', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STATEMESSAGE_EVENT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=17,
  serialized_end=145,
)


_ROBOTFULLSTATE = _descriptor.Descriptor(
  name='RobotFullState',
  full_name='RobotFullState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robotName', full_name='RobotFullState.robotName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='RobotFullState.x', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='RobotFullState.y', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='theta', full_name='RobotFullState.theta', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='RobotFullState.timestamp', index=4,
      number=5, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fearFactor', full_name='RobotFullState.fearFactor', index=5,
      number=6, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=147,
  serialized_end=258,
)


_SETUPMESSAGE = _descriptor.Descriptor(
  name='SetupMessage',
  full_name='SetupMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robotName', full_name='SetupMessage.robotName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=260,
  serialized_end=293,
)


_ACK = _descriptor.Descriptor(
  name='Ack',
  full_name='Ack',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=295,
  serialized_end=300,
)


_COMMANDMESSAGE = _descriptor.Descriptor(
  name='CommandMessage',
  full_name='CommandMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CommandMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='robotCommand', full_name='CommandMessage.robotCommand', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMMANDMESSAGE_TYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=303,
  serialized_end=438,
)


_ROBOTCOMMAND = _descriptor.Descriptor(
  name='RobotCommand',
  full_name='RobotCommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frontLeft', full_name='RobotCommand.frontLeft', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='frontRight', full_name='RobotCommand.frontRight', index=1,
      number=2, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rearLeft', full_name='RobotCommand.rearLeft', index=2,
      number=3, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rearRight', full_name='RobotCommand.rearRight', index=3,
      number=4, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fearFactor', full_name='RobotCommand.fearFactor', index=4,
      number=5, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=440,
  serialized_end=550,
)

_STATEMESSAGE.fields_by_name['robotState'].message_type = _ROBOTFULLSTATE
_STATEMESSAGE.fields_by_name['event'].enum_type = _STATEMESSAGE_EVENT
_STATEMESSAGE_EVENT.containing_type = _STATEMESSAGE;
_COMMANDMESSAGE.fields_by_name['type'].enum_type = _COMMANDMESSAGE_TYPE
_COMMANDMESSAGE.fields_by_name['robotCommand'].message_type = _ROBOTCOMMAND
_COMMANDMESSAGE_TYPE.containing_type = _COMMANDMESSAGE;
DESCRIPTOR.message_types_by_name['StateMessage'] = _STATEMESSAGE
DESCRIPTOR.message_types_by_name['RobotFullState'] = _ROBOTFULLSTATE
DESCRIPTOR.message_types_by_name['SetupMessage'] = _SETUPMESSAGE
DESCRIPTOR.message_types_by_name['Ack'] = _ACK
DESCRIPTOR.message_types_by_name['CommandMessage'] = _COMMANDMESSAGE
DESCRIPTOR.message_types_by_name['RobotCommand'] = _ROBOTCOMMAND

class StateMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STATEMESSAGE

  # @@protoc_insertion_point(class_scope:StateMessage)

class RobotFullState(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBOTFULLSTATE

  # @@protoc_insertion_point(class_scope:RobotFullState)

class SetupMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _SETUPMESSAGE

  # @@protoc_insertion_point(class_scope:SetupMessage)

class Ack(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ACK

  # @@protoc_insertion_point(class_scope:Ack)

class CommandMessage(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMANDMESSAGE

  # @@protoc_insertion_point(class_scope:CommandMessage)

class RobotCommand(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROBOTCOMMAND

  # @@protoc_insertion_point(class_scope:RobotCommand)


# @@protoc_insertion_point(module_scope)
