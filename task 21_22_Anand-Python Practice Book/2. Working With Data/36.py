def anagrams(x):
   s=[]
   s.append([x[0]])
   for i in range(1,len(x)):
      flag=0
      for j in range(len(s)):
         if sorted(list(x[i]))==sorted(list(s[j][0])):
            s[j].append(x[i])
            flag=1
            break
      if flag==0:
         s.append([x[i]])
   return s    

        
        

print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))
