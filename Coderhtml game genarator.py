#Coderhtml game generator
#Type of device for the game. One space in python for indentation which is used for brackets in other programming languages. Use one space in python.
print("Type the option content and press the enter key.")
gametype= input("Which type of game- 1) PC 2) Mobile-")
if(gametype=="PC" or gametype=="Mobile"):
 global gameresolutionwidth
 global gameresolutionheight
 gameresolutionwidth= input("Enter game resolution width-")
 gameresolutionheight= input("Enter game resolution height-")
global imagecounter
imagecounter=-1
global image
global imageid
global x
global y
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
   print('Imageid-')   
   print(image[imageprint])
  for imageidprint in imageid:
   print('Image variable-')     
   print('t2x'+imageid[imageidprint]+' t2y'+imageid[imageidprint])
  if(imagenumber=='yes'):
   images()
images()
global variableset
global keyset
global logicset
global counter
global keycounter
global ifcounter
global d
global dcounter
d={}
dcounter=0
counter=0
keycounter=0
ifcounter=0
variableset={}
keyset={}
logicset={}
def deletec():
 global d
 global dcounter
 global count
 d[dcounter]= input('d-')
 dcounter=dcounter+1
 count=count+1
def variable():
 global counter
 global variableset
 global count
 variableset[counter]= input('v-')
 counter=counter+1
 count=count+1
def keycondition():
 global keycounter
 global keyset
 global count
 keyset[keycounter]= input('key-')
 keycounter=keycounter+1
 count=count+1
def ifcondition():
 global ifcounter
 global logicset
 global count
 logicset[ifcounter]= input('c-')
 ifcounter=ifcounter+1
 count=count+1
global count
count=1
def logic():
 global count
 global dlogic3
 global ifcounter
 global logicset
 logicinput= input('line '+str(count)+' Command v, c, key, d, htmlcode-')
 if(logicinput=='d'):
  deletec()
  logic()
 if(logicinput=='v'):
  variable()
  logic()
 if(logicinput=='c'):
  ifcondition()
  logic()
 if(logicinput=='key'):
  keycondition()
  logic()
 if(logicinput=='htmlcode'):
  count=1
logic()
global dcounter54
dcounter54=0
def dimages54():
 global dcounter
 global dcounter54
 if(dcounter54<dcounter):
  print(logicset[dcounter54])
  dcounter54=dcounter54+1
  dimages54()
dimages54()
startcode='''Html game code-
<!DOCTYPE html>
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
<script>'''
code2='''let c = document.getElementById("myCanvas");
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
function mup22(event){'''
#let key=event.key;if(key2==1){if(key=="a"){t2x=t2x+1;t2y=t2y+1;key2=0;
code3='''}
function startsoftware2(){
ctx.clearRect(0, 0,1280, 720);
ctx.fillStyle ="white";
ctx.fillRect(0,0,1280,720);'''
print(code)
global imagecounter43
imagecounter43=0
def images43():
 global counter
 global imagecounter43
 if(imagecounter43<counter):   
  print('let '+variableset[imagecounter43]+';')
  imagecounter43=imagecounter43+1
  images43()
images43()
print(code2)
global imagecounter53
imagecounter53=0
def images53():
 global keycounter
 global imagecounter53
 if(imagecounter53<keycounter):
  print(keyset[imagecounter53])
  imagecounter53=imagecounter53+1
  images53()
images53()
print(code3)
global ifcounter54
ifcounter54=0
def images54():
 global ifcounter
 global ifcounter54
 if(ifcounter54<ifcounter):
  print(logicset[ifcounter54])
  ifcounter54=ifcounter54+1
  images54()
images54()
code4='''key2=1;
a=0;
}
startsoftware2.call();
s2.call();
function s2() {
  if (a==0) {
    a=1;
    startsoftware2.call();
  }  
}
setInterval(s2,800);
</script>
</body>
</html>'''
print(code4)
