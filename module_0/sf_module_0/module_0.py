import numpy as np
def score_game(game_core):
  count_ls = []
  np.random.seed(1) # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
  random_array = np.random.randint(1,101, size=(1000))
  for number in random_array:
    count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
  print(f"��� �������� ��������� ����� � ������� �� {score} �������")
  return(score)

def game_core_oem1(number):
  count = 1
  min_n = 1
  max_n = 101
  predict = np.random.randint(min_n,max_n)
  while number != predict:
    count += 1
    if number > predict:
      min_n = predict
      predict = np.random.randint(min_n,max_n)
    elif number < predict:
      max_n = predict
      predict = np.random.randint(min_n,max_n)
  return(count)

score_game(game_core_oem1)









import numpy as np
def score_game1(game_core1):
  count_ls = []
  np.random.seed(1) # ��������� RANDOM SEED, ����� ��� ����������� ��� �������������!
  random_array = np.random.randint(1,101, size=(1000))
  for number in random_array:
    count_ls.append(game_core1(number))
    score = int(np.mean(count_ls))
  print(f"��� �������� ��������� ����� � ������� �� {score} �������")
  return(score)

def game_core_oem2(number):
  count = 1
  min_n = 1
  max_n = 101
  predict = int(max_n/2)
  print('�������� ����� {}'.format(number))
  print('����',predict)
  while number != predict:
    count += 1
    if number > predict:
      min_n = predict
      predict = int(max_n-((max_n-min_n)/2))
      print('�����',min_n, '������',max_n, 'pr-',predict)
    elif number < predict:
      max_n = predict
      predict = int(max_n-((max_n-min_n)/2))
    print('�����',min_n,'������',max_n, count,'- �������, ����� -',predict)
  return(count)

score_game1(game_core_oem2)