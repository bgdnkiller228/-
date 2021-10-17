let = 'КЛНТЭ'
s = []
for a in let:
    for b in let:
        for c in let:
            for d in let:
                for e in let:
                    for f in let:
                        word = a + b + c + d + e + f
                        s.append(word)
for i in range(0, len(s)):
    if s[i] == 'ККЛКЛК':
        print(i+1)
