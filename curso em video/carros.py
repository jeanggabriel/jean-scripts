from bs4 import BeautifulSoup
import requests

requests = requests.get('https://www.autocompara.com.br/br/web/wcsbrautocomlr/faca-sua-cotacao#_48_INSTANCE_ZJkGnyT9PKB8_=https%3A%2F%2Fwww.autocompara.com.br%2Fbr%2Fweb%2Fwcsbrautocomlr%2Fhome%3Fp_p_id%3DAutocompara_WAR_Autocomparaportlet_INSTANCE_25qpclIeviRN%26p_p_lifecycle%3D1%26p_p_state%3Dmaximized%26p_p_mode%3Dview%26p_p_col_id%3Dcolumn-3%26p_p_col_count%3D2%26_Autocompara_WAR_Autocomparaportlet_INSTANCE_25qpclIeviRN_javax.portlet.action%3DSTEP1%26_Autocompara_WAR_Autocomparaportlet_INSTANCE_25qpclIeviRN_base.portlet.view%3DInitialView%26')
soup = BeautifulSoup(requests.content,'html.parser')
soup1 = soup.select('div_W044_Information_Detail_WAR_W044_Information_Detailportlet_INSTANCE_A9tdgCWPpvuD__VIEW')
#soup2 = soup.select('div',{'class':'boxPolitica'})
soup3 = soup.select('div div viewbox[width|=219] div div div div ')
for i in soup3:
    print(i.text)
