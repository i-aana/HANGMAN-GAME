import pygame,sys,asyncio
import random
import string

pygame.init() #initializing
screen = pygame.display.set_mode((1385, 720))#to make the screen height and width respectively
pygame.display.set_caption("HANGMAN")
hangman_surface = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
hangman_surface1 = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)
hangmansurface=[hangman_surface,hangman_surface1]
# next_surface=pygame.Surface(((1200,680)),pygame.SRCALPHA)
BG = pygame.transform.scale(pygame.image.load("book3.jpg"),(screen.get_width(), screen.get_height())) #loading background image
BG_0=pygame.image.load("black.png")
bg_wood1=pygame.transform.scale(pygame.image.load("start_screenimg.png"),(800,720))
hanger=pygame.image.load("hanger-removebg-preview.png").convert_alpha()
next_img=pygame.image.load("playbutton-removebg-preview.png").convert_alpha()
# main_word=pygame.transform.scale(pygame.image.load("main_word.png"),(240,240))
hangman_image=[pygame.transform.scale(pygame.image.load("hang_1.png").convert_alpha(),(250,300)),
               pygame.transform.scale(pygame.image.load("hang_4.png").convert_alpha(),(250,300))]   
#    pygame.transform.scale(pygame.image.load("hang_2.png").convert_alpha(),(250,300))
            #    pygame.transform.scale(pygame.image.load("hang_3.png").convert_alpha(),(250,300)),
            #    pygame.transform.scale(pygame.image.load("hang_5.png").convert_alpha(),(250,300))]
hangmancry_image=[pygame.image.load("cry_hang_1.png"),pygame.image.load("cry_hang_3.png")]

hanger1=pygame.transform.scale(pygame.image.load("hanger1.png"),(550,550))
pygame.font.init()
clock = pygame.time.Clock()
running = True
image_hang=0
i=0
count1=0
bubble_font=pygame.font.Font("Macondo-Regular.ttf",40)
qfont=pygame.font.Font("AmaticSC-Bold.ttf",40)
qfont1=pygame.font.Font("AmaticSC-Bold.ttf",40)
pygame.font.Font.set_underline(qfont1,True)
pygame.font.Font.set_bold(qfont,True)
start_font=pygame.font.Font("GloriaHallelujah-Regular.ttf",70)
word_was_font=pygame.font.Font("GloriaHallelujah-Regular.ttf",35)
qfont_info=pygame.font.SysFont("Lucida Fax",30,bold=True)
qfont_ss=pygame.font.SysFont("Arial",90,bold=True)
qfont_ss1=pygame.font.SysFont("Arial",50,bold=True)
qfont_lost=pygame.font.SysFont("Chiller",60,bold=True)
# pygame.font.Font(qfont_lost,underline=True)

#sound
# pygame.mixer.init(4410, -8, 2, 5000)
# letter_click = pygame.mixer.Sound("letter_click.ogg")
# next_sound=pygame.mixer.Sound("next.ogg")
# game_sound=pygame.mixer.Sound("game_sound.ogg")

t=False

