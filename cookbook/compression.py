import gzip
f = open('test.txt','rb')
f_out = gzip.open('test.txt.gz','wb')

f_out.writelines(f)
f_out.close()
f.close()
