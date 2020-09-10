low_to_num={"1":"1","abc":"2","def":"3","ghi":"4",
            "jkl":"5","mno":"6","pqrs":"7","tuv":"8",
            "wxyz":"9","0":"0"}
letter="abcdefghijklmnopqrstuvwxyz"
num="23456789"

def low_to_num1(s):
    for k in low_to_num:
        if s in k:
            return low_to_num[k]

s_input=[]
s=input()
for i in range(len(s)):
    if s[i]!=" ":
        if s[i].isupper():
            letter_lower=s[i].lower()

            position=letter.find(letter_lower)
            if position==25:
                s_input.append(letter[0])
            else:
                s_input.append(letter[position+1])
        elif s[i] in num:
            s_input.append(s[i])
        else:
            s_input.append(low_to_num1(s[i]))

print("".join(s_input))








