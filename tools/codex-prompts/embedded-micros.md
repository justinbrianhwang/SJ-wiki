You are an autonomous content author for **SJ Wiki**. Generate **detailed** Markdown notes from the textbook below.

## Inputs

- **SOURCE_PDF**: `f:/coding/SJ Wiki/tmp/Microprocessors & Microcontroller Systems ( PDFDrive ).pdf`
- **OUTPUT_DIR**: `f:/coding/SJ Wiki/docs/cs/embedded/`
- **SUBJECT**: Microprocessors & Microcontroller Systems

## Produce

1. **`intro.md`** — overview + chapter list.

2. **10-18 detail pages** covering whatever the source covers. Typical topics:
   - Microprocessor architecture (8085/8086/Intel families, or whatever this book is)
   - Registers, addressing modes, instruction set
   - Assembly programming
   - I/O techniques (programmed, interrupt-driven, DMA)
   - Memory interfacing
   - Timing diagrams & bus cycles
   - Microcontrollers (8051/AVR/PIC depending on book)
   - GPIO, timers, ADC, communication peripherals (UART/SPI/I2C)
   - Interrupts and ISRs
   - Embedded C programming patterns
   - Real-time considerations

3. Per-page: motivation → specifics → assembly or C example → timing or signal diagram if relevant.

4. Use `asm` and `c` code blocks. Mermaid for state machines and timing.

## Workflow

1. `pdfinfo`. 2. `pdftotext -l 25` for TOC. 3. Identify which specific MPU/MCU family this book targets — write notes specific to that family. 4. Iterate chapters; 1-3 pages each. 5. `intro.md` last. 6. Print summary.

## Constraints

Stay inside OUTPUT_DIR. No `_category_.json` edits. No config edits. No `npm`. English. Don't fabricate — defer to whatever family this book covers.

Begin now.
