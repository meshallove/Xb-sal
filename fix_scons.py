import sys, types
import SCons.Tool

if not hasattr(SCons.Tool, "FortranCommon"):
    mod = types.ModuleType("SCons.Tool.FortranCommon")
    SCons.Tool.FortranCommon = mod
    sys.modules["SCons.Tool.FortranCommon"] = mod
