//============================================================
// USERID:........ KMANZANA
// PROGRAMMER:.... Manzanares, Kelton M.
// COURSE:........ CSCI-410
// TERM:.......... SP14
// PROJECT:....... translated
// FILENAME:...... BasicTest.asm
//============================================================

@10
D=A
@SP
A=M
M=D
@SP
M=M+1

@LCL
D=A
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1

@21
D=A
@SP
A=M
M=D
@SP
M=M+1

@22
D=A
@SP
A=M
M=D
@SP
M=M+1

@ARG
D=A
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1

@ARG
D=A
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1

@36
D=A
@SP
A=M
M=D
@SP
M=M+1

@THIS
D=A
@6
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1

@42
D=A
@SP
A=M
M=D
@SP
M=M+1

@45
D=A
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=A
@5
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1

@THAT
D=A
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M-1

@510
D=A
@SP
A=M
M=D
@SP
M=M+1

@THAT
D=A
@11
A=D+A
D=M
@SP
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
A=M-1
D=M
A=A-1
M=M-D
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
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
@SP
A=M-1
D=M
A=A-1
M=M+D
@SP
M=M-1
