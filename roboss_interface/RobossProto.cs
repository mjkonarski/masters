//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

// Generated from: roboss.proto
namespace roboss
{
  [global::System.Serializable, global::ProtoBuf.ProtoContract(Name=@"RobotState")]
  public partial class RobotState : global::ProtoBuf.IExtensible
  {
    public RobotState() {}
    
    private double _x;
    [global::ProtoBuf.ProtoMember(1, IsRequired = true, Name=@"x", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double x
    {
      get { return _x; }
      set { _x = value; }
    }
    private double _y;
    [global::ProtoBuf.ProtoMember(2, IsRequired = true, Name=@"y", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double y
    {
      get { return _y; }
      set { _y = value; }
    }
    private double _theta;
    [global::ProtoBuf.ProtoMember(3, IsRequired = true, Name=@"theta", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double theta
    {
      get { return _theta; }
      set { _theta = value; }
    }
    private long _timestamp;
    [global::ProtoBuf.ProtoMember(4, IsRequired = true, Name=@"timestamp", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public long timestamp
    {
      get { return _timestamp; }
      set { _timestamp = value; }
    }
    private global::ProtoBuf.IExtension extensionObject;
    global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
      { return global::ProtoBuf.Extensible.GetExtensionObject(ref extensionObject, createIfMissing); }
  }
  
  [global::System.Serializable, global::ProtoBuf.ProtoContract(Name=@"RobossRequest")]
  public partial class RobossRequest : global::ProtoBuf.IExtensible
  {
    public RobossRequest() {}
    
    private RobossRequest.Type _type;
    [global::ProtoBuf.ProtoMember(1, IsRequired = true, Name=@"type", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public RobossRequest.Type type
    {
      get { return _type; }
      set { _type = value; }
    }

    private WheelsCommand _wheelsCmd = null;
    [global::ProtoBuf.ProtoMember(2, IsRequired = false, Name=@"wheelsCmd", DataFormat = global::ProtoBuf.DataFormat.Default)]
    [global::System.ComponentModel.DefaultValue(null)]
    public WheelsCommand wheelsCmd
    {
      get { return _wheelsCmd; }
      set { _wheelsCmd = value; }
    }
    [global::ProtoBuf.ProtoContract(Name=@"Type")]
    public enum Type
    {
            
      [global::ProtoBuf.ProtoEnum(Name=@"WHEELS_CMD", Value=0)]
      WHEELS_CMD = 0,
            
      [global::ProtoBuf.ProtoEnum(Name=@"STATE_REQUEST", Value=1)]
      STATE_REQUEST = 1,
            
      [global::ProtoBuf.ProtoEnum(Name=@"START", Value=2)]
      START = 2,
            
      [global::ProtoBuf.ProtoEnum(Name=@"STOP", Value=3)]
      STOP = 3,
            
      [global::ProtoBuf.ProtoEnum(Name=@"RESET", Value=4)]
      RESET = 4
    }
  
    private global::ProtoBuf.IExtension extensionObject;
    global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
      { return global::ProtoBuf.Extensible.GetExtensionObject(ref extensionObject, createIfMissing); }
  }
  
  [global::System.Serializable, global::ProtoBuf.ProtoContract(Name=@"WheelsCommand")]
  public partial class WheelsCommand : global::ProtoBuf.IExtensible
  {
    public WheelsCommand() {}
    
    private double _frontLeft;
    [global::ProtoBuf.ProtoMember(1, IsRequired = true, Name=@"frontLeft", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double frontLeft
    {
      get { return _frontLeft; }
      set { _frontLeft = value; }
    }
    private double _frontRight;
    [global::ProtoBuf.ProtoMember(2, IsRequired = true, Name=@"frontRight", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double frontRight
    {
      get { return _frontRight; }
      set { _frontRight = value; }
    }
    private double _rearLeft;
    [global::ProtoBuf.ProtoMember(3, IsRequired = true, Name=@"rearLeft", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double rearLeft
    {
      get { return _rearLeft; }
      set { _rearLeft = value; }
    }
    private double _rearRight;
    [global::ProtoBuf.ProtoMember(4, IsRequired = true, Name=@"rearRight", DataFormat = global::ProtoBuf.DataFormat.TwosComplement)]
    public double rearRight
    {
      get { return _rearRight; }
      set { _rearRight = value; }
    }
    private global::ProtoBuf.IExtension extensionObject;
    global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
      { return global::ProtoBuf.Extensible.GetExtensionObject(ref extensionObject, createIfMissing); }
  }
  
}