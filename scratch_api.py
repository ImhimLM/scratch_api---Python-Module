#### DATA ####

# Modules
import requests, re

# Variables and Lists
response = ''
responseJSON = ''

userLink = ''

#### API ####
def users(user, data):
        userLink = 'https://api.scratch.mit.edu/users/' + str(user)
        userLink2 = 'https://scratchdb.lefty.one/v3/user/info/' + str(user)

        response = requests.get(userLink)
        response2 = requests.get(userLink2)

        if response.status_code == 200:
                responseJSON = response.json()
                responseJSON2 = response2.json()

                responsePROFILE = responseJSON['profile']
                responseHISTORY = responseJSON['history']

                if data == 'userID':
                        userID = responsePROFILE['id']
                        return userID
                elif data == 'joinDate':
                        userJoined = responseHISTORY['joined']
                        userJoinedYear = str(userJoined[0] + userJoined[1] + userJoined[2] + userJoined[3])
                        userJoinedMonth = str(userJoined[5] + userJoined[6])
                        userJoinedDay = str(userJoined[8] + userJoined[9])
                        return userJoinedYear + '-' + userJoinedMonth + '-' + userJoinedDay
                elif data == 'country':
                        userCountry = responsePROFILE['country']
                        return userCountry
                elif data == 'bio':
                        bio = responsePROFILE['bio']
                        return bio
                elif data == 'status':
                        status = responsePROFILE['status']
                        return status
                elif data == 'followerCount':
                        userFollowers = responseJSON2['statistics']['followers']
                        return userFollowers
                elif data == 'followingCount':
                        userFollowing = responseJSON2['statistics']['following']
                        return userFollowing
                elif data == 'scratchTeam':
                        responseST = responseJSON['scratchteam']
                        return responseST
                else:
                        print('Unknown data for "' + str(data) + '". Please read the instructions in "README.md"')
                        quit()
        else:
                print(str(response.status_code) + ' Error, could not connect to "' + str(userLink) + '"')
                quit()

def projects(id, data):
        projectLink = 'https://api.scratch.mit.edu/projects/' + id
        projectLink2 = 'https://scratchdb.lefty.one/v2/project/info/id/' + str(id)

        response = requests.get(projectLink)
        response2 = requests.get(projectLink2)

        if response.status_code == 200:
                responseJSON = response.json()
                responseJSON2 = response2.json()

                projectAuthorInfo = responseJSON['author']
                projectStats = responseJSON['stats']

                if data == 'projectName':
                        project = responseJSON['title']
                        return project
                elif data == 'author':
                        projectAuthor = projectAuthorInfo['username']
                        return projectAuthor
                elif data == 'views':
                        projectViews = projectStats['views']
                        return projectViews
                elif data == 'loves':
                        projectLoves = projectStats['loves']
                        return projectLoves
                elif data == 'favorites':
                        projectFavorites = projectStats['favorites']
                        return projectFavorites
                elif data == 'remixes':
                        projectRemixes = projectStats['remixes']
                        return projectRemixes
                elif data == 'instructions':
                        projectInstructions = responseJSON['instructions']
                        return projectInstructions
                elif data == 'notesAndCredits':
                        projectNAC = responseJSON['description']
                        return projectNAC
                elif data == 'commentCount':
                        projectCommentCount = responseJSON2['statistics']['comments']
                        return projectCommentCount
                elif data == 'commentsAllowed':
                        projectCommentsAllowed = responseJSON2['comments_allowed']
                        if projectCommentsAllowed == 1:
                                projectCommentsAllowed = True
                        elif projectCommentsAllowed == 0:
                                projectCommentsAllowed = False
                        return projectCommentsAllowed
                else:
                        print('Unknown data for "' + str(data) + '". Please read the instructions in "README.md"')
                        quit()
        else:
                print(str(response.status_code) + ' Error, could not connect to "' + str(projectLink) + '"')
                quit()