'''
def lstr_list(string):
    line = ""
    final_list = []
    switch = 'off'
    for val in string:

        if val == "'" and switch == 'off':
            switch == 'on' 


        if val == "'" and switch == 'on':
            switch = 'off'
            final_list.append(line)
            return line
            line = ""

        if val != "'" and switch == 'off':
            pass

        if val != "'" and switch == 'on':
            line.append(val)
            print(line)

    return line 

        

print(lstr_list("['kop' , 'pop' , 'cop']")) 
'''

'''
string = "['kop' , 'pop' , 'cop']"
line = ""
final_list = []
switch = 'off'
for val in string:

    if val == "'" and switch == 'off':
        switch ='on' 


    if val == "'" and switch == 'on':
        switch = 'off'
        final_list.append(line)
        print(line , 'dasj')
        line = ""

    if val != "'" and switch == 'off':
        pass

    if val != "'" and switch == 'on':
        line = line + val
        print(line , 'hash')

print(final_list)

'''

def lstr_list(string):
    line = ""
    final_list = []
    switch = 'off'

    for val in string:
        if val == "'" and switch == 'off':
            switch = 'on'  # Corrected assignment operator

        elif val == "'" and switch == 'on':
            switch = 'off'
            final_list.append(line)
            line = ""

        elif val != "'" and switch == 'on':
            line += val  # Corrected to concatenate characters

    return final_list
            



