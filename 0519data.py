data = []

#開啟檔案
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())


#讀取單字
words= {}

for lines in data:
	line = lines.split()
	for m in line:
		if m in words:
			words[m] +=1
		else:
			words[m] =1

#印出字串出現數大於100000的
# for m in words:
# 	if words[m]>100000:
# 		print(m, words[m])
#print(m,'有幾個:',words[m]')

#讓使用者輸入他們想找的關鍵字出現幾次

while True:
	x = input('請輸入你們想查詢的關鍵字')
	if x in words:
		print(x,'出現的次數為',words[x])
	else:
		print('沒有這個詞')