
Import("env")

#
# Dump build environment (for debug)
# print(env.Dump())
#       "-TSTM32H743ZITx_FLASH_WD2.ld",

# Replace assembler with C compiler as is done in ~/.platformio/platforms/ststm32/builder/frameworks/stm32cube.py
env.Replace(
    AS="$CC",
    ASCOM="$ASPPCOM"
)

env.Append(
  LINKFLAGS=[
      "-mfloat-abi=hard",
      "-mfpu=fpv4-sp-d16",
      "--specs=nano.specs",
      "--specs=nosys.specs",
      "-lm",
      "-lnosys"
  ]
)
