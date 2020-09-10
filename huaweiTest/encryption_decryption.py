#coding:utf-8

class Encrytion_decryption:

  def letter_encryption(self,letter):
    """对字母的加密"""
    if letter.islower():
        if letter=="z":
            letter="A"
        else:
            letter=chr(ord(letter)+1).upper()
    else:
        if letter=="Z":
            letter="a"
        else:
            letter=chr(ord(letter)+1).lower()
    return letter


  def letter_decryption(self,letter):
      """对字母的解密方法"""
      if letter.islower():
          if letter == "a":
              letter = "Z"
          else:
              letter = chr(ord(letter) - 1).upper()
      else:
          if letter == "A":
              letter = "z"
          else:
              letter = chr(ord(letter) - 1).lower()
      return letter

  def digit_encryption(self,num):
      """对数字的加密方法"""
      if num==9:
          num_input=0
      else:
          num_input=num+1
      return num_input

  def digit_decryption(self,num):
      """对数字的解密方法"""
      if num==0:
          num_input=9
      else:
          num_input=num-1
      return num_input

if __name__=="__main__":
    Encrytion_decryption=Encrytion_decryption()
    print(Encrytion_decryption.letter_encryption("Z"))
    print(Encrytion_decryption.digit_decryption(5))
