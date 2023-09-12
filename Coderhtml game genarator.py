#Coderhtml game generator
#Type of device for the game. One space in python for indentation which is used for brackets in other programming languages. Use one space in python.
print("Type the option content and press the enter key.")
gametype= input("Which type of game- 1) PC 2) Mobile-")
if(gametype=="PC" or gametype=="Mobile"):
 global gameresolutionwidth
 global gameresolutionheight
 gameresolutionwidth= input("Enter game resolution width-")
 gameresolutionheight= input("Enter game resolution height-")
fps=input("Enter FPS (Frames per second)-") 
keycode='''document.documentElement.onkeydown=function(){mup22(event)};
function mup22(event){
let key2a =event.key;
if(key2a=="a"){
ctx.fillStyle = "red";
ctx.fillRect(0, 0,350,350);
t2333=2;
}
ctx.fillStyle = "green";
ctx.fillRect(0, 0,350,350);
}
}'''
mousecode='''document.documentElement.onmouseup = function(){mup22(event)};
function mup22(event){
let x = event.screenX;
let y = event.screenY;'''
global imagecounter
imagecounter=-1
global image
global imageid
image={}
imageid={}
#Use python sets
def images():
 global imagenumber
 imagenumber=input('Add images yes/no-')
 if(imagenumber=='yes'):
  global imagecounter   
  global image
  global imageid
  imagecounter=imagecounter+1   
  image[imagecounter]=input('Enter the unique name of the image file(.png file only). No duplicate names-')
  imageid[imagecounter]=input('Enter the unique id for the image file. No duplicate names-')
  print('Enterd images and imageids-')
  for imageprint in image:
   print(image[imageprint])
  for imageidprint in imageid:
   print(imageid[imageidprint])
  if(imagenumber=='yes'):
   images()
images()
gamecode='''function startsoftware2(){
if(t2333==1){
let t4hs=0;
let t4vs=0;
let t4ha=1;
let t4va=1;
let t4mh=0;
let t4mv=0;
t66point[0]=1;
t66point[1]=2;
tsd32++;
ctx.fillStyle = "yellow";
ctx.fillRect(0, 0,350,350);
ctx.font = "30px Verdana";
ctx.fillStyle = "blue";
ctx.fillText(tsd32,swidth/8+8,sheight-12);
t2333=1;
}
}
ctx.fillStyle = "brown";
ctx.fillRect(0, 0,350,350);
startsoftware2.call();'''
startcode='''<!DOCTYPE html>
<html>
<head>
</head>
<body>
<h1 style="color:blue;text-align:center;">R COMPUTER</h1>'''
print(startcode)
global imagecounter2
imagecounter2=0
def images2():
 global imagecounter
 global imagecounter2
 if(imagecounter2<=imagecounter):
  print('<img id="'+imageid[imagecounter2]+'" src="'+image[imagecounter2]+'.png" style="display: none;">')
  imagecounter2=imagecounter2+1
  images2()
images2()
code='''<button onclick="startsoftware();">Open Software in Fullscreen Mode</button>
<canvas id="myCanvas" width="'''+gameresolutionwidth+'" height="'+gameresolutionheight+'''">
</canvas>
<script>
let c = document.getElementById("myCanvas");
let ctx = c.getContext("2d");
function startsoftware(){
openFullscreen.call();
}
/*full screen code*/
function openFullscreen() {
var elem = document.getElementById("myCanvas");
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
  }
}
document.documentElement.onkeydown=function(){mup22(event)};
function mup22(event){
let key2a =event.key;
if(key2a=="a"){
key22a=1;
if(key22a==1){
t2x=t2x+1;
t2y=t2y+1;
}
}
key22a=0;
}
function startsoftware2(){
ctx.clearRect(0, 0,1280, 720);
ctx.fillStyle ="white";
ctx.fillRect(0,0,1280,720);
img = document.getElementById("image");
ctx.drawImage(img,t2x,t2y,30,30);
if(key22a==0){
t2x=t2x+0.01;
t2y=t2y+0.01;
}
key22a=0;
let ct= setTimeout(startsoftware2,20);
}
startsoftware2.call();
</script>
</body>
</html>'''
print(code)
