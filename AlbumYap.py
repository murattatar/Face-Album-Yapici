######################################################################
# Faces of Face's v1.1TR
# by Murat Tatar
# Aralık 2017
######################################################################


# işletim sistemi
import os


basla = raw_input(u"Başlanacak Id: ")
#uyesayisi = raw_input(u"Üye sayısı: ")
#boyut = raw_input(u"Avatar boyutu? ")
boyut = 60
uyesayisi = 89

if basla =="": basla = 4
if uyesayisi =="": uyesayisi = 6*15
if boyut  =="": boyut  = 60

basla = int(basla)
uyesayisi = int(uyesayisi)
boyut = int(boyut)




sli = unicode(str(boyut/2+2))
bsli_x = unicode(str(boyut * 3.2))
bsli_y = unicode(str(boyut / 2.2))

boyut = unicode(str(boyut))




# resim döndürmeyen ID'ler
noid = [0, 1, 2, 3, 8, 9, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


html =  u"""<!DOCTYPE html><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /> 
<title>Face'in Yüzleri</title> <head> 
<style class="cp-pen-styles"> 
body, 
html {
  padding: 0 10px;
  margin: 0;
  background: #0e0f11;
  color: #ecf0f1;
  font-family: "Open Sans", sans-serif;
  min-height: 100vh;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
      -ms-flex-direction: row;
          flex-direction: row;
  -webkit-box-align: center;
      -ms-flex-align: center;
          align-items: center;
  width: 95%;
}
* {
}
h1, p { text-align: center;}

a:link,
a:hover,
a:active,
a:visited {
  -webkit-transition: color 150ms;
  transition: color 150ms;
  color: #95a5a6;
  text-decoration: none;
}
a:hover {
  color: #5f5c5d;
  text-decoration: none;


}
.contain {
	width: auto;
	margin-left: 7%;
	margin-right: 7%;
	
}
.row {
	overflow: auto;
	width: 83%;
	margin-right: auto;
	margin-left: 50px;
}
.row__inner {
	-webkit-transition: 400ms -webkit-transform;
	transition: 400ms -webkit-transform;
	transition: 400ms transform;
	transition: 400ms transform, 400ms -webkit-transform;
	font-size: 0;
	white-space: normal;
	margin: 20px 0;
	padding-bottom: 10px;
}
.tile { 
  position: relative;
  display: inline-block;
  width: """ + boyut + u"""px;
  height: """ + boyut + u"""px;
  margin-right: 8px;
  font-size: 5px;
  cursor: pointer;
  -webkit-transition: 400ms all;
  transition: 400ms all;
  -webkit-transform-origin: center left;
          transform-origin: center left;
}
.tile__img {border-radius:50%; /* opacity: 0.15; */
  width: """ + boyut + u"""px;
  height: """ + boyut + u"""px;
  -o-object-fit: cover;
     object-fit: cover;
}
.tile__details {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  top: 0;
  font-size: 5px;
  opacity: 0;
 /* background: -webkit-linear-gradient(bottom, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
  background: linear-gradient(to top, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);*/
  -webkit-transition: 400ms opacity;
  transition: 400ms opacity;
}
.tile__details:after,
.tile__details:before {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  /*display: #000;*/
}
.tile__details:after {
  margin-top: -""" + sli + u"""px;
  margin-left: -""" + sli + u"""px;
  width: """ + boyut + u"""px;
  height: """ + boyut + u"""px;
  /* border: 4px solid #ecf0f1; */
  border: 2px solid #06d6a9;
  line-height: 60px;
  text-align: center;
  border-radius: 100%;
  
 
}
.tile__details:before { 
  /* content: "▶"; */
  left: 0;
  width: 100%;
  font-size: 5px;
  margin-left: 7px;
  margin-top: -18px;
  text-align: center;
  /* background: rgba(0,0,0,0.1); */

}
.tile:hover .tile__details { z-index:9999;
  opacity: 1; 
}
.tile__title { text-align:center; color:#06d6a9;
font-size:5px;


  position: absolute;
  bottom: 40%;
  width:100%;
  margin-left:auto; margin-right:auto;
}




.row__inner:hover .tile:hover {
  -webkit-transform: scale(4.5);
          transform: scale(4.5);
  z-index:9999;

  
}




.tile:hover ~ .tile {


  -webkit-transform: scale(.92) translate3d(""" + bsli_x + u"""px, """ + bsli_y + u"""px, 0);
          transform: scale(.92) translate3d(""" + bsli_x + u"""px, """ + bsli_y + u"""px, 0);

}







</style></head><body>


<div class="contain">

  <h1>Face'in Yüzleri</h1>
  
    <p> 
  <span style="white-space:nowrap">Face'in Yüzleri</span> by <a style="white-space:nowrap" href="https://steemit.com/@murattatar">Murat Tatar</a>. Esin kaynağı <a href="https://codepen.io/joshhunt/pen/LVQZRa">joshhunt</a></p>
  
<div class="row__inner">""" 


for i in xrange(basla,basla+uyesayisi+1):
    
    if i in noid: continue

    

    html = html + u"""<div class="tile" onclick="window.open('https://www.facebook.com/profile.php?id=""" + unicode(str(i)) +u"""','myw');">
      <div class="tile__media">
        <img class="tile__img" src="https://graph.facebook.com/"""+ unicode(str(i)) +u"""/picture?type=large" />
      </div>
      <div class="tile__details">
        <div class="tile__title">
          User
        </div>
      </div>
    </div>"""

  

html = html +u"""</div>

</div>


</body></html>"""



# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


o = open("FaceYuzleri.html","w"); o.write(html.encode("utf-8")); o.close()
os.startfile("FaceYuzleri.html")






