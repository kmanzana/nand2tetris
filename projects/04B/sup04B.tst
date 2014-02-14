//============================================================
// USERID:........ kmanzana
// PROGRAMMER:.... Manzanares, Kelton M.
// COURSE:........ CSCI-410
// TERM:.......... SP14
// PROJECT:....... 04B
// FILENAME:...... sup04B.tst
//============================================================

load sup04B.asm,
output-file sup04B.out;

// Wait for Bootstrap code to initialize software trap
while RAM[15]=0 {
  ticktock;
}

set RAM[101]  32103,   // SLL   data
set RAM[102]   5533,   // SLR   data
set RAM[103] -27297,   // SLLN  data
set RAM[104]      5,   // SLLN  shift amount
set RAM[105]  -6819,   // SLRN  data
set RAM[106]      3,   // SLRN  shift amount
set RAM[107]  -4167,   // SLN   data
set RAM[108]     -2,   // SLN   shift amount
set RAM[109] -17061,   // SAR   data
set RAM[110] -17578,   // SARN  data
set RAM[111]      6,   // SARN  shift amount
set RAM[112]  -5321,   // SAN   data
set RAM[113]     -2,   // SAN   shift amount
set RAM[114]  -8329,   // ROTL  data
set RAM[115] -27139,   // ROTR  data
set RAM[116] -10825,   // ROTLN data
set RAM[117]    171,   // ROTLN rotate amount
set RAM[118]  23513,   // ROTRN data
set RAM[119]   1613,   // ROTRN rotate amount
set RAM[120]  30077,   // ROTN  data
set RAM[121] -19759;   // ROTN  rotate amount -19759

while RAM[15]<>0 {
  ticktock;
}
echo "Simulation Halted normally",

output-list time%S1.5.1,
output;

compare-to sup04B.cmp,

output-list
RAM[201]%X2.4.2  // SLL
RAM[202]%X2.4.2  // SLR
RAM[203]%X2.4.2  // SLLN
RAM[204]%X2.4.2  // SLRN
RAM[205]%X2.4.2  // SLN
RAM[206]%X2.4.2  // SAR
RAM[207]%X2.4.2  // SARN
RAM[208]%X2.4.2  // SAN
RAM[209]%X2.4.2  // ROTL
RAM[210]%X2.4.2  // ROTR
RAM[211]%X2.4.2  // ROTLN
RAM[212]%X2.4.2  // ROTRN
RAM[213]%X2.4.2, // ROTN

output;
