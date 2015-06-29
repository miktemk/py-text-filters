import sys, os, re
import time, datetime
import getopt
from filtersCommon import wholeWordOnly

# ============== DEBUG!!! ================
sys.argv = ['script', 'ruhist_better.txt']
# ============== DEBUG!!! ================


optlist, args = getopt.getopt(sys.argv[1:], "")

# read file lines
fname = args[0]
if not os.path.exists(fname):
	print("File does not exist!!")
	
infile = open(fname, encoding="utf8")
text = infile.read()
#lines = infile.readlines() ### or read everything into array of lines
infile.close()

# correct pronounciation
text = wholeWordOnly(text, "жили", "жили-жили-поживали")
text = wholeWordOnly(text, "I—II вв", "первому второму веку")
text = wholeWordOnly(text, "В VII-VIII веках", "В седьмом по восьмом веках")
text = wholeWordOnly(text, "в VIII-IX веках", "в восьмом по девятом веках")
text = wholeWordOnly(text, "В VIII — начале IX веков", "В восьмом и начале девятого веков")
text = wholeWordOnly(text, "в IX — начале X", "в девятом и начале десятого")
# [IVX]+ съезд
text = wholeWordOnly(text, "I съезд", "первый съезд")
text = wholeWordOnly(text, "XX съезде", "двадцатом съезде")
text = wholeWordOnly(text, "XX съезду", "двадцатому съезду")
text = wholeWordOnly(text, "XXI съезде", "двадцать первом съезде")
text = wholeWordOnly(text, "XXVII съезд", "двадцать седьмой съезд")
# [IVX]+ Всероссийск
text = wholeWordOnly(text, "II Всероссийском съезде", "втором Всероссийском съезде")
text = wholeWordOnly(text, "III Всероссийском съезде", "третьем Всероссийском съезде")
text = wholeWordOnly(text, "II Всесоюзный съезд Советов", "второй Всесоюзный съезд Советов")
# I, II, III, IV, V, VI, VII, VIII
text = wholeWordOnly(text, "Петр I", "Петр первый")
text = wholeWordOnly(text, "Петра I", "Петра первого")
text = wholeWordOnly(text, "Петре I", "Петра первом")
text = wholeWordOnly(text, "Петра II", "Петра второго")
text = wholeWordOnly(text, "Екатерины I", "Екатерины первой")
text = wholeWordOnly(text, "Павел I", "Павел первый")
text = wholeWordOnly(text, "Павла I", "Павла первого")
text = wholeWordOnly(text, "Павле I", "Павле первом")
text = wholeWordOnly(text, "Александр I", "Александр первый")
text = wholeWordOnly(text, "Александра I", "Александра первого")
text = wholeWordOnly(text, "Наполеон I", "Наполеон первый")
text = wholeWordOnly(text, "Николай I", "Николай первый")
text = wholeWordOnly(text, "Николаю I", "Николаю первому")
text = wholeWordOnly(text, "Николая I", "Николая первого")
text = wholeWordOnly(text, "Ивана I", "Ивана первого")
text = wholeWordOnly(text, "Петр III", "Петр третий")
text = wholeWordOnly(text, "Петра III", "Петра третьего")
text = wholeWordOnly(text, "Петром III", "Петра третьим")
text = wholeWordOnly(text, "Фридрихом II", "Фридрихом вторым")
text = wholeWordOnly(text, "Екатерина II", "Екатерина вторая")
text = wholeWordOnly(text, "Екатерины II", "Екатерины второй")
text = wholeWordOnly(text, "Екатерине II", "Екатерине второй")
text = wholeWordOnly(text, "Ираклий II", "Ираклий второй")
text = wholeWordOnly(text, "Александр II", "Александр второй")
text = wholeWordOnly(text, "Александра II", "Александра второго")
text = wholeWordOnly(text, "Александр III", "Александр третий")
text = wholeWordOnly(text, "Александра III", "Александра третьего")
text = wholeWordOnly(text, "Николай II", "Николай второй")
text = wholeWordOnly(text, "Николая II", "Николая второго")
text = wholeWordOnly(text, "Лжедмитрий II", "Лжедмитрий второй")
text = wholeWordOnly(text, "Лжедмитрия II", "Лжедмитрия второго")
text = wholeWordOnly(text, "II Государственную думу", "вторую Государственную думу")
text = wholeWordOnly(text, "Иване III", "Иване третьем")
text = wholeWordOnly(text, "Василия III", "Василия третьего")
text = wholeWordOnly(text, "Сигиз-мунд III", "Сигизмунд третий")
text = wholeWordOnly(text, "Сигиз-мунд III", "Сигиз-мунд третий")
text = wholeWordOnly(text, "Сигизмунда III", "Сигизмунда третьего")
text = wholeWordOnly(text, "Иван IV", "Иван четвертый")
text = wholeWordOnly(text, "Ивана IV", "Ивана четвертого")
text = wholeWordOnly(text, "Иваном IV", "Иваном четвертым")
text = wholeWordOnly(text, "Ивану IV", "Ивану четвертому")
text = wholeWordOnly(text, "Иваном VI", "Иваном шестым")

text = wholeWordOnly(text, "", "")
text = wholeWordOnly(text, "", "")
text = wholeWordOnly(text, "", "")
text = wholeWordOnly(text, "", "")
text = wholeWordOnly(text, "", "")
text = wholeWordOnly(text, "", "")
text = wholeWordOnly(text, "", "")

# write to file
filename, fileExtension = os.path.splitext(fname)
fff = open(filename + "2.txt", "w", encoding="utf8")	
fff.write(text)
fff.close()