my_dict = {
    'ANIMALS': ['ELEPHANT', 'GIRAFFE', 'PENGUIN', 'KANGAROO', 'CHEETAH'],
    'COUNTRY': ['AUSTRALIA', 'BRAZIL', 'JAPAN', 'CANADA', 'INDIA'],
    'FRUITS': ['PINEAPPLE', 'STRAWBERRY', 'WATERMELON', 'MANGO', 'BLUEBERRY'],
    
    'COLORS': ['BLUE', 'VERMILION', 'INDIGO', 'PINK', 'YRLLOW'],
    'SPORTS': ['BASKETBALL', 'SOCCER', 'TENNIS', 'VOLLEYBALL', 'BADMINTON'],
    'PROFESSIONS': ['DOCTOR', 'ENGINEER', 'ASTRONAUT', 'CHEF', 'MUSICIAN'],
    'PLANETS': ['MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN'],
    'LANGUAGES': ['SPANISH', 'MANDARIN', 'FRENCH', 'ARABIC', 'RUSSIAN'],
    'Food': ['PIZZA', 'SUSHI', 'CHOCOLATE', 'ICE CREAM', 'SANDWICH']
}
# 'Movies': ['INCEPTION', 'TITANIC', 'AVATAR', 'JURASSIC PARK', 'THE GODFATHER'],
# my_dict={
#     "A N I M A L S": ["ELEPHANT", "GIRAFFE", "LION", "MONKEY", "PENGUIN", "ZEBRA"],
#     "F R U I T S": ["APPLE", "BANANA", "GRAPE", "ORANGE", "STRAWBERRY", "WATERMELON"],
#     "C O L O R S": ["BLUE", "GREEN", "RED", "YELLOW", "ORANGE", "PURPLE"],
#     "S H A P E S": ["CIRCLE", "SQUARE", "TRIANGLE", "HEART", "STAR", "DIAMOND"],
#     "N U M B E R S": ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX"]
# }

pygame.font.get_fonts()

 #for hangman switch case
a=0
z=20
list_hanger=[]
array=[]#of letters
string1=[]
string2=[]
count1=0
incorrect=0
x1=-1
n=0
level_number=0
check=level_number
a1=''
values=[]
def initialize_game():
    global key, value, length, a, z, array, string1, string2, n,level_number,incorrect,list_hanger,x1,check,values
    key = random.choice(list(my_dict))
    value= random.choice(list(my_dict.get(key)))
    
    # values.append(value)
    length = len(value)
    level_number+=1
    check=level_number
    a = 0
    z = 20
    x1=-1
    array = []
    string1 = ["_ "] * length
    string2 = []
    n = 0
    incorrect =0
    list_hanger=[]
    for char in string.ascii_uppercase:
        array.append(char)
    array = array[:26]
   
def draw_text():
    question = qfont.render(key,10,"black")#rendering it
    screen.blit(question,(300,75))#placing img onto the screen
    level=qfont.render("Level: "+ str(level_number),1,"red")
    screen.blit(level,(880,75))

def hang(x):
    global list_hanger
 
    for x1 in range(0,x):
        if x1==0:
            pygame.draw.line(screen,"black",(920,210),(920,265),width=4)
        elif x1==1:    
            pygame.draw.circle(screen,"black",(920,285),(20),width=0,draw_top_right=True, draw_top_left=True, draw_bottom_left=True, draw_bottom_right=True)
        elif x1==2: 
            pygame.draw.line(screen,"black",(920,300),(920,400),width=4)#ribline
        elif x1==3: 
            pygame.draw.line(screen,"black",(920,310),(970,335),width=5)#right hand
        elif x1==4: 
            pygame.draw.line(screen,"black",(920,310),(870,335),width=5)#left hand
        elif x1==5: 
            pygame.draw.line(screen,"black",(920,400),(970,425),width=5)#right leg
        elif x1==6: 
            pygame.draw.line(screen,"black",(920,400),(870,425),width=5)#left leg

    
        screen.blit(screen,(0,0))

    pygame.display.flip()
    return x1
def draw_letters():
    global array,count1,check,level_number

    z=20
    b=20
    count=0
    rect=[]
    rect1=[]
 
    for p in array:
        # print(p,end=" ")  
        if count in range(0,13):
            letter=qfont.render(p,10,"black")
            rect.append(letter.get_rect(topleft=(100+z,400)))
            # screen.blit(letter,(100+z,400))
            screen.blit(letter,rect[-1])
            pygame.draw.rect(screen,(255,255,255),rect[-1],width=-1)
    
        else:
            letter=qfont.render(p,10,"black")
            rect1.append(letter.get_rect(topleft=(100+b,500)))
            # screen.blit(letter,(100+b,450))
            screen.blit(letter,rect1[-1])
            pygame.draw.rect(screen,(255,255,255),rect1[-1],width=-1)
            b=b+40
        z=z+40
        if p=="Z":           
            break
        count=count +1
       
    # print(count)
    rect2=rect+rect1
    return rect2
