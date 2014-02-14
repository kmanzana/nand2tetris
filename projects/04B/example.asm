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
//------------------------------------------------------------
// High Level Language Equivalant
//
// int16 SLR(int16 data) {
// }

(SLR)
// set ROTLN arg
@SLR.1
D = M
@ROTLN.1
M = D
// want to rotate 15 times
@15
D = A
@ROTLN.2
M = D
// set return address
@SLR_END
D = A
@ROTLN.0
M = D
// call ROTLN
@ROTLN
0; JMP

(SLR_END)
// make mask
@32767
D = A
// mask away MSB
@ROTLN.1
D = D & M
// set return value and return
@SLR.1
M = D
@SLR.0
A = M
0; JMP



//------------------------------------------------------------


//============================================================
// SLLN: Shift Logical Left (by N)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(SLLN)
// call to mod
//@SLLN.2
//D = M
//@MOD1
//M = D
//@16
//D = A
//@MOD2
//M = D
//@SLLN_MOD_RETURN
//D = A
//@MOD.O
//M = D
//(SLLN_MOD_RETURN)
//@MOD.1
//D = M
//@SLLN1
//M = D
// move args to correct places to call SLL
// move arg to shift
@SLLN.1
D = M
@SLL.1
M = D
// load return address
@SLLN_LOOP
D = A
@SLL.0
M = D


(SLLN_LOOP)
// jump to end if shift amount == 0
@SLLN.2
D = M
@SLLN_END
D;JEQ
// otherwise...
// decrement shift amount
@SLLN.2
M = M - 1
@SLL
0;JMP


(SLLN_END)
// move arg back to correct place
@SLL.1
D = M
@SLLN.1
M = D
// jump to return
@SLLN.0
A = M
0;JMP

//============================================================
// SLRN: Shift Logical Right (by N)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(SLRN)
// calculate how many times to ROTL
@16
D = A
@SLRN.2
MD = D - M // store back into SLRN.2 for later use
// move N to ROTLN
@ROTLN.2
M = D
// move arg to ROTLN
@SLRN.1
D = M
@ROTLN.1
M = D
// set return address
@SLRN_BUILD_MASK
D = A
@ROTLN.0
M = D
// call ROTLN
@ROTLN
0; JMP

(SLRN_BUILD_MASK)
@R0
M = 0

(SLRN_LOOP)
@SLRN.2
D = M
@SLRN_END
D; JEQ
// decrement
@SLRN.2
M = M - 1
// otherwise
@R0
D = M
M = D + M
M = M + 1
@SLRN_LOOP
0; JMP


(SLRN_END)
@R0
D = M
@ROTLN.1
D = D & M
@SLRN.1
M = D
// jump to return
@SLRN.0
A = M
0;JMP

//============================================================
// SLN:
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(SLN)
// create mask
@32767
D = !A
// check if SLN.2 < 0
@SLN.2
D = D & M
// shift right if positive
@SLN_POSITIVE
D; JEQ
// else shift left

(SLN_NEGATIVE)
// flip sign
@SLN.2
D = M
@SLLN.2
M = -D
// set arg
@SLN.1
D = M
@SLLN.1
M = D
// set return address
@SLN_NEG_RETURN
D = A
@SLLN.0
M = D
// call SLLN
@SLLN
0; JMP

(SLN_POSITIVE)
// set arg
@SLN.1
D = M
@SLRN.1
M = D
// set N
@SLN.2
D = M
@SLRN.2
M = D
// set return address
@SLN_POS_RETURN
D = A
@SLRN.0
M = D
// call
@SLRN
0; JMP

(SLN_NEG_RETURN)
// get value
@SLLN.1
D = M
@SLN.1
M = D
// return
@SLN.0
A = M
0;JMP

(SLN_POS_RETURN)
// get value
@SLRN.1
D = M
@SLN.1
M = D
// return
@SLN.0
A = M
0;JMP

//============================================================
// SAR: Shift Arithmetic Right (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(SAR)
// load SLR arg
@SAR.1
D = M
@SLR.1
M = D
// set return address
@SAR_END
D = A
@SLR.0
M = D
// create mask
@32767
D = !A
// get MSB
@SAR.1
M = M & D // store MSB to SAR.1
// call SLR
@SLR
0; JMP

(SAR_END)
// add MSB back to result
@SLR.1
D = M
@SAR.1
M = M | D
// return
@SAR.0
A = M
0;JMP



//============================================================
// SARN: Shift Arithmetic Right (by N)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------


(SARN)
// set SAR arg
@SARN.1
D = M
@SAR.1
M = D
// set return address
@SARN_LOOP
D = A
@SAR.0
M = D

(SARN_LOOP)
// get N
@SARN.2
D = M
@SARN_END
D; JEQ
// decrement
@SARN.2
M = M - 1
// call SAR
@SAR
0; JMP

(SARN_END)
// move result
@SAR.1
D = M
@SARN.1
M = D
// return
@SARN.0
A = M
0;JMP

//============================================================
// SAN:
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------


(SAN)
// create mask
@32767
D = !A
// check if SAN.2 < 0
@SAN.2
D = D & M
// shift right if positive
@SAN_POSITIVE
D; JEQ
// else shift left

(SAN_NEGATIVE)
// flip sign
@SAN.2
D = M
@SLLN.2
M = -D
// set arg
@SAN.1
D = M
@SLLN.1
M = D
// set return address
@SAN_NEG_RETURN
D = A
@SLLN.0
M = D
// call SLLN
@SLLN
0; JMP

