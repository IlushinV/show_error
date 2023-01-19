import easygui

while True:
    with open(r'C:\Users\v.ilushin\AppData\Roaming\ATOL\drivers10\logs\fptr10.log', encoding="utf8") as txt:
        list_of_lines = txt.readlines()
    for line in list_of_lines:
        pass
    if "ERROR" in line.split(" "):
        easygui.msgbox(line, title="ERROR")

    print(line)