def next():
    global level_number,image_hang
    pygame.time.wait(100)
    next=True
    while next:
        
        event=pygame.event.poll()
        if event.type==pygame.QUIT:
            next=False
        # screen.fill("yellow")
        
        screen.blit(BG,(0,0))
        # screen.blit(next_img,(500,100))
        # pygame.mixer.Sound.play(next_sound)
        right_word_was=word_was_font.render("word was:   ",1,(255,0,0))
        right_word=qfont1.render(value,1,"black")

        screen.blit(right_word_was,(150,80))
        screen.blit(right_word,(350,90))
        
        level_word=qfont.render("LEVEL: "+str(level_number+1),1,"red")
        screen.blit(level_word,(880,75))
        
        
        next_rect=next_img.get_rect(topleft=(400,100))
        pygame.draw.rect(screen,(255,255,255),next_rect,width=-1)
        screen.blit(next_img,next_rect)
        
        if image_hang>=len(hangman_image):
            image_hang=0
        clock.tick(4)    
        h_img=hangman_image[image_hang]
        x=850
        y=200
       
        screen.blit(h_img,(x,y))
        image_hang+=1

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if next_rect.collidepoint(event.pos):
                game()
                # print("next is clickked")
            return True
        pygame.display.flip()
        
        clock.tick(60)
    pygame.quit()  
    return False 

def lose():
    global level_number,i
    # pygame.time.wait(100)
    lose=True
    while lose:
        
        event=pygame.event.poll()
        if event.type==pygame.QUIT:
            lose=False
        # screen.blit(BG,(0,0))
        screen.fill("white")
        right_word_was=word_was_font.render("Word was:   " ,1,"black")
        screen.blit(right_word_was,(80,125))
        right_word=qfont1.render(value,1,"RED")
        screen.blit(right_word,(280,135))
        # level_word=qfont_info.render("LEVEL: "+str(level_number),1,"red")
        # screen.blit(level_word,(880,40))
        score_word=qfont_info.render("SCORE: "+str(level_number-1),1,"red")
        screen.blit(score_word,(1000,140))
        lose_word=qfont_lost.render("YOU LOST !!!",1,"darkblue")
        screen.blit(lose_word,(500,10))
        playagain_word=start_font.render("PLAY AGAIN",10,"red")
        playagain_rect=playagain_word.get_rect(topleft=(700,320))
        quit_word=start_font.render("QUIT",10,"black")
        quit_rect=quit_word.get_rect(topleft=(740,470))
        pygame.draw.rect(screen,(255,255,255),playagain_rect,width=-1)
        pygame.draw.rect(screen,(255,255,255),quit_rect,width=-1)
        screen.blit(playagain_word,playagain_rect)
        screen.blit(quit_word,quit_rect)
        screen.blit(hanger1,(-30,200))
        if i>=len(hangmancry_image):
            i=0
        clock.tick(4)    
        hcry_img=hangmancry_image[i]
        x=50
        y=200
    
        screen.blit(hcry_img,(x,y))
        i+=1

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if playagain_rect.collidepoint(event.pos):
                
                level_number=level_number-1
                
                # lose_screen_result = next()
                # if lose_screen_result:
                    # initialize_game()
                game()
            elif quit_rect.collidepoint(event.pos):
                pygame.QUIT()
                # print("quit is clicked")
    
        pygame.display.flip()
        
        
        clock.tick(60)
    pygame.quit()
    return False 

def on_mouse_button_down(event, rect):
    global incorrect
    global array,string2
    
    guess=""
    s2=""
     
    for s in string1:#converting it to string
        s2+=s
    s3= qfont.render(s2,10,"black")#rendering it
    screen.blit(s3,(300,225))

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        # pygame.mixer.Sound.play(letter_click)
        for idx, l in enumerate(rect):#rect shows the position and at that position array elemnt starting from 1 i.e A is printed
            if l.collidepoint(event.pos):
                # print(array[idx] + "..................was pressed")
                
                guess+=array[idx] 
                array[idx]="  "
                
                if guess not in value:
                    
                    if len(string2)<6:
                        string2.append(guess)
                        incorrect=len(set(string2))
                        # print("the value of incorersct: "+str(incorrect)) 
                    else:
                        lose()
                else:
                    for i,word in enumerate(value):
                        if word in guess:
                            string1[i]=word
                # print(string1)
                
                if "_ " not in string1:
                    
                    # print("done") 
                    return True
                
    
