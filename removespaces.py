# remove all the spaces at front and back
sentence = "   this is python crt   "
print(sentence.strip())# with inbuilt
start_ind = None
end_ind = None
for i in range(len(sentence)):# to get first non-space char index
    if sentence[i] != " ":
        start_ind = i
        break
for i in range(len(sentence)-1,-1,-1):# to get last non-space char index
    if sentence[i] !=" ":
        end_ind = i
        break
print(sentence[start_ind : end_ind+1])#substring from start to end