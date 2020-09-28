import sys
sys.path.insert(1, './class/')

from GameApp import *

def main():
    app = GameApp()
    app.play()
    
if __name__ == "__main__":
    main()
