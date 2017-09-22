import json

class Photo(object):
    def __init__(self, photo_diction):
        self.owner = {
            'username': photo_diction['owner']['username'],
            'realname': photo_diction['owner']['realname'],
            'location': photo_diction['owner']['location']
        }

        self.title = photo_diction['title']['_content']
        # self.title = 'Photo1'

        # initializing tags by looping through the list of tags
        self.tags = []
        tag_list = photo_diction['tags']['tag']
        for tag_diction in tag_list:
            tag_raw = tag_diction['raw']
            self.tags.append(tag_raw)
        # self.tags = ['Nature', 'Mist', 'Mountain']

        self.id = photo_diction['id']
        self.date_taken = photo_diction['dates']['taken']
        self.url = photo_diction['urls']['url'][0]['_content']
        self.license = photo_diction['license']

    def __str__(self):
        return self.title

    def __repr__(self):
        return 'ID: {}, Title: {}, URL: {}'.format(self.id, self.title, self.url)
        # return 'Title: {1}, ID: {0}, URL: {2}'.format(self.id, self.title, self.url)

    def __contains__(self, test_string):
        # enable 'in' operator on this object/class
        return (test_string in self.tags
            or test_string in self.title)


# with open(filename, mode) as f
# with automatically closes the file outside of its indent (scope)
with open("sample_diction.json", "r") as f:
    f_string = f.read()
    response_diction = json.loads(f_string)

pd = response_diction['photo']
photo = Photo(pd)
print(photo) # print(str(photo))
print(repr(photo))
print(isinstance(photo, Photo))

if "Nature" in photo:
    print('Nature tag exists')

if "Kaboom" in photo:
    print('Kaboom tag exists')

if "Pho" in photo:
    print('Pho exists in photo')
