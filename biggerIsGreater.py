

def biggerIsGreater(w):
    s = w
    # Write your code here
    lstOfLetters = [*s]
    for i in range(len(s)-1,-1, -1):
        if i == 0:
            newString = 'no answer'
            break
        if s[i] > s[i-1]:
            if i < len(s)-1:
                
                #find smallest letter that's bigger than this
                swapLetter = s[i-1]
                minLetter = min(list(filter(lambda x: x > swapLetter, lstOfLetters[i:])))
                indexOfSwap = lstOfLetters[i:].index(minLetter) + i
                lstOfLetters[i-1] = minLetter
                lstOfLetters[indexOfSwap] = swapLetter
                restOfLetters = lstOfLetters[i:]
                restOfLetters.sort()
                lstOfLetters = lstOfLetters[:i] + restOfLetters
                newString = ''.join(lstOfLetters)
                
            else:
                newS = s[:i-1] + s[i] + s[i-1] + s[i+1:]
                newString = newS
            break
    return newString
    
            
                


w = ['bkedcba', 'bb', 'hefg', 'dhck', 'dkhc']


assert biggerIsGreater('zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw') == 'zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgwm'
assert biggerIsGreater('zyyxwwtrrnmlggfeb') == 'no answer'
assert biggerIsGreater('ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvlmcpapfbmzxmftrkkqvkpflxpezzapllerxyzlcf') == 'ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvlmcpapfbmzxmftrkkqvkpflxpezzapllerxyzlfc'
assert biggerIsGreater('biehzcmjckznhwrfgglverxsezxuqpj') == 'biehzcmjckznhwrfgglverxsjepquxz'
assert biggerIsGreater('rebjvsszebhehuojrkkhszxltyqfdvayusylgmgkdivzlpmmtvbsavxvydldmsym') == 'rebjvsszebhehuojrkkhszxltyqfdvayusylgmgkdivzlpmmtvbsavxvydldmyms'
assert biggerIsGreater('unpzhmbgrrs') == 'unpzhmbgrsr'
assert biggerIsGreater('jprfovzkdlmdcesdcpdchcwoedjchcovklhrhlzfeeptoewcqpxg') == 'jprfovzkdlmdcesdcpdchcwoedjchcovklhrhlzfeeptoewcqxgp'
assert biggerIsGreater('ywsfmynmiylcjgrfrrmtyeeykffzkuphpajndwxjteyjba') == 'ywsfmynmiylcjgrfrrmtyeeykffzkuphpajndwxjtjabey'
assert biggerIsGreater('dkuashjzsdq') == 'dkuashjzsqd'
# w = ['zedawdvyyfumwpupuinbdbfndyehircmylbaowuptgmw',
# 'zyyxwwtrrnmlggfeb',
# 'ocsmerkgidvddsazqxjbqlrrxcotrnfvtnlutlfcafdlwiismslaytqdbvlmcpapfbmzxmftrkkqvkpflxpezzapllerxyzlcf',
# 'biehzcmjckznhwrfgglverxsezxuqpj',
# 'rebjvsszebhehuojrkkhszxltyqfdvayusylgmgkdivzlpmmtvbsavxvydldmsym',
# 'unpzhmbgrrs',
# 'jprfovzkdlmdcesdcpdchcwoedjchcovklhrhlzfeeptoewcqpxg',
# 'ywsfmynmiylcjgrfrrmtyeeykffzkuphpajndwxjteyjba',
# 'dkuashjzsdq',
# 'gwakhcpkolybihkmxyecrdhsvycjrljajlmlqgpcnmvvkjlkvdowzdfikh',
# 'nebsajjbbuifimjpdcqfygeitief',
# 'qetpicxagjkydehfnvfxrtigljlheulcsfidjjozbsnomygqbcmpffwswptbgkzrbgqwnczrcfynjmhebfbgseuhckbtuynvbo']

for i in w:
    print(biggerIsGreater(i))