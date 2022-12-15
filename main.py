def count_batteries_by_usage(cycles):
  lowcount = 0
  mediumCount = 0
  highCount = 0


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  print("lowCount")
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  for i in counts:
      if(counts < 310):
          lowCount += 1
      if(counts >= 310 and counts<930):
          mediumCount += 1
      if(counts >= 930):
          highCount +=1
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_number_of_cycles()
