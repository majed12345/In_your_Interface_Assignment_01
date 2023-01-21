class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)

  def __contains__(self,member):
        return member in self.__myTeam
  def __iter__(self):
        return iter(self.__myTeam)

def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  #print (len(classmates))
  print('Tim' in classmates)
  print('Sam' in classmates)
  i = iter(classmates)
  for member in i:
      print(member,end=" ")
main()