def draw():
    screen.blit(BG,(0,0))
    screen.blit(hanger,(750,176))

def game():
    initialize_game()
    running =True
    global incorrect,x1
    global array,count1,check,level_number
      
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        # for event in pygame.event.get():#just creates event when it is run
        event=pygame.event.poll()#gettinga single event everytime
        if event.type == pygame.QUIT:
            running = False

        draw()
        draw_text()
        rect2 =draw_letters()
        
        result=on_mouse_button_down(event,rect2)
        # hang(len(string2))
        # next_screen(t)
        if incorrect!=0:
            x1=hang(incorrect)
            # print(x1)
        if result:
            next_screen_result = next()
            if next_screen_result:
                initialize_game()
            else:
                running = False

        pygame.display.flip()#updating display
        
        clock.tick(60)  # limits FPS to 60

    pygame.quit()
# game()
def intro():
    intro=True
    while intro:
        
        event=pygame.event.poll()
        if event.type==pygame.QUIT:
            intro=False

        screen.fill("white")
        screen.blit(bg_wood1,(0,0))
        info=bubble_font.render("Guess the word related given word.",5,"darkblue")
        info1=bubble_font.render("If the guessed letter is wrong the hangman",5,"darkblue")
        info4=bubble_font.render("will start hanging.",5,"darkblue")
        info3=bubble_font.render("Game gets over when the man gets hanged.",5,"darkblue")
        screen.blit(info,(460,50))
        screen.blit(info1,(460,120))
        screen.blit(info4,(460,157))
        screen.blit(info3,(460,227))
        next_word=start_font.render("NEXT",10,"red")
        next_rect=next_word.get_rect(topleft=(950,450))
        pygame.draw.rect(screen,(255,255,255),next_rect,width=-1)
        screen.blit(next_word,next_rect)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if next_rect.collidepoint(event.pos):
            #    print("next is clickked")
               return True 

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    return False
async def start_screen():
    start =True
    while start:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
               start = False

        # screen.fill("lightblue")
        screen.fill("white")
        screen.blit(bg_wood1,(0,0))
        # pygame.mixer.Sound.play(game_sound) 
        # screen.blit(main_word,(500,-80))
        hangman_font=pygame.font.Font("GloriaHallelujah-Regular.ttf",50)
        hangman_word=hangman_font.render("HANGMAN",1,"brown")
        screen.blit(hangman_word,(600,10))
        # screen.draw.text("HANGMAN", (500, 50), width=60,lineheight=2)
        start_word=start_font.render("START",10,"red")
        start_rect=start_word.get_rect(topleft=(780,180))
        quit_word=start_font.render("QUIT",10,"black")
        quit_rect=quit_word.get_rect(topleft=(780,320))
        pygame.draw.rect(screen,(255,255,255),start_rect,width=-1)
        pygame.draw.rect(screen,(255,255,255),quit_rect,width=-1)
        screen.blit(start_word,start_rect)
        screen.blit(quit_word,quit_rect)

        if event1.type == pygame.MOUSEBUTTONDOWN and event1.button == 1:
            if start_rect.collidepoint(event1.pos):
                intro_result = intro()
                if intro_result:  # If intro returns True, start the game
                    game()
                # print("start is clickked")
            elif quit_rect.collidepoint(event1.pos):
                # print("quit is clicked")
                pygame.quit()
        pygame.display.flip()#updating display
        clock.tick(60)  # limits FPS to 60

    pygame.quit()
    await asyncio.sleep(0)
asyncio.run(start_screen())
   
