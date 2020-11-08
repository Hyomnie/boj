while True:
  a=input()
  if a=='.':
    break
  stack=[]
  s=True
  for i in a:
    if i == '(' or i == '[':
      stack.append(i)
    elif i == ')':
      if not stack or stack[-1] =='[':
        s=False
        break
      elif stack[-1] == '(':
        stack.pop()
    elif i == ']':
      if not stack or stack[-1] == '(':
        s=False
        break
      elif stack[-1] == '[':
        stack.pop()
  if s == True and not stack:
    print('yes')
  else:
    print('no')
