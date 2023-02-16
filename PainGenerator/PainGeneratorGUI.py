from PIL import Image, ImageDraw, ImageFont
from nltk.tokenize import word_tokenize
import PySimpleGUI as sg
import colorsys
import numpy as np
import os.path
import random, re, sys

#Set program path and theme
c_path = sys.path[0]
theme = sg.theme('DarkPurple5')
word = 'None'
color1 = None
color2 = None
random_file_number = None
#warnings.filterwarnings('ignore')

#simple code to check if given hex code is valid
def isValidHexaCode(str):
    regex = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    p = re.compile(regex)
    if(str == None):
        return False
    if (re.search(p, str)):
        return True
    else:
        return False

#Hex to RGB converter
def hex_to_rgb(hex):
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

#GUI Layout
lower, upper = 1, 100
data = [i for i in range(lower - 1, upper + 2)]

layout_l = [[sg.Checkbox('Random/User Generated', default=False, key='-CHECKBOX-', enable_events=True)],
            [sg.Input(key='-WORD-', disabled=True, size=20), sg.Text('Word')],
            [sg.Input(key='-HEX1-', disabled=True, size=10), sg.Text('Hex Value 1'), sg.Input(key='-HEX2-', disabled=True, size=10), sg.Text('Hex Value 2'), sg.Button(button_text='Reset Hex', key='-RESETHEX-')],
            [sg.Spin(data, initial_value=lower, key='-SPIN-', enable_events=True, tooltip='1 to 100', size=(4)), sg.Text('How many images would you like to generate?')],
            [sg.Text('Output Folder')],
            [sg.InputText(c_path+'/results/', key='-FOLDER-'), sg.FolderBrowse()], 
            [sg.Text(' ')],
            [sg.Button('GENERATE', key='-GENERATE-', button_color=('black', '#01d28e'), size=(25))]
            ]

layout_r = [[sg.Column([[sg.Image(c_path+"/resources/PAIN.png", key='-IMAGE-')]], justification='right')],
            [sg.Push(),sg.Text('WORDLIST:'), sg.Combo(values=('Cyberpunk AF', 'TempleOS', '1894'), default_value='Cyberpunk AF', key='-WORDLIST-', auto_size_text=True, readonly=True)],
            [sg.Text(' ')], 
            [sg.Button('EXIT', button_color=('black', '#01d28e'), size=25)],
            ]
            

layout = [[sg.Col(layout_l, p=0), sg.Col(layout_r, p=0, expand_y=1, expand_x=0)]]

# Create the Window
window = sg.Window('PAIN GENERATOR v1.00', layout, use_custom_titlebar=False, icon=c_path+'/resources/PAIN.ico',finalize=True, keep_on_top=True, grab_anywhere=True, element_padding=3)


