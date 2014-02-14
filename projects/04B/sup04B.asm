//============================================================
// USERID:........ kmanzana
// PROGRAMMER:.... Manzanares, Kelton M.
// COURSE:........ CSCI-410
// TERM:.......... SP14
// PROJECT:....... 04B
// FILENAME:...... sup04B.tst
//============================================================

//============================================================
// The BOOTSTRAP, MAIN, and SLL code was provided and used
// without modification.
//============================================================

//============================================================
// BOOTSTRAP CODE
//============================================================
// The test script monitors R15 and terminates the test once
// it sees it become zero. The bootstrap code enters an
// infinite loop after that so that the program can be run
// independent of the test script.
//------------------------------------------------------------
// Arguments......... N/A
// Return values..... N/A
// Local variables... NONE
// Global variables.. R15: running flag
//------------------------------------------------------------
// High Level Language Equivalant
//
// running = TRUE;
// main();
// running = FALSE;
// while(TRUE);
//------------------------------------------------------------
@R15               // running = TRUE;
M = -1

@RET_MAIN          // main();
D = A
@MAIN.0
M = D
@MAIN
0; JMP
(RET_MAIN)

@R15               // running = FALSE;
M = 0

(DONE)
@DONE              // while(TRUE);
0; JMP

//============================================================
// SLL: Shift Logical Left (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// This is the primitive operation used by all of the other
// shift/rotate operations. It is implemented by noting that
// a left shift operation is effectively a multiplication by
// two which, in turn, can be effected on the HACK platform
// by adding a value to itself.
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SLL(int16 data)
// {
//    data += data;
//    return data;
// }
//------------------------------------------------------------

(SLL)

@SLL.1             // SLL.1 += SLL.1
D = M
M = D+M

@SLL.0             // Return
A = M
0; JMP

//***************** START OF STUDENT CODE ********************

//============================================================
// SLR: Shift Logical Right (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SLR(int16 data) {
//   data = ROTLN(data, 15);
//   data &= 0x7FFF;
//   return data
// }
//------------------------------------------------------------

(SLR)

@SLR.1          // first ROTLN arg
D = M
@ROTLN.1
M = D
@15             // second ROTLN arg
D = A
@ROTLN.2
M = D

@RET_ROTLN_SLR  // Load RA
D = A
@ROTLN.0
M = D
@ROTLN          // Call ROTLN
0; JMP
(RET_ROTLN_SLR)

@ROTLN.1       // Load return value
D = M
@SLR.1
M = D

@32767         // 0x7FFF
D = A
@SLR.1
M = M & D      // mask the first bit

@SLR.0      // return
A = M
0; JMP

//============================================================
// SLLN: Shift Logical Left (by N)
//============================================================
// Arguments......... 2: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SLL(int16 data, int16 amount) {
//   for (int i = 0; i < amount; ++i) {
//     data = SLL(data);
//   }

//   return data
// }
//------------------------------------------------------------

(SLLN)

(SLLN_DO)
@SLLN.1        // Load SLL arg
D = M
@SLL.1
M = D

@RET_SLL_SLLN  // Load RA
D = A
@SLL.0
M = D

@SLL           // Call SLL
0; JMP
(RET_SLL_SLLN)

@SLL.1         // data = SLL(data)
D = M
@SLLN.1
M = D

@SLLN.2         // --amount
M = M - 1

D = M
@SLLN_END
D; JEQ          // if (amount == 0)

@SLLN_DO
0; JMP

(SLLN_END)

@SLLN.0
A = M
0; JMP

//============================================================
// SLRN: Shift Logical Right (by N)
//============================================================
// Arguments......... 2: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SLR(int16 data, int16 amount) {
//   for (int i = 0; i < amount; ++i) {
//     data = SLR(data);
//   }

//   return data
// }
//------------------------------------------------------------

(SLRN)

(SLRN_DO)
@SLRN.1        // Load SLR arg
D = M
@SLR.1
M = D

@RET_SLR_SLRN  // Load RA
D = A
@SLR.0
M = D

@SLR           // Call SLR
0; JMP
(RET_SLR_SLRN)

@SLR.1         // data = SLR(data)
D = M
@SLRN.1
M = D

@SLRN.2         // --amount
M = M - 1

D = M
@SLRN_END
D; JEQ          // if (amount == 0)

@SLRN_DO
0; JMP

(SLRN_END)

@SLRN.0
A = M
0; JMP

