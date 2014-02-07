//============================================================
// USERID:........ KMANZANA
// PROGRAMMER:.... Manzanares, Kelton M.
// COURSE:........ CSCI-410
// TERM:.......... SP14
// PROJECT:....... 04
// FILENAME:...... Fill.asm
//============================================================

// This file is based on a file from www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

  @8192
  D=A
  @size
  M=D // size = 8192

  @write
  M=-1 // write = 0

(MAIN)

  @KBD
  D=M
  @PRESSED
  D;JNE
  @write
  M=0
  @NOT_PRESSED
  0;JMP
(PRESSED)
  @write
  M=-1
(NOT_PRESSED)
  @index
  M=0 // index = 0

(LOOP)
  @index
  D=M
  @SCREEN
  D=A+D
  @pointer
  M=D
  @write
  D=M
  @pointer
  A=M
  M=D
  @index
  M=M+1
  D=M
  @size
  D=D-M
  @LOOP
  D;JNE

  @MAIN
  0;JMP
// Pseudo code
// size = 2^13 = 8192
// while true
//   if KBD == 0
//     a = size
//     while a != 0
//       SCREEN[a] = -1
//       a--
//     end
//   else
//     a = size
//     while a != 0
//       SCREEN[a] = 0
//       a--
//     end
//   end
// end
