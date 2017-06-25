"""
function get() - I will spiz*il it from http://yameb.blogspot.ru/2013/01/gamepad-input-in-python.html
pyHook (pyautogui) to send keyboard - write to myself
"""

import pygame, keyboard, time, pyautogui
from KeyList import keyList

KEY_PRESSED = []

pygame.init()
j = pygame.joystick.Joystick(0)
j.init()

print 'Send here CTRL+C, or CTR+D, or cose the window to exit'
print 'Initialized Joystick : %s' % j.get_name()

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
	if K[0] < -0.5:
		RETURN.append('LL')
	if K[0] > 0.5:
		RETURN.append('LR')
	if K[1] < -0.5:
		RETURN.append('LU')
	if K[1] > 0.5:
		RETURN.append('LD')
	if K[14] == 1:
		RETURN.append('L3')
		
	#right stick
	if K[2] < -0.5:
		RETURN.append('RL')
	if K[2] > 0.5:
		RETURN.append('RR')
	if K[3] < -0.5:
		RETURN.append('RU')
	if K[3] > 0.5:
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
        
 
   
   
def push(key):	
	time.sleep(0.03)
	global KEY_PRESSED
	if key == None: 
		print 'NONE'
		##release all buttons
		for Keys in KEY_PRESSED:
			pass
			keyboard.release(keyList[Keys])
		KEY_PRESSED = []
		#return 0
		
	
	elif not(key in KEY_PRESSED):
		print key		
		
		KEY_PRESSED.append(key)
		try:			
			keyboard.press(keyList[key])
		except:
			print '***ERROR IN :'+key+' '+keyList[key]
	#else:
#		KEY_PRESSED.remove(key)
#		keyboard.release(keyList[key])
	
	
	##new key - need release other
	elif not(key in KEY_PRESSED):
		KEY_PRESSED = []
		keyboard.press(keyList[key])
		
	print KEY_PRESSED
	
	
def pushMultiply(keysSend):
	time.sleep(0.01)
	global KEY_PRESSED
	#print keysSend
	## emulate mouse move in R-stick
	'''for S in keysSend:
			key = keyList[S]
			if key == 'MouseL':
				pyautogui.moveRel(-10)
			if key == 'MouseR':
				pyautogui.moveRel(10)
			if key == 'MouseU':
				pyautogui.moveRel(0,-10)
			if key == 'MouseD':
				pyautogui.moveRel(0, 10)
	'''
	
	### if button unpressed
	for K in KEY_PRESSED:
		if not(K in keysSend) and not (K in ['RL', 'RU', 'RR', 'RD']):
			KEY_PRESSED.remove(K)
			keyboard.release(keyList[K])
	
	### if button pressed first
	for S in keysSend:
		if not(S in KEY_PRESSED) and not (S in ['RL', 'RU', 'RR', 'RD']):
			KEY_PRESSED.append(S)
			keyboard.press(keyList[S])
		else:
			key = keyList[S]
			if key == 'MouseL':
				pyautogui.moveRel(-10)
			if key == 'MouseR':
				pyautogui.moveRel(10)
			if key == 'MouseU':
				pyautogui.moveRel(0,-10)
			if key == 'MouseD':
				pyautogui.moveRel(0, 10)
			

		
		
			
			
while True:
   #print get()
   #print pushVirtualKey(get())
   #push(pushVirtualKey(get()))
   pushMultiply(pushVirtualKey(get()))