(SAN_POSITIVE)
// set arg
@SAN.1
D = M
@SARN.1
M = D
// set N
@SAN.2
D = M
@SARN.2
M = D
// set return address
@SAN_POS_RETURN
D = A
@SARN.0
M = D
// call
@SARN
0; JMP

(SAN_NEG_RETURN)
// get value
@SLLN.1
D = M
@SAN.1
M = D
// return
@SAN.0
A = M
0;JMP

(SAN_POS_RETURN)
// get value
@SARN.1
D = M
@SAN.1
M = D
// return
@SAN.0
A = M
0;JMP



//============================================================
// ROTL: Rotate Left (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(ROTL)
// create mask
@32767
D = !A
@R0
M = D
// get MSB
@ROTL.1
D = M
@R0
D = D & M
// store to R1
@R1
M = D
// SLL
@ROTL.1
D = M
D = M + D
// store
M = D
// check if should add 1
@R1
D = M
@ROTL_END
D; JEQ
@ROTL.1
M = M + 1

(ROTL_END)
@ROTL.0
A = M
0;JMP

//============================================================
// ROTR: Rotate Right (by 1)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------


(ROTR)
// set ROTLN args
// N
@15
D = A
@ROTLN.2
M = D
// arg
@ROTR.1
D = M
@ROTLN.1
M = D
// return address
@ROTR_END
D = A
@ROTLN.0
M = D
// call
@ROTLN
0; JMP


(ROTR_END)
// move result
@ROTLN.1
D = M
@ROTR.1
M = D
// return
@ROTR.0
A = M
0;JMP

//============================================================
// ROTLN: Rotate Left (by N)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(ROTLN)
// N % 16 to eliminate unnecessary rotate cycles
@16
D = A
@MOD.2
M = D
@ROTLN.2
D = M
@MOD.1
M = D
@ROTLN_MOD_RETURN
D = A
@MOD.0
M = D
@MOD
0; JMP
(ROTLN_MOD_RETURN)
@MOD.1
D = M
@ROTLN.2
M = D
// load ROTL arg
@ROTLN.1
D = M
@ROTL.1
M = D
// load ROTL return address
@ROTLN_LOOP
D = A
@ROTL.0
M = D




(ROTLN_LOOP)
// jump to end if rotate amount == 0
@ROTLN.2
D = M
@ROTLN_END
D; JEQ
// otherwise
// decrement count
@ROTLN.2
M = M - 1
// call ROTL
@ROTL
0; JMP




(ROTLN_END)
// move ROTL to ROTLN
@ROTL.1
D = M
@ROTLN.1
M = D
@ROTLN.0
A = M
0;JMP

//============================================================
// ROTRN: Rotate Right (by N)
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------


(ROTRN)
// mod to ensure works right
@16
D = A
@MOD.2
M = D
@ROTRN.2
D = M
@MOD.1
M = D
@ROTRN_MOD_RET
D = A
@MOD.0
M = D
@MOD
0; JMP
(ROTRN_MOD_RET)
@MOD.1
D = M
@ROTRN.2
M = D
// set N
@16
D = A
@ROTRN.2
D = D - M
@ROTLN.2
M = D
// set arg
@ROTRN.1
D = M
@ROTLN.1
M = D
// set return address
@ROTRN_END
D = A
@ROTLN.0
M = D
// call
@ROTLN
0;JMP

(ROTRN_END)
// move return value
@ROTLN.1
D = M
@ROTRN.1
M = D
// return
@ROTRN.0
A = M
0;JMP

//============================================================
// ROTN:
//============================================================
// Arguments......... 1: data
// Return values..... 1: result
// Local variables... NONE
// Global variables.. NONE
//------------------------------------------------------------
//------------------------------------------------------------
// High Level Language Equivalant
//
//------------------------------------------------------------

(ROTN)
// create mask
@32767
D = !A
// check if ROTN.2 < 0
@ROTN.2
D = D & M
// shift right if positive
@ROTN_POSITIVE
D; JEQ
// else shift left

(ROTN_NEGATIVE)
// flip sign
@ROTN.2
D = M
@ROTLN.2
M = -D
// set arg
@ROTN.1
D = M
@ROTLN.1
M = D
// set return address
@ROTN_NEG_RETURN
D = A
@ROTLN.0
M = D
// call ROTLN
@ROTLN
0; JMP

(ROTN_POSITIVE)
// set arg
@ROTN.1
D = M
@ROTRN.1
M = D
// set N
@ROTN.2
D = M
@ROTRN.2
M = D
// set return address
@ROTN_POS_RETURN
D = A
@ROTRN.0
M = D
// call
@ROTRN
0; JMP

(ROTN_NEG_RETURN)
// get value
@ROTLN.1
D = M
@ROTN.1
M = D
// return
@ROTN.0
A = M
0;JMP

(ROTN_POS_RETURN)
// get value
@ROTRN.1
D = M
@ROTN.1
M = D
// return
@ROTN.0
A = M
0;JMP







// mod
// mod.1 % mod.2

(MOD)
@MOD.1
D = M

(MOD_LOOP)
@MOD.2
D = D - M
@MOD_END
D; JLT
@MOD.1
M = D
@MOD_LOOP
0; JMP

(MOD_END)
@MOD.0
A = M
0;JMP












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
