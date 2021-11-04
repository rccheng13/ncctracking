import os
from datetime import datetime
webdata = os.popen("http --session=li http://rwjinfo.win.rwjuh.edu/MTS/Neurology/loginform.asp").read()
webdata = os.popen("http --session=li -f POST http://rwjinfo.win.rwjuh.edu/MTS/Neurology/VerifyLogin.asp LoginName= Password=stroke1234").read()

webdata = os.popen("http --session=li http://rwjinfo.win.rwjuh.edu/MTS/Neurology_Care/list.asp").read()
ncc_cen = webdata.count("option value=")-1

webdata = os.popen("http --session=li http://rwjinfo.win.rwjuh.edu/MTS/Neurology_PrimStroke/List.asp").read()
strp_cen = webdata.count("option value=")-1

webdata = os.popen("http --session=li http://rwjinfo.win.rwjuh.edu/MTS/Neurology_ConsultStroke/List.asp").read()
strc_cen = webdata.count("option value=")-1

webdata = os.popen("http --session=li http://rwjinfo.win.rwjuh.edu/MTS/Neurology/List.asp").read()
gen_cen = webdata.count("option value=")-1

webdata = os.popen("http --session=li http://rwjinfo.win.rwjuh.edu/MTS/Neurology_VEEG_EMU/List.asp").read()
epi_cen = webdata.count("option value=")-1

ds = datetime.now().strftime("%Y-%m-%d")
ts = datetime.now().strftime("%H:%M")

f=open("census_log.csv","a")
f.write(ds+","+ts+","+str(ncc_cen)+","+str(strp_cen)+","+str(strc_cen)+","+str(gen_cen)+","+str(epi_cen)+",\n")
f.close()
