class Solution(object):
    def mostWordsFound(self, sentences):
        maxi = len(sentences[0].split(' '))
        for sen in sentences:
            count = len(sen.split(' '))
            if maxi < count:
                maxi = count
        return maxi

    def finalValueAfterOperations(self, operations):
        x = 0
        for oper in operations:
            for i in oper:
                if i == '-':
                    x -= 1
                    break
                if i == '+':
                    x += 1
                    break
        return x

    def restoreString(self, s, indices):
        result = list(s)

        i = 0
        while i < len(s):
            result[indices[i]] = s[i]
            i += 1
        resultt = ''
        for i in result:
            resultt += i
        return resultt


print()
inp1 = ["alice and bob love leetcode","i think so too","this is great thanks very much"]
print('mostWordsFound:')
print('input: ', inp1)
print('result: ', Solution().mostWordsFound(inp1))
print()

inp2 = ["--X","X++","X++"]
print('finalValueAfterOperations:')
print('input: ', inp2)
print('result: ', Solution().finalValueAfterOperations(inp2))
print()

inp3 = [4,5,6,7,0,2,1,3]
print('restoreString:')
print('input: ', "codeleet", inp3)
print('result: ', Solution().restoreString("codeleet", inp3))
print()