# Event Loop
while True:
    
    event, values = window.read()# type: ignore
    
    #Close window or exit
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break

    #Collect variables
    savepath = values['-FOLDER-']
    chosen_wordlist = values['-WORDLIST-']
    hex1 = values['-HEX1-']
    hex2 = values['-HEX2-']
    
    #Spin wrap around 
    if event == '-SPIN-':
        value = values['-SPIN-']
        if value == lower - 1:
            window['-SPIN-'].update(value=upper)
            values['-SPIN-'] = upper        # Change the values dictionary too so it'll be correct if used
        elif value == upper + 1:
            window['-SPIN-'].update(value=lower)

    #Checkbox Check
    elif values['-CHECKBOX-'] == True:
        
        window['-SPIN-'].Widget.configure(state="disabled")# type: ignore
        window['-SPIN-'].Update(1)# type: ignore
        
        window['-WORD-'].Widget.configure(state="normal")# type: ignore
        window['-WORD-'].Update('PAIN')# type: ignore
        
        window['-HEX1-'].Widget.configure(state="normal")# type: ignore
        window['-HEX1-'].Update('#FF0000')# type: ignore
        window['-HEX2-'].Widget.configure(state="normal")# type: ignore
        window['-HEX2-'].Update('#0000FF')# type: ignore
            
    elif values['-CHECKBOX-'] == False:
        
        window['-SPIN-'].Widget.configure(state="normal")# type: ignore
        
        window['-WORD-'].Widget.configure(state="disabled")# type: ignore
        window['-WORD-'].Update('')# type: ignore
        
        window['-HEX1-'].Widget.configure(state="disabled")# type: ignore
        window['-HEX1-'].Update('')# type: ignore
        window['-HEX2-'].Widget.configure(state="disabled")# type: ignore
        window['-HEX2-'].Update('')# type: ignore
        
    #Reset Hex on User's demande
    if event == '-RESETHEX-' and values['-CHECKBOX-'] == True:
        window['-HEX1-'].Update('#FF0000')# type: ignore
        window['-HEX2-'].Update('#0000FF')# type: ignore
        
        
    #Generate the pictures
    if event == '-GENERATE-':
        
        times_to_run = str(values['-SPIN-'])
        user_word = values['-WORD-']
        
        if times_to_run.isnumeric():
            
            times_to_run = int(times_to_run)
            
            if times_to_run < 1 or times_to_run > 100:
                sg.Popup('Number is too small or too large. Range = 1 -> 100', button_color=('black', '#01d28e'), keep_on_top=True, title="ERROR", icon=c_path+'/resources/PAIN.ico')
                window['-SPIN-'].update(value=lower)
            
            elif times_to_run > 1 or times_to_run < 100:
                #GENERATE THE PICTURES
                for i in range(times_to_run):
                    
                    #pick a word from the wordlist
                    if values['-CHECKBOX-'] == True: #Check checkbox value, True
                       
                        if len(user_word) < 2 or len(user_word) > 10: #If user word is too short or too long
                            sg.Popup('Word is too small or too large. Range = 2 -> 10 letters', button_color=('black', '#01d28e'), keep_on_top=True, title="ERROR", icon=c_path+'/resources/PAIN.ico') 
                            break
                        
                        elif len(values['-WORD-']) > 2 or len(values['-WORD-']) < 10: #If word is correct, set user word in uppercase and set user colors
                            word = user_word.upper()
                            
                            if isValidHexaCode(hex1) == True and isValidHexaCode(hex2) == True:
                                
                                window['-HEX1-'].Update(hex1)# type: ignore
                                window['-HEX2-'].Update(hex2)#type: ignore
                                window['-WORD-'].Update(word)# type: ignore
                                hex1 = hex1.strip('#')
                                hex2 = hex2.strip('#')
                                color1 = hex_to_rgb(hex1)
                                color2 = hex_to_rgb(hex2)
                            else:
                                window['-WORD-'].Update(word)# type: ignore
                                window['-HEX1-'].Update(hex1)# type: ignore
                                window['-HEX2-'].Update(hex2)#type: ignore
                                sg.Popup('Hex value is incorrect', button_color=('black', '#01d28e'), keep_on_top=True, title="ERROR", icon=c_path+'/resources/PAIN.ico')
                                break
                    
                    elif values['-CHECKBOX-'] == False: #Check checkbox value, False
                        
                        if chosen_wordlist == 'Cyberpunk AF':
                            wordlist = c_path+"/resources/SPRAWL.txt"
                        elif chosen_wordlist == 'TempleOS':
                            wordlist = c_path+"/resources/TempleOS.txt"
                        elif chosen_wordlist == '1894':
                            wordlist = c_path+"/resources/1894.txt"
    
                        wordlist = open(wordlist, encoding='UTF8')#type: ignore
                        wordlist = wordlist.read()
                        wordlist = word_tokenize(wordlist)
                        word = random.choice(wordlist)
                        
                        #Randomly generate a set of 2 colors in HSV, convert to RGB
                        (h1, s1, v1) = (random.random(), random.uniform(0.5, 1), random.uniform(0.7, 1))
                        (r1, g1, b1) = colorsys.hsv_to_rgb(h1, s1, v1)
                        (r1, g1, b1) = (int(r1 * 255), int(g1 * 255), int(b1 * 255))
                        color1 = (r1,g1,b1)
                        (h2, s2, v2) = (random.random(), random.uniform(0.5, 1), random.uniform(0.7, 1))
                        (r2, g2, b2) = colorsys.hsv_to_rgb(h2, s2, v2)
                        (r2, g2, b2) = (int(r2 * 255), int(g2 * 255), int(b2 * 255))
                        color2 = (r2,g2,b2)
                        
                    #Create transparent image for text to be applied on
                    txtimg = Image.new(mode='RGBA', size=(1024, 1024), color=(255, 255, 255, 0))

                    #Create Gradient
                    def get_gradient_2d(start, stop, width, height, is_horizontal):
                        if is_horizontal:
                            return np.tile(np.linspace(start, stop, width), (height, 1))
                        else:
                            return np.tile(np.linspace(start, stop, height), (width, 1)).T

                    def get_gradient_3d(width, height, start_list, stop_list, is_horizontal_list):
                        result = np.zeros((height, width, len(start_list)), dtype=np.cfloat)

                        for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
                            result[:, :, i] = get_gradient_2d(start, stop, width, height, is_horizontal)

                        return result

                    #Draw the gradient onto an image
                    array = get_gradient_3d(128, 128, (color1), (color2), (False, False, False))
                    img = Image.fromarray(np.uint8(array))

                    #Define word's length in the image, define font, define length of word
                    fontsize = 1
                    img_fraction = 1
                    font = ImageFont.truetype(c_path+"/resources/Envy Code R.ttf", fontsize)
                    fontlength = font.getlength(word) 
                    fontlength = str(fontlength)
                    fontlength = int(fontlength[0])

                    #Loop until word fills the box
                    while fontlength < img_fraction*txtimg.size[0]:
                        fontlength = font.getlength(word) 
                        fontsize += 1
                        font = ImageFont.truetype(c_path+"/resources/Envy Code R.ttf", fontsize)

                    #Draw text letter by letter
                    txtdraw = ImageDraw.Draw(txtimg)
                    left, top, total_word_width, total_world_height = txtdraw.textbbox((0,0),word,font=font) 
                    width_difference = 1024 - total_word_width
                    gap_width = int(width_difference / (len(word) + 1)) 
                    xpos = 0
                    for letter in word:
                        txtdraw.text((xpos, -0), letter, (0, 0, 0), font=font)
                        letter_left, letter_top, letter_width, letter_height = txtdraw.textbbox((-1,0),letter,font=font)
                        xpos += letter_width + gap_width

                    #Stretch the text image vertically, reposition it, according to the number of letters in the word (2 --> 10)
                    image_y = 128
                    if len(word) == 2: 
                        resize = txtimg.resize(size = (128, 160), resample=4)
                        croptest = resize.crop(box=(0, 24, 128, 152))
                        
                    elif len(word) == 3: 
                        resize = txtimg.resize(size = (128, 260), resample=4)
                        croptest = resize.crop(box=(0, 30, 128, 158))

                    elif len(word) == 4: 
                        resize = txtimg.resize(size = (128, 360), resample=4)
                        croptest = resize.crop(box=(0, 33, 128, 161))
                        
                    elif len(word) == 5: 
                        resize = txtimg.resize(size = (128, 460), resample=4)
                        croptest = resize.crop(box=(0, 36, 128, 164))

                    elif len(word) == 6: 
                        resize = txtimg.resize(size = (128, 560), resample=4)
                        croptest = resize.crop(box=(0, 37, 128, 165))
                        
                    elif len(word) == 7:  
                        resize = txtimg.resize(size = (128, 660), resample=4)
                        croptest = resize.crop(box=(0, 38, 128, 166))

                    elif len(word) == 8: 
                        resize = txtimg.resize(size = (128, 750), resample=4)
                        croptest = resize.crop(box=(0, 38, 128, 166))
                        
                    elif len(word) == 9:
                        resize = txtimg.resize(size = (128, 860), resample=4)
                        croptest = resize.crop(box=(0, 40, 128, 168))

                    else:
                        resize = txtimg.resize(size = (128, 960), resample=4)
                        croptest = resize.crop(box=(0, 40, 128, 168))

                    #Generate random number, convert gradient image to RGBA, composite both images, save final image
                    random_file_number = f'{random.randint(1, 999):03}'
                    imgRGBA = img.convert('RGBA')
                    composite = Image.alpha_composite(imgRGBA, croptest)
                    if os.path.exists(savepath) == True:   
                        composite.save(fp=savepath+'/'+word+'_'+random_file_number+".png", quality=95)
                    elif os.path.exists(savepath) == False:
                        sg.Popup('Savepath does not exist, file has been saved in the default results folder.', button_color=('black', '#01d28e'), keep_on_top=True, title="ERROR", icon=c_path+'/resources/PAIN.ico')
                        composite.save(fp=c_path+'/results/'+word+'_'+random_file_number+".png", quality=95)
                        window['-FOLDER-'].Update(c_path+'/results/')# type: ignore
                        window['-IMAGE-'].Update(c_path+'/results/'+word+'_'+random_file_number+".png")#type:ignore 
                    
                    #Stops user from crashing the program by inputting something invalid if the first image generated is custom
            if random_file_number is None:#type:ignore
                window['-IMAGE-'].Update(c_path+"/resources/PAIN.png")#type:ignore
            else:
                if os.path.exists(savepath+'/'+word+'_'+random_file_number+".png") == True:
                    window['-IMAGE-'].Update(savepath+'/'+word+'_'+random_file_number+".png")#type:ignore 
                    
                    #If spin is text = incorrect. Also, easter egg, shhhhh
        else:
            if times_to_run == 'CRUELTY SQUAD':
                sg.PopupYesNo(button_color=('black', '#01d28e'), keep_on_top=True, title="WHY ARE YOU HERE", icon=c_path+'/resources/PAIN.ico', image=c_path+'/resources/FACE.png')
                window['-IMAGE-'].Update(c_path+'/resources/FACE.png')#type:ignore 
                window['-SPIN-'].update(value=lower)
            else:    
                sg.Popup('Incorrect input.', button_color=('black', '#01d28e'), keep_on_top=True, title="ERROR", icon=c_path+'/resources/PAIN.ico')
                window['-SPIN-'].update(value=lower)
        
             
window.close()
