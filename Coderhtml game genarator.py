#Code power game maker
#Type of device for the game. One space in python for indentation which is used for brackets in other programming languages. Use one space in python.
print("Type the option content and press the enter key.")
gametype= input("Which type of game- 1) PC 2) Mobile-")
if(gametype=="PC" or gametype=="Mobile"):
 global gameresolutionwidth
 global gameresolutionheight
 gameresolutionwidth= input("Enter game resolution width-")
 gameresolutionheight= input("Enter game resolution height-")
fps=input("Enter FPS (Frames per second)-") 
startcode='''<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1 style="color:blue;text-align:center;">R COMPUTER</h1>
<button onclick="startsoftware();">Open Software in Fullscreen Mode</button>
<canvas id="myCanvas" width="'''+gameresolutionwidth+'" height="'+gameresolutionheight+'''">
</canvas>
<script>'''
print(startcode)
