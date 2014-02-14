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
