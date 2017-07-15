import pygame, keyboard, time

KEY_PRESSED = []
keyList = {}

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

print 'Send here CTRL+C, or CTR+D, or cose the window to exit'
print 'Initialized Joystick : %s' % j.get_name()

###--- get list of keys from KeyList.txt
def parseKeyList():
    global keyList
    listTXT = open('KeyList.txt', 'r')
    line = listTXT.readline()
    while line != '':
        line = listTXT.readline()
        if not '#' in line:
            buttons = line.split(":")
            if len(buttons) == 2:
                keyList[buttons[0]] = buttons[1].replace('\n','')
    listTXT.close()
            
    

##----get string with buttons from GamePad
def get():
    out = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    it = 0 #iterator
    pygame.event.pump()
    
    #Read input from the two joysticks       
    for i in range(0, j.get_numaxes()):
        out[it] = j.get_axis(i)
        it+=1
    #Read input from buttons
    for i in range(0, j.get_numbuttons()):
        out[it] = j.get_button(i)
        it+=1
    return out


def pushVirtualKey(K):
	RETURN = []
	#left stick
	if K[0] < -0.9:
		RETURN.append('LL')
	if K[0] > 0.9:
		RETURN.append('LR')
	if K[1] < -0.9:
		RETURN.append('LU')
	if K[1] > 0.9:
		RETURN.append('LD')
	if K[14] == 1:
		RETURN.append('L3')
		
	#right stick
	if K[2] < -0.9:
		RETURN.append('RL')
	if K[2] > 0.9:
		RETURN.append('RR')
	if K[3] < -0.9:
		RETURN.append('RU')
	if K[3] > 0.9:
		RETURN.append('RD')
	if K[15] == 1:
		RETURN.append('R3')

	#buutons ABXY
	if K[4] == 1:
		RETURN.append('Y')
	if K[5] == 1:
		RETURN.append('B')
	if K[6] == 1:
		RETURN.append('A')
	if K[7]==1:
		RETURN.append('X')

	##LB,LT, RB,RT
	if K[8]==1:
		RETURN.append('LB')
	if K[9] == 1:
		RETURN.append('RB')
	if K[10] == 1:
		RETURN.append('LT')
	if K[11] == 1:
		RETURN.append('RT')

	##start, mode
	if K[12] == 1:
		RETURN.append('mode')
	if K[13] == 1:
		RETURN.append('start')  

	return RETURN


def pushMultiply(keysSend):
	time.sleep(0.01)
	global KEY_PRESSED

	
	### if button unpressed
	for K in KEY_PRESSED:
		if not(K in keysSend): 
			KEY_PRESSED.remove(K)
			keyboard.release(keyList[K])
	
	### if button pressed first
	for S in keysSend:
		if not(S in KEY_PRESSED): 
			KEY_PRESSED.append(S)
			keyboard.press(keyList[S])


##------------ Initialie KeyList
parseKeyList()

##---------------start listen the gamepad and emulate keyboard
while True:
   #print get()
   #print pushVirtualKey(get())
   #push(pushVirtualKey(get()))
   pushMultiply(pushVirtualKey(get()))

