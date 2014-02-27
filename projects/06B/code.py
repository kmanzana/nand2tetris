#============================================================
# USERID:......... KMANZANA
# PROGRAMMER:..... Manzanares, Kelton M.
# COURSE:......... CSCI-410
# TERM:........... SP14
# PROJECT:........ 06B
# FILENAME:....... code.py
# PYTHON VERSION:. 2.7.2
#============================================================

class Code:
  @staticmethod
  def dest(command):
    A = '1' if 'A' in command else '0'
    D = '1' if 'D' in command else '0'
    M = '1' if 'M' in command else '0'

    return A + D + M

  @staticmethod
  def comp(command):
    if command[0] == 'X':
      return Code.xhh_type(command)
    else:
      a = '1' if 'M' in command else '0'

      return a + {
        '0':   '101010',
        '1':   '111111',
        '-1':  '111010',
        'D':   '001100',
        'A':   '110000',
        'M':   '110000',
        '!D':  '001101',
        '!A':  '110001',
        '!M':  '110001',
        '-D':  '001111',
        '-A':  '110011',
        '-M':  '110011',
        'D+1': '011111',
        'A+1': '110111',
        'M+1': '110111',
        'D-1': '001110',
        'A-1': '110010',
        'M-1': '110010',
        'D+A': '000010',
        'D+M': '000010',
        'D-A': '010011',
        'D-M': '010011',
        'A-D': '000111',
        'M-D': '000111',
        'D&A': '000000',
        'D&M': '000000',
        'D|A': '010101',
        'D|M': '010101'
      }[command]

  @staticmethod
  def xhh_type(command):
    bin = '{:0>8b}'.format(int(command[1:3], 16))

    if bin[0] == '0':
      return bin[1:8]
    else:
      print 'Invalid XHH instruction: {}. Exiting...'.format(command)

      exit()

  @staticmethod
  def jump(command):
    return {
      '':    '000',
      'JGT': '001',
      'JEQ': '010',
      'JGE': '011',
      'JLT': '100',
      'JNE': '101',
      'JLE': '110',
      'JMP': '111'
    }[command]
