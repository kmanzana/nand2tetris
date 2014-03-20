//============================================================
// USERID:........ KMANZANA
// PROGRAMMER:.... Manzanares, Kelton M.
// COURSE:........ CSCI-410
// TERM:.......... SP14
// PROJECT:....... translated
// FILENAME:...... BasicLoop.asm
//============================================================

@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
AM=M-1
D=M
@R13
M=D
@LCL
D=M
@0
D=D+A
A=M
M=D
@SP
M=M-1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
@SP
AM=M-1
D=M
@R13
M=D
@LCL
D=M
@0
D=D+A
A=M
M=D
@SP
M=M-1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
@ARG
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1
