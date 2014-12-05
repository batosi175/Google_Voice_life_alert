#event_handler for text.py
import curses
correspondingValues = [48,49,50,51,52,53,54,55,56,57]

def main(stdscr):
	#no waiting for input when using getch
	stdscr.nodelay(1)
	#returns -1 when there is no input
	while True:
		c = stdscr.getch()

		if c!= -1:
			#loop for user input using numberic values 0--9
			for i in range(0,len(correspondingValues)):
				if c == correspondingValues[i]:
					#calls python program that sends a text using my void number
					execfile("text.py")
					stdscr.refresh()
					stdscr.move(0,0)
if __name__ == '__main__':
	curses.wrapper(main)