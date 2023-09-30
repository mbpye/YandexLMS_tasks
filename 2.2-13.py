elf_number = input()
gnome_number = input()
human_number = input()

if len(elf_number) == len(gnome_number) == len(human_number) == 2:
    unified_digit = str(int(elf_number[0]) + int(gnome_number[0]) + int(human_number[0]))
    
    print(int(int(unified_digit) / 3))
else:
    print("")