//============================================================
// SLN: Shift Logical (by N)
//============================================================
// Arguments......... 1: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SLN(int16 data, amount) {
//   if (amount >= 0) {
//     SLRN(data, amount);
//   } else {
//     SLLN(data, amount);
//   }
// }
//------------------------------------------------------------

(SLN)

@SLN.1
D = M
@SLN_IF_NEG   // if (data >= 0)
D; JLT

@SLN.1        // Argument 1 (data value)
D = M
@SLRN.1
M = D
@SLN.2        // Argument 2 (shift/rotate amount)
D = M
@SLRN.2
M = D

@RET_SLRN_SLN // Load RA
D = A
@SLRN.0
M = D
@SLRN         // Call subroutine
0; JMP
(RET_SLRN_SLN)

@SLRN.1       // Store returned value
D = M
@SLN.1
M = D

@SLN_IF_NEG_END
0; JMP
(SLN_IF_NEG)

@SLN.1        // Argument 1 (data value)
D = M
@SLLN.1
M = D
@SLN.2        // Argument 2 (shift/rotate amount)
D = -M
@SLLN.2
M = D

@RET_SLLN_SLN // Load RA
D = A
@SLLN.0
M = D
@SLLN         // Call subroutine
0; JMP
(RET_SLLN_SLN)

@SLLN.1       // Store returned value
D = M
@SLN.1
M = D
(SLN_IF_NEG_END)

@SLN.0
A = M
0; JMP

//============================================================
// SAR: Shift Arithmetic Right (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SAR(int16 data) {
//   if (data >= 0) {
//     mask = 0x0000;
//   } else {
//     mask = 0x8000;
//   }

//   data = SLR(data);
//   data |= mask;
//   return data
// }
//------------------------------------------------------------

(SAR)

@SAR.1
D = M

@SAR_IF_NEG   // if (data >= 0)
D; JLT
@mask
M = 0         // mask = 0x0000
@SAR_IF_NEG_END
0; JMP

(SAR_IF_NEG)
@32767
D = !A
@mask
M = D         // mask = 0x8000
(SAR_IF_NEG_END)

@SAR.1        // Load arg
D = M
@SLR.1
M = D

@RET_SLR_SAR  // Load RA
D = A
@SLR.0
M = D

@SLR          // Call SLR
0; JMP
(RET_SLR_SAR)

@SLR.1        // data = SLR(data)
D = M
@R1
M = D

@mask
D = M
@R1
M = M | D     // data &= mask

@R1
D = M
@SAR.1       // return data
M = D

@SAR.0
A = M
0; JMP

//============================================================
// SARN: Shift Arithmetic Right (by N)
//============================================================
// Arguments......... 2: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SARN(int16 data, int16 amount) {
//   for (int i = 0; i < amount; ++i) {
//     data = SAR(data);
//   }
//
//   return data
// }
//------------------------------------------------------------

(SARN)

(SARN_DO)
@SARN.1        // Load SAR arg
D = M
@SAR.1
M = D

@RET_SAR_SARN  // Load RA
D = A
@SAR.0
M = D

@SAR           // Call SAR
0; JMP
(RET_SAR_SARN)

@SAR.1         // data = SAR(data)
D = M
@SARN.1
M = D

@SARN.2         // --amount
M = M - 1

D = M
@SARN_END
D; JEQ          // if (amount == 0)

@SARN_DO
0; JMP

(SARN_END)

@SARN.0
A = M
0; JMP

//============================================================
// SAN: Shift Arithmetic (by N)
//============================================================
// Arguments......... 1: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SAN(int16 data, amount) {
//   if (amount >= 0) {
//     SARN(data, amount);
//   } else {
//     SLLN(data, amount);
//   }
// }
//------------------------------------------------------------

(SAN)

@SAN.1
D = M
@SAN_IF_NEG   // if (data >= 0)
D; JLT

@SAN.1        // Argument 1 (data value)
D = M
@SARN.1
M = D
@SAN.2        // Argument 2 (shift/rotate amount)
D = M
@SARN.2
M = D

@RET_SARN_SAN // Load RA
D = A
@SARN.0
M = D
@SARN         // Call subroutine
0; JMP
(RET_SARN_SAN)

@SARN.1       // Store returned value
D = M
@SAN.1
M = D

@SAN_IF_NEG_END
0; JMP
(SAN_IF_NEG)

@SAN.1        // Argument 1 (data value)
D = M
@SLLN.1
M = D
@SAN.2        // Argument 2 (shift/rotate amount)
D = -M
@SLLN.2
M = D

