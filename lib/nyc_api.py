
import requests
import json

class GetPrograms:

  def get_programs(self):
    URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

    response = requests.get(URL)
    pretty_content = (json.loads(response.content))
    return json.dumps(pretty_content, indent=4, sort_keys=True)


# programs = GetPrograms().get_programs()
# print(programs)

# Write a method program_school that returns a list of the schools or organizations that are running after school proograms.
# We use the hson library to parse the API response into a nicely formatted JSON
  def program_school(self):
    programs_list = []
    programs = json.loads(self.get_programs())
    for program in programs:
      programs_list.append(program["agency"])
    return programs_list
  
programs = GetPrograms()
program_schools = programs.program_school()

for school in set(program_schools):
  print(school)
