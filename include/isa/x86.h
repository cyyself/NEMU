#ifndef __ISA_X86_H__
#define __ISA_X86_H__

#include <common.h>
#include <isa/mmu.h>

// memory
#define IMAGE_START 0x100000
#define PMEM_BASE 0x0

// reg

/* TODO: Re-organize the `CPU_state' structure to match the register
 * encoding scheme in i386 instruction format. For example, if we
 * access cpu.gpr[3]._16, we will get the `bx' register; if we access
 * cpu.gpr[1]._8[1], we will get the 'ch' register. Hint: Use `union'.
 * For more details about the register encoding scheme, see i386 manual.
 */

typedef struct {
  union {
    union {
      uint32_t _32;
      uint16_t _16;
      uint8_t _8[2];
    } gpr[8];

  /* Do NOT change the order of the GPRs' definitions. */

  /* In NEMU, rtlreg_t is exactly uint32_t. This makes RTL instructions
   * in PA2 able to directly access these registers.
   */
    struct {
      rtlreg_t eax, ecx, edx, ebx, esp, ebp, esi, edi;
    };
  };

  vaddr_t pc;
  uint32_t eflags;
  uint16_t cs;

  rtlreg_t OF, CF, SF, ZF, IF;

  struct {
    uint32_t limit :16;
    uint32_t base  :32;
  } idtr;

  union {
    rtlreg_t cr[4];
    struct {
      CR0 cr0;
      rtlreg_t cr1;
      rtlreg_t cr2;
      CR3 cr3;
    };
  };

  bool INTR;
} CPU_state;

// decode
struct ISADecodeInfo {
  bool is_operand_size_16;
  uint8_t ext_opcode;
};

#define suffix_char(width) ((width) == 4 ? 'l' : ((width) == 1 ? 'b' : ((width) == 2 ? 'w' : '?')))

#endif
