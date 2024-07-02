
def change_current_word_state(selected_word,input_char, current_word_state):
  modified_word_state=""
  for i in range(len(selected_word)):
    if current_word_state[i]=="_" and selected_word[i]==input_char:
      modified_word_state+=selected_word[i]
    else:
      modified_word_state+=current_word_state[i]
  return modified_word_state

selected_word="vision"
current_word_state="_ i _ i o _"
input_char='n'
output=change_current_word_state(selected_word,input_char, current_word_state)
print(output)