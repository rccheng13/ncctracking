import requests
from datetime import datetime
logindata = {
	'LoginName': '',
	'Password': 'stroke1234'
}

with requests.Session() as s:
		lo = s.post('http://rwjinfo.win.rwjuh.edu/MTS/Neurology/VerifyLogin.asp', data=logindata)
		ncc = s.get('http://rwjinfo.win.rwjuh.edu/MTS/Neurology_Care/list.asp')
		strp = s.get('http://rwjinfo.win.rwjuh.edu/MTS/Neurology_PrimStroke/List.asp')
		strc = s.get('http://rwjinfo.win.rwjuh.edu/MTS/Neurology_ConsultStroke/List.asp')
		gen = s.get('http://rwjinfo.win.rwjuh.edu/MTS/Neurology/List.asp')
		epi = s.get('http://rwjinfo.win.rwjuh.edu/MTS/Neurology_VEEG_EMU/List.asp')

		ncc_cen = ncc.text.count("option value=")-1
		strp_cen = strp.text.count("option value=")-1
		strc_cen = strc.text.count("option value=")-1
		gen_cen = gen.text.count("option value=")-1
		epi_cen = epi.text.count("option value=")-1

ds = datetime.now().strftime("%Y-%m-%d")
ts = datetime.now().strftime("%H:%M")

f=open("census_log.csv","a")
f.write(ds+","+ts+","+str(ncc_cen)+","+str(strp_cen)+","+str(strc_cen)+","+str(gen_cen)+","+str(epi_cen)+",\n")
f.close()

f=open("census_log_dw.csv","a")
f.write(ds+" "+ts+","+str(ncc_cen)+","+str(strp_cen)+","+str(strc_cen)+","+str(gen_cen)+","+str(epi_cen)+",\n")
f.close()

# f=open("census_log_test.csv","a")
# f.write(ds+","+ts+","+str(ncc_cen)+","+str(strp_cen)+","+str(strc_cen)+","+str(gen_cen)+","+str(epi_cen)+",\n")
# f.close()
