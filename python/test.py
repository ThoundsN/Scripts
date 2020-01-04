


text = """
http://virtualstudio.yahoo.com
http://sports.search.yahoo.com
http://promo.yahoo.com
http://developer.yahoo.com
http://redir.yahoo.com
http://help.yahoo.com
https://virtualstudio.yahoo.com
http://alpha.sports.yahoo.com
http://login.yahoo.com
https://promo.yahoo.com
http://security.yahoo.com
http://toolbar.yahoo.com
https://help.yahoo.com
https://security.yahoo.com
http://developer.search.yahoo.com
https://developer.search.yahoo.com
https://login.yahoo.com
http://us.yahoo.com
https://us.yahoo.com
https://sports.search.yahoo.com
http://private.search.yahoo.com
https://alpha.sports.yahoo.com
https://api.sports.yahoo.com
http://api.sports.yahoo.com
http://preview.sports.yahoo.com
https://profiles.sports.yahoo.com
https://private.search.yahoo.com
http://profiles.sports.yahoo.com
http://test.gemini.yahoo.com
http://api.gemini.yahoo.com
https://api.gemini.yahoo.com
https://test.gemini.yahoo.com
https://preview.sports.yahoo.com
https://developer.yahoo.com
http://o2.ycpi.ne1.yahoo.com
https://o2.ycpi.ne1.yahoo.com
http://blog.360.yahoo.com
http://search.yahoo.com
https://search.yahoo.com
http://private.comet.vip.sg3.yahoo.com
https://private.comet.vip.sg3.yahoo.com
http://sports.yahoo.com
https://sports.yahoo.com
http://adspecs.yahoo.com
https://adspecs.yahoo.com
http://api.lps.cp.yahoo.com
https://api.lps.cp.yahoo.com
http://election2020.yahoo.com
https://election2020.yahoo.com
http://stgmerchant.gemini.yahoo.com
https://stgmerchant.gemini.yahoo.com
https://mail.partners.yahoo.com
http://mail.partners.yahoo.com
"""


list  = text.split()

sortedlist = (sorted(list, key=lambda x: (x[::-1], len(x))))

for a in sortedlist:
    print(a)