@RET_SLLN_SAN // Load RA
D = A
@SLLN.0
M = D
@SLLN         // Call subroutine
0; JMP
(RET_SLLN_SAN)

@SLLN.1       // Store returned value
D = M
@SAN.1
M = D
(SAN_IF_NEG_END)

@SAN.0
A = M
0; JMP

//============================================================
// ROTL: Rotate Left (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 ROTL(int16 data) {
//   int R0;
//   if (data >= 0) {
//     R0 = 0;
//   } else {
//     R0 = 1;
//   }

//   data = SLL(data);
//   data += R0;
//   return data
// }
//------------------------------------------------------------

(ROTL)

@ROTL.1
D = M

@ROTL_IF_NEG       // if (data >= 0)
D; JLT
@R0
M = 0         // R0 = 0
@ROTL_IF_NEG_END
0; JMP
(ROTL_IF_NEG)
@R0
M = 1         // R0 = 1
(ROTL_IF_NEG_END)

@ROTL.1       // Load arg
D = M
@SLL.1
M = D

@RET_SLL_ROTL // Load RA
D = A
@SLL.0
M = D

@SLL          // Call SSL
0; JMP
(RET_SLL_ROTL)

@SLL.1        // data = SSL(data)
D = M
@R1
M = D

@R0
D = M
@R1
M = M + D     // data += R0

@R1
D = M
@ROTL.1       // return data
M = D

@ROTL.0       // return to address
A = M
0; JMP

//============================================================
// ROTR: Rotate Right (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 ROTR(int16 data) {
//   data = ROTLN(data, 15)
//
//   return data
// }
//------------------------------------------------------------

(ROTR)

@ROTR.1          // first ROTLN arg
D = M
@ROTLN.1
M = D
@15             // second ROTLN arg
D = A
@ROTLN.2
M = D

@RET_ROTLN_ROTR  // Load RA
D = A
@ROTLN.0
M = D
@ROTLN          // Call ROTLN
0; JMP
(RET_ROTLN_ROTR)

@ROTLN.1       // Load return value
D = M
@ROTR.1
M = D

@ROTR.0     // return to address
A = M
0; JMP

//============================================================
// ROTLN: Rotate Left (by N)
//============================================================
// Arguments......... 2: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 ROTLN(int16 data, int16 amount) {
//   for (int i = 0; i < amount; ++i) {
//     data = ROTL(data);
//   }

//   return data
// }
//------------------------------------------------------------

(ROTLN)
@15             // amount = amount % 15
D = A
@ROTLN.2
M = M & D

(ROTLN_DO)
@ROTLN.1        // Load ROTL arg
D = M
@ROTL.1
M = D

@RET_ROTL_ROTLN // Load RA
D = A
@ROTL.0
M = D

@ROTL           // Call ROTLR
0; JMP
(RET_ROTL_ROTLN)

@ROTL.1         // data = ROTL(data)
D = M
@ROTLN.1
M = D

@ROTLN.2         // --amount
M = M - 1

D = M
@ROTLN_END
D; JEQ          // if (amount == 0)

@ROTLN_DO
0; JMP

(ROTLN_END)

@ROTLN.0      // return to address
A = M
0; JMP

//============================================================
// ROTRN: Rotate Right (by N)
//============================================================
// Arguments......... 2: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 ROTRN(int16 data, int16 amount) {
//   for (int i = 0; i < amount; ++i) {
//     data = ROTR(data);
//   }

//   return data
// }
//------------------------------------------------------------

(ROTRN)
@15             // amount = amount % 15
D = A
@ROTRN.2
M = M & D

(ROTRN_DO)
@ROTRN.1        // Load ROTR arg
D = M
@ROTR.1
M = D

@RET_ROTR_ROTRN // Load RA
D = A
@ROTR.0
M = D

@ROTR           // Call ROTRR
0; JMP
(RET_ROTR_ROTRN)

@ROTR.1         // data = ROTR(data)
D = M
@ROTRN.1
M = D

@ROTRN.2         // --amount
M = M - 1

D = M
@ROTRN_END
D; JEQ          // if (amount == 0)

@ROTRN_DO
0; JMP

(ROTRN_END)

@ROTRN.0
A = M
0; JMP

