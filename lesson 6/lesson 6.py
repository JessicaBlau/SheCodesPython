#Exercise 3: rot_13

def rot_13():
    """
    a way to create the initial dictionary
    """
    encoding={}
    abc='abcdefghijklmnopqrstuvwxyzabcdefghijklm'
    ABC='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    for i in range(0,26):
        encoding.update({abc[i] : abc[i+13]})
        encoding.update({ABC[i] : ABC[i+13]})
    return encoding

print(rot_13()) # note that since dictionaaries are not sorted, it might look a bit different from
# what is written in the exercise. What matters is that the encoding is the same.
def decode(s):
    key = rot_13()
    sentence = []
    for i in range(0, len(s)):
        if key.get(s[i], 'none') != 'none':
            sentence.append(key[s[i]])
        else:
            sentence.append(s[i])
    new_sentence = ''.join(sentence)
    return new_sentence

print(rot_13('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))

"""
Other solutions, proposed by your fellow participant Merav Friedland from Bar Ilan branch, makes use
of the update and get methods of dictionries:
"""
def char_freq(word):
     freq = {}
     for i in word:
        if freq.get(i):
            value = freq[i]
            freq.update({i:value+1})
        else:
             freq.update({i:1})
     return freq

print(char_freq('abzz'))

def rot_13():
    """
    a way to create the initial dictionary
    """
    ROT_13_dict={}
    abc='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    ABC=abc.upper()
    for i in range(0,26):
        ROT_13_dict.update({abc[i] : abc[i+13]})
        ROT_13_dict.update({ABC[i] : ABC[i+13]})
    return ROT_13_dict

def decode (sentence):
    new_sentence=[]
    ROT_13_dict=rot_13()
    for i in sentence:
        if ROT_13_dict.get(i)==None:
            new_sentence.append(i)
        else:
            new_sentence.append(ROT_13_dict.get(i))
    new_sentence= "".join(new_sentence)
    return new_sentence

print(rot_13('V NZ YRNEAVAT CLGUBA JVGU FUR PBQRF NPNQRZL!'))