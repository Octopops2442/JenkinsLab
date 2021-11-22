import main

def testCases() :
  assert main.add(12, 18) == 30
  
  assert main.add(100, 1500) == 1600

if __name__ == '__main__':
  print(testCases())
