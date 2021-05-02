import requests
import json
import time
import base64

count = 0


def get_all_buildings(school_name):
    school = getSchoolInfo(school_name)
    location = school["location"]
    APIKEY = "AIzaSyCsYNcoCH1QtcagcbPzfwOBetYuv5OA-cs"
    buildings = []

    def findPlaces(loc=(location["lat"], location["lng"]), pagetoken=None):
        lat, lng = loc
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{lng}&rankby=distance&key={APIKEY}{pagetoken}".format(
            lat=lat,
            lng=lng,
            APIKEY=APIKEY,
            pagetoken="&pagetoken=" + pagetoken if pagetoken else "")
        response = requests.get(url)
        res = json.loads(response.text)

        for result in res["results"]:
            building_name = result["name"]
            lat = result["geometry"]["location"]["lat"]
            lng = result["geometry"]["location"]["lng"]
            buildings.append({
                "title": building_name,
                "description1": "This is the " + building_name + '.',
                "description2": "",
                "lat": lat,
                "lng": lng,
                "heading": 34,
                "pitch": 10,
            })
        pagetoken = res.get("next_page_token", None)

        return pagetoken

    pagetoken = None

    while True:
        pagetoken = findPlaces(pagetoken=pagetoken)
        import time
        time.sleep(3)
        if not pagetoken:
            break

    result = {}
    result["school_name"] = school["name"]
    result["address"] = school["formatted_address"]
    result["location"] = school["location"]
    result["buildings"] = buildings

    return result


def getSchoolInfo(string):
    request = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key=AIzaSyCsYNcoCH1QtcagcbPzfwOBetYuv5OA-cs&input=' + string + '&inputtype=textquery&fields=name,formatted_address,geometry'
    result = requests.get(request)
    result = json.loads(result.text)
    candidates = result["candidates"]

    rightCandidate = ''
    for candidate in candidates:
        if candidate["name"] == string:
            rightCandidate = candidate

    if rightCandidate == '':
        rightCandidate = candidates[0]

    geo = rightCandidate["geometry"]

    ans = {}
    ans["name"] = rightCandidate["name"]
    ans["formatted_address"] = rightCandidate["formatted_address"]
    ans["location"] = geo["location"]
    return ans


def generateSchoolList(li):
    global count
    timestamp = time.time()
    array = {}
    array["timestamp"] = timestamp
    array["data"] = []

    for school in li:
        answer = get_all_buildings(school)
        array['data'].append(answer)
        count += 1
        print(count, school)
    return array


