

search = []

with open("input.txt", "r") as file:

    for line in file:
        line = line[:-1]
        search.append(line)

    
res = 0
word = "XMAS"

for i in range(len(search)):
    for j in range(len(search[0])):

        if search[i][j] == word[0]:

            # search left
            for k in range(len(word)):
                if  j - k < 0 or search[i][j-k] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1
            # search right
            for k in range(len(word)):
                if  j + k >= len(search[0]) or search[i][j+k] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1  
            # search down       
            for k in range(len(word)):
                if  i + k >= len(search) or search[i+k][j] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1 
            # search up
            for k in range(len(word)):
                if  i - k < 0 or search[i-k][j] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1     
            #search up left
            for k in range(len(word)):
                if  i - k < 0 or j-k < 0 or search[i-k][j-k] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1                          
            #search up right
            for k in range(len(word)):
                if  i - k < 0 or j+k >= len(search[0]) or search[i-k][j+k] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1   
            #search down right
            for k in range(len(word)):
                if  i+k >= len(search) or j+k >= len(search[0]) or search[i+k][j+k] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1             
            #search down left
            for k in range(len(word)):
                if  i+k >= len(search) or j - k < 0 or search[i+k][j-k] != word[k]:
                    break
                if k == len(word)-1:
                    res += 1                  

print(res)


    

    