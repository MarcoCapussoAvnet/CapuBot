def makeLeague(teams):
  dayoff = {}
  dayoff["name"] = "DayOff"
  dayoff["rank"] = 0
  dayoff["id"] = 0
  if len(teams) % 2:
      teams.append(dayoff)
  n = len(teams)
  matchs = []
  fixtures = []
  return_matchs = []
  for fixture in range(1, n):
      for i in range(int(n/2)):
          matchs.append((teams[i], teams[n - 1 - i]))
          return_matchs.append((teams[n - 1 - i], teams[i]))
      teams.insert(1, teams.pop())
      fixtures.insert(int(len(fixtures)/2), matchs)
      fixtures.append(return_matchs)

      matchs = []
      return_matchs = []

  final_matches = [None]*len(fixtures)
  s = int(len(fixtures)/2)
  print(s)
  for i in range(s):
      if i%2:
          print(i)
          final_matches[i] = fixtures[i]
          final_matches[s+i] = fixtures[s+i]
      else:
          final_matches[i] = fixtures[s+i]
          final_matches[s+i] = fixtures[i]

  return final_matches