'''execute part '''
######################################################################
school_list = [
    "Harvard University",
    "Stanford University",
    "Massachusetts Institute of Technology (MIT)",
    "University of California, Berkeley (UCB)",
    "Columbia University",
    "University of California, Los Angeles (UCLA)",
    "Yale University",
    "University of Pennsylvania",
    "Princeton University",
    "Cornell University",
    "New York University (NYU)",
    "University of Chicago",
    "Duke University",
    "Johns Hopkins University",
    "University of Southern California",
    "Northwestern University",
    "Carnegie Mellon University",
    "University of Michigan",
    "California Institute of Technology (Caltech)",
    "Brown University",
    "Boston University",
    "Rice University",
    "Georgetown University",
    "University of Washington",
    "University of Texas at Austin",
    "University of California, San Diego (UCSD)",
    "Emory University",
    "University of California, Davis (UCD)",
    "Washington University in St. Louis",
    "University of Rochester",
    "Vanderbilt University",
    "Georgia Institute of Technology (Georgia Tech)",
    "University of Illinois at Urbana-Champaign",
    "George Washington University",
    "Tufts University",
    "University of Florida",
    "Dartmouth College",
    "University of North Carolina, Chapel Hill",
    "University of Miami",
    "University of Notre Dame",
    "Rutgers University - New Brunswick",
    "University of California, Irvine (UCI)",
    "Case Western Reserve University",
    "University of Illinois, Chicago (UIC)",
    "Stony Brook University, State University of New York",
    "University at Buffalo SUNY",
    "Pennsylvania State University",
    "Boston College",
    "University of Maryland, College Park",
    "University of Virginia",
    "Syracuse University",
    "University of Wisconsin-Madison",
    "Purdue University",
    "Northeastern University",
    "University of Minnesota, Twin Cities",
    "Michigan State University",
    "Brandeis University",
    "The Ohio State University",
    "Drexel University",
    "University of Massachusetts Amherst",
    "Temple University",
    "North Carolina State University",
    "University of Colorado at Boulder",
    "Lehigh University",
    "Rensselaer Polytechnic Institute",
    "University of Hawaii at Manoa",
    "Tulane University",
    "Howard University",
    "University of Arizona",
    "University of Maryland, Baltimore County",
    "Binghamton University SUNY",
    "Illinois Institute of Technology",
    "University of Pittsburgh",
    "New Jersey Institute of Technology (NJIT)",
    "University of California, Santa Barbara (UCSB)",
    "University of the Pacific",
    "Texas A&M University",
    "University of Denver",
    "University of Massachusetts, Boston",
    "College of William & Mary",
    "Florida State University",
    "San Diego State University",
    "University of Connecticut",
    "Virginia Commonwealth University",
    "Indiana University Bloomington",
    "Worcester Polytechnic Institute",
    "University of Houston",
    "University of San Francisco",
    "The University of Georgia",
    "University of Oklahoma, Norman",
    "Arizona State University, Tempe",
    "Wake Forest University",
    "Southern Methodist University",
    "Andrews University",
    "Universiof California, Santa Cruz (UCSC)",
    "University of Oregon",
    "University of Texas Dallas",
    "Santa Clara University",
    "University of Louisville",
    "George Mason University",
    "Rutgers - The State University of New Jersey, Newark",
    "Virginia Polytechnic Institute (Virginia Tech)",
    "University of California, Merced (UC Merced)",
    "University of California, Riverside (UC Riverside)",
    "California State University Maritime Academy",
    "California Polytechnic State University",
    "California State Polytechnic University, Pomona",
    "California State University, Bakersfield",
    "California State University Channel Islands",
    "California State University, Chico",
    "California State University, Dominguez Hill",
    "California State University, East Bay",
    "California State University, Fresno",
    "California State University, Fullerton",
    "California State University, Long Beach",
    "California State University, Los Angeles",
    "California State University, Monterey Bay",
    "California State University, Northridge",
    "California State University, Sacramento",
    "California State University, San Bernardino",
    "California State University San Marcos",
    "California State University, Stanislaus",
    "Humboldt State University",
    "San Diego State University",
    "San Francisco State University",
    "San Jose State University",
    "Sonoma State University",
    "Academy of Art University	San Francisco	",
    "Alliant International University",
    "American Heritage University of Southern California",
    "American Jewish University",
    "Anaheim University",
    "Antioch University Los Angeles",
    "ArtCenter College of Design",
    "Azusa Pacific University	",
    "Berean Bible College",
    "Biola University",
    "Brandman University",
    "California Baptist University	Riverside",
    "California College of the Arts",
    "California College San Diego",
    "California Health Sciences University",
    "California Institute of Integral Studies",
    "California Institute of Technology",
    "California Institute of the Arts",
    "California Lutheran University",
    "California Miramar University",
    "California South Bay University",
    "California University of Management and Technology",
    "Cambridge College",
    "Chapman University",
    "Charles R. Drew University of Medicine and Science",
    "Claremont Graduate University",
    "Claremont Lincoln University",
    "Claremont McKenna College",
    "Cogswell Polytechnical College",
    "Concordia University Irvine",
    "The Culinary Institute of America at Greystone	",
    "Deep Springs College",
    "DeVry University",
    "Dominican University of California",
    "Epic Bible College",
    "Fashion Institute of Design & Merchandising",
    "Fielding Graduate University",
    "Frederick S. Pardee RAND Graduate School",
    "Fresno Pacific University	Fresno",
    "Fuller Theological Seminary",
    "Golden Gate University",
    "Graduate Theological Union",
    "Gurnick Academy",
    "Harvey Mudd College",
    "Holy Names University",
    "Hope International University",
    "Hult International Business School",
    "Humphreys University",
    "Imago Dei College",
    "John Paul the Great Cathol",
    "Keck Graduate Institute",
    "La Sierra University",
    "Laguna College of Art and Design",
    "Life Pacific College",
    "Lincoln University",
    "Loma Linda University",
    "Los Angeles College of Music",
    "Loyola Marymount University",
    "Make School",
    "Marymount California University",
    "The Master's University",
    "Menlo College",
    "Mills College",
    "Middlebury Institute of International Studies at Monterey	",
    "The Minerva Project	San Francisco",
    "Mount St. Mary's University	",
    "National University",
    "New York Film Academy	",
    "NewSchool of Architecture and Design",
    "Northwestern Polytechnic University",
    "Notre Dame de Namur University",
    "Oak Valley College",
    "Occidental College",
    "Oikos University",
    "Otis College of Art and Design",
    "Pacific Lutheran Theological Seminary",
    "Pacific Oaks College",
    "Pacific School of Religion",
    "Pacific Union College",
    "Pacifica Graduate Institute",
    "Palmer College of Chiropractic",
    "Palo Alto University",
    "Patten University",
    "Pepperdine University",
    "Pitzer College",
    "Point Loma Nazarene University",
    "Pomona College",
    "Providence Christian College",
    "Saint Mary's College of California",
    "Samuel Merritt University",
    "San Diego Christian College",
    "San Diego University for Integrative Studies",
    "San Francisco Institute of Architecture",
    "San Joaquin College of Law",
    "Santa Clara University",
    "Saybrook University",
    "Scripps College",
    "Simpson University",
    "Soka University of America",
    "Southern California Institute of Architecture",
    "Southern States University",
    "Southwestern Law School",
    "Stanford University",
    "Starr King School for Ministry",
    "Thomas Aquinas College",
    "Touro University California",
    "Trident University International",
    "University of Antelope Valley",
    "University of La Verne",
    "University of Redlands",
    "University of San Diego",
    "University of San Francisco",
    "University of Southern California	Los Angeles",
    "University of the Pacific",
    "University of the People",
    "University of the West",
    "University of West Los Angeles",
    "Vanguard University",
    "Western Seminary - Sacramento Campus",
    "Western Seminary - San Jose Campus",
    "Western State College of Law",
    "Western University of Health Sciences",
    "Westcliff University",
    "Westmont College",
    "Whittier College",
    "William Jessup University",
    "Woodbury University",
    "Zaytuna College",
    "Illinois Institute of Technology",
]


