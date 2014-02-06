//============================================================
// USERID:........ KMANZANA
// PROGRAMMER:.... Manzanares, Kelton M.
// COURSE:........ CSCI-410
// TERM:.......... SP14
// PROJECT:....... 04
// FILENAME:...... Mult.asm
//============================================================

// This file is based on a file from www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

// Pseudo code:
// R2 = 0
// do {
//   R2 += R1
//   R0 -= 1
// } while (R0 != 0)

  @0
  D=0
  @2
  M=D
  @ENTER_LOOP
  0;JMP
(LOOP)
  @1
  D=M
  @2
  M=M+D
  @0
  M=M-1
(ENTER_LOOP)
  @0
  D=M
  @LOOP
  D;JNE
