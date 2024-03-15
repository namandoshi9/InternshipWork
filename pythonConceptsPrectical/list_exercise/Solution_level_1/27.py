# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end

full_stack.insert(front_end.index('Redux') + 1, 'Python')
full_stack.insert(front_end.index('Redux') + 2, 'SQL')

print(full_stack)