# Add the descriptions
def processing(inp):
    data = inp
    for school in data["data"]:
        for i in range(len(school["buildings"])):
            if i + 1 == len(school["buildings"]):
                school['buildings'][i][
                    'description2'] = "You have reached the last stop of the tour. Hope you enjoyed. Have a wonderful day!"
            else:
                school['buildings'][i][
                    'description2'] = "Your next stop is " + school[
                        'buildings'][i + 1]['title'] + '.'
    return data


def check_repeat(inp):
    data = inp
    for school in data["data"]:
        li = []
        index_factor = 0
        for i in range(len(school["buildings"]) - 1):
            lat = float('%.4f' % school['buildings'][i - index_factor]['lat'])
            lng = float('%.4f' % school['buildings'][i - index_factor]['lng'])
            school['buildings'][i - index_factor]['lat'] = lat
            school['buildings'][i - index_factor]['lng'] = lng
            if {lat: lng} not in li:
                li.append({lat: lng})
            else:
                school['buildings'].pop(i - index_factor)
                index_factor += 1
        print(school['school_name'], index_factor)
    return data


result = generateSchoolList(school_list)
temporary = check_repeat(result)
final = processing(temporary)
with open('data5.json', 'w') as outfile:
    json.dump(final, outfile)
"""
dumped parts
"""
# from github import Github
# from github import InputGitTreeElement

# def pushToRepo():
#   user = "charliespy"
#   password = "Monkeysun01"
#   g = Github(user,password)
#   print(g)
#   repo = g.get_user().get_repo("virtualTourProject")
#   print(repo)

#   file_list = [
#       'data.json'
#   ]

#   file_names = [
#       'data.json'
#   ]
#   commit_message = 'first commit from python'
#   master_ref = repo.get_git_ref('heads/master')
#   master_sha = master_ref.object.sha
#   base_tree = repo.get_git_tree(master_sha)
#   element_list = list()
#   for i, entry in enumerate(file_list):
#       with open(entry) as input_file:
#           data = input_file.read()
#       if entry.endswith('.png'):
#           data = base64.b64encode(data)
#       element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
#       element_list.append(element)
#   tree = repo.create_git_tree(element_list, base_tree)
#   parent = repo.get_git_commit(master_sha)
#   commit = repo.create_git_commit(commit_message, tree, [parent])
#   master_ref.edit(commit.sha)
