### number hassing:

arr = [1,2,4,6,4,2,3,1]

freq = {}

for num in arr:
    if num in freq:
        freq[num]+= 1
    else:
        freq[num] = 1

print(freq)

### charecter hasing:

# count the frequency of character in a string. 

s = "abcdabcfcd priyansh"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1

print(freq)

## solving the same problem but USING ARRAY HASHING:

s = "abcdabcfcdpriyansh".lower()

hash_arr = [0]*26

for ch in s:
    
    index = ord(ch) - ord("a")

    hash_arr[index] +=1

print(hash_arr)

# finding maximum and minimum :

arr = [1,2,4,6,4,2,3,1]

freq = {}

for num in arr:
    if num in freq:
        freq[num]+=1

    else:
        freq[num] = 1

    max_element,max_freq = next(iter(freq.items()))
    min_element,min_freq = next(iter(freq.items()))
    
    for element,frequence in freq.items():

        if frequence >= max_freq:
            max_freq = frequence
            max_element = element

        if frequence <= min_freq:
            min_freq = frequence
            min_element = element
    
print(f"your max freqence {max_freq} for the element {max_element}")
print(f"your min freqence {min_freq} for the element {min_element}")      

