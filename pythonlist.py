jvm_langs=['java','jython','groovy','scala','jruby']
print('I know of',jvm_langs.__len__(),'langs that can run on the JVM')

print('I know of',len(jvm_langs),'langs that can run on the JVM')

print('oops I forgot Clojure')
jvm_langs.append('Clojure')

for lang in jvm_langs:
	print(lang)
print("The 3rd JVM languages is",jvm_langs[2])
print("The first 3 JVM languaes are",jvm_langs[:3])
print("The 2nd to 4th JVM languages are",jvm_langs[1:4])

print("lets sort these languages")
jvm_langs.sort()
print(jvm_langs)
