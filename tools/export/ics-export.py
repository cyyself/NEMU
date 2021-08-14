#!/usr/bin/env python3

from utils import export

WHITE_LIST = [
  r'.gitignore',
  r'^/*$',
  r'Makefile',
  r'^/src/',
  r'^/include/',
  r'^/configs/',
  r'^/resource/debian/',
  r'^/resource/mips-elf/',
  r'^/resource/sdcard/',
  r'^/scripts/',
  r'^/tools/*',
]

BLACK_LIST = [
  r'/build/',
  r'/export/',
  r'/.git/',
  r'/.config',
  r'/difftest/ref.c',
  r'^/include/config/',
  r'^/include/generated/',
  r'^/include/memory/host-tlb.h',
  r'^/include/rtl/fp.h',
  r'^/src/isa/mips32/local-include/intr.h',
  r'^/src/isa/x86/exec/eflags.c',
  r'^/src/isa/x86/exec/lazycc.h',
  r'^/src/isa/x86/exec/string.h',
  r'^/src/isa/x86/kvm/',
  r'^/src/isa/x86/local-include/mmu.h',

  r'^/src/isa/x86/',
  r'^/src/isa/mips32/',
  r'^/src/isa/riscv32/instr/compress.h',
  r'^/src/isa/riscv32/instr/control.h',
  r'^/src/isa/riscv32/instr/muldiv.h',
  r'^/src/isa/riscv32/instr/pseudo.h',
  r'^/src/isa/riscv32/instr/system.h',
  r'^/src/isa/riscv64/clint.c',
  r'^/src/isa/riscv64/filelist.mk',
  r'^/src/isa/riscv64/Kconfig',
  r'^/src/isa/riscv64/local-include/csr.h',
  r'^/src/isa/riscv64/local-include/intr.h',
  r'^/src/isa/riscv64/instr/rv*/',
  r'^/src/isa/riscv64/instr/rv*/',
  r'^/src/isa/riscv64/instr/priv/',
  r'^/src/isa/riscv64/instr/fp.c',
  r'^/src/isa/riscv64/instr/pseudo.h',
  r'^/src/isa/riscv64/instr/rocc.h',

  r'^/src/cpu/tcache.c',
  r'^/src/engine/interpreter/*-fp.[ch]',
  r'^/src/memory/host-tlb.c',
  r'^/src/monitor/aligncheck.c',
  r'^/src/user/',
  r'^/src/utils/iqueue.c',
  r'^/resource/softfloat/',
  r'^/tools/spike-diff/repo/',
]

export(WHITE_LIST, BLACK_LIST)