//============================================================
// ROTN: Rotate (by N)
//============================================================
// Arguments......... 1: data, amount
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 ROTN(int16 data, amount) {
//   if (amount >= 0) {
//     ROTRN(data, amount);
//   } else {
//     ROTLN(data, amount);
//   }
// }
//------------------------------------------------------------

(ROTN)

@ROTN.1
D = M
@ROTN_IF_NEG   // if (data >= 0)
D; JLT

@ROTN.1        // Argument 1 (data value)
D = M
@ROTRN.1
M = D
@ROTN.2        // Argument 2 (shift/rotate amount)
D = M
@ROTRN.2
M = D

@RET_ROTRN_ROTN // Load RA
D = A
@ROTRN.0
M = D
@ROTRN         // Call subroutine
0; JMP
(RET_ROTRN_ROTN)

@ROTRN.1       // Store returned value
D = M
@ROTN.1
M = D

@ROTN_IF_NEG_END
0; JMP
(ROTN_IF_NEG)

@ROTN.1        // Argument 1 (data value)
D = M
@ROTLN.1
M = D
@ROTN.2        // Argument 2 (shift/rotate amount)
D = -M
@ROTLN.2
M = D

@RET_ROTLN_ROTN // Load RA
D = A
@ROTLN.0
M = D
@ROTLN         // Call subroutine
0; JMP
(RET_ROTLN_ROTN)

@ROTLN.1       // Store returned value
D = M
@ROTN.1
M = D
(ROTN_IF_NEG_END)

@ROTN.0
A = M
0; JMP

@ROTN.0
A = M
0; JMP

//****************** END OF STUDENT CODE *********************

//============================================================
// MAIN SUBROUTINE
//============================================================
// Arguments......... NONE
// Return values..... NONE
// Local variables... NONE
// Global variables.. R14: number of tests completed.
//------------------------------------------------------------
// The test script will initialize memory locations starting
// at address 101 with the test values. The MAIN subroutine
// passes these to the appropriate subroutines and then places
// the value returned into memory locations starting at
// address 201.
//
// For diagnostic purposes, R14 is used to count how many
// subroutines were returned from. It should end up being 13.
//------------------------------------------------------------
// Equivalent High Level code:
//
// void main(void)
// {
//    tests = 0;
//
//    M[201] = SLL(M[101]); tests++;
//    M[202] = SLR(M[103]); tests++;
//    M[203] = SLLN(M[104], M[105]); tests++;
//    M[204] = SLRN(M[106], M[107]); tests++;
//    M[205] = SLN(M[107], M[108]); tests++;
//    M[206] = SAR(M[109]); tests++;
//    M[207] = SARN(M[110], M[111]); tests++;
//    M[208] = SAN(M[112], M[113]); tests++;
//    M[209] = ROTL(M[114]); tests++;
//    M[210] = ROTR(M[115]); tests++;
//    M[211] = ROTLN(M[116], M[117]); tests++;
//    M[212] = ROTRN(M[118], M[119]); tests++;
//    M[213] = ROTN(M[120], M[121]); tests++;
//
//    return;
// }
//------------------------------------------------------------

(MAIN)

//------------------------------------------------------
// INITIALIZATION
//------------------------------------------------------

@R14               // tests = 0;
M = 0

//------------------------------------------------------
// Test SLL           M[201] = SLL(M[101])
//------------------------------------------------------

@101               // Argument 1 (data value)
D = M
@SLL.1
M = D

@RET_SLL           // Load RA
D = A
@SLL.0
M = D

@SLL               // Call subroutine
0; JMP
(RET_SLL)

@SLL.1             // Store returned value in output array
D = M
@201
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SLR           M[202] = SLR(M[103])
//------------------------------------------------------

@102               // Argument 1 (data value)
D = M
@SLR.1
M = D

@RET_SLR           // Load RA
D = A
@SLR.0
M = D

@SLR               // Call subroutine
0; JMP
(RET_SLR)

@SLR.1             // Store returned value in output array
D = M
@202
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SLLN          M[203] = SLLN(M[104], M[105])
//------------------------------------------------------

@103               // Argument 1 (data value)
D = M
@SLLN.1
M = D

@104               // Argument 2 (shift/rotate amount)
D = M
@SLLN.2
M = D

@RET_SLLN          // Load RA
D = A
@SLLN.0
M = D

@SLLN              // Call subroutine
0; JMP
(RET_SLLN)

@SLLN.1            // Store returned value in output array
D = M
@203
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SLRN          M[204] = SLRN(M[106], M[107])
//------------------------------------------------------

@105               // Argument 1 (data value)
D = M
@SLRN.1
M = D

@106               // Argument 2 (shift/rotate amount)
D = M
@SLRN.2
M = D

@RET_SLRN          // Load RA
D = A
@SLRN.0
M = D

@SLRN              // Call subroutine
0; JMP
(RET_SLRN)

@SLRN.1            // Store returned value in output array
D = M
@204
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SLN           M[205] = SLN(M[107], M[108])
//------------------------------------------------------

@107               // Argument 1 (data value)
D = M
@SLN.1
M = D

@108               // Argument 2 (shift/rotate amount)
D = M
@SLN.2
M = D

@RET_SLN           // Load RA
D = A
@SLN.0
M = D

@SLN               // Call subroutine
0; JMP
(RET_SLN)

@SLN.1             // Store returned value in output array
D = M
@205
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SAR           M[206] = SAR(M[109])
//------------------------------------------------------

@109               // Argument 1 (data value)
D = M
@SAR.1
M = D

@RET_SAR           // Load RA
D = A
@SAR.0
M = D

@SAR               // Call subroutine
0; JMP
(RET_SAR)

@SAR.1             // Store returned value in output array
D = M
@206
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SARN          M[207] = SARN(M[110], M[111])
//------------------------------------------------------

@110               // Argument 1 (data value)
D = M
@SARN.1
M = D

@111               // Argument 2 (shift/rotate amount)
D = M
@SARN.2
M = D

@RET_SARN          // Load RA
D = A
@SARN.0
M = D

@SARN              // Call subroutine
0; JMP
(RET_SARN)

@SARN.1            // Store returned value in output array
D = M
@207
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test SAN           M[208] = SAN(M[112], M[113])
//------------------------------------------------------

@112               // Argument 1 (data value)
D = M
@SAN.1
M = D

@113               // Argument 2 (shift/rotate amount)
D = M
@SAN.2
M = D

@RET_SAN           // Load RA
D = A
@SAN.0
M = D

@SAN               // Call subroutine
0; JMP
(RET_SAN)

@SAN.1             // Store returned value in output array
D = M
@208
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test ROTL          M[209] = ROTL(M[114])
//------------------------------------------------------

@114               // Argument 1 (data value)
D = M
@ROTL.1
M = D

@RET_ROTL          // Load RA
D = A
@ROTL.0
M = D

@ROTL              // Call subroutine
0; JMP
(RET_ROTL)

@ROTL.1            // Store returned value in output array
D = M
@209
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test ROTR          M[210] = ROTR(M[115])
//------------------------------------------------------

@115               // Argument 1 (data value)
D = M
@ROTR.1
M = D

@RET_ROTR          // Load RA
D = A
@ROTR.0
M = D

@ROTR              // Call subroutine
0; JMP
(RET_ROTR)

@ROTR.1            // Store returned value in output array
D = M
@210
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test ROTLN         M[211] = ROTLN(M[116], M[117])
//------------------------------------------------------

@116               // Argument 1 (data value)
D = M
@ROTLN.1
M = D

@117               // Argument 2 (shift/rotate amount)
D = M
@ROTLN.2
M = D

@RET_ROTLN         // Load RA
D = A
@ROTLN.0
M = D

@ROTLN             // Call subroutine
0; JMP
(RET_ROTLN)

@ROTLN.1           // Store returned value in output array
D = M
@211
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test ROTRN         M[212] = ROTRN(M[118], M[119])
//------------------------------------------------------

@118               // Argument 1 (data value)
D = M
@ROTRN.1
M = D

@119               // Argument 2 (shift/rotate amount)
D = M
@ROTRN.2
M = D

@RET_ROTRN         // Load RA
D = A
@ROTRN.0
M = D

@ROTRN             // Call subroutine
0; JMP
(RET_ROTRN)

@ROTRN.1           // Store returned value in output array
D = M
@212
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// Test ROTN          M[213] = ROTN(M[120], M[121])
//------------------------------------------------------

@120               // Argument 1 (data value)
D = M
@ROTN.1
M = D

@121               // Argument 2 (shift/rotate amount)
D = M
@ROTN.2
M = D

@RET_ROTN          // Load RA
D = A
@ROTN.0
M = D

@ROTN              // Call subroutine
0; JMP
(RET_ROTN)

@ROTN.1            // Store returned value in output array
D = M
@213
M = D

@R14               // tests++;
M = M+1

//------------------------------------------------------
// END OF TESTS
//------------------------------------------------------

@MAIN.0            // Return
A=M
0; JMP

//============================================================
