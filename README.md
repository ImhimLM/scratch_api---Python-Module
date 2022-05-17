# Scratch API

## How to Install

Download the file named `scratch_api.py`. Then in your Python file, use this to import it:
```
import scratch_api.py
```

## Instructions

### Users

Default user function:
```python
scratch_api.users(user, data)
```

List of texts that can replace `data` (Note that "Imhim_LM" is just an example username, it can be replaced with another existing username on Scratch):

User ID can be collected in the following way (with `userID`):
```python
scratch_api.users('Imhim_LM', 'userID')
```

Join Date can be collected in the following way (with `joinDate`), Returns date in YYYY-MM-DD:
```python
scratch_api.users('Imhim_LM', 'joinDate')
```

User's Country can be collected in the following way (with `country`):
```python
scratch_api.users('Imhim_LM', 'country')
```

User's Bio can be collected in the following way (with `bio`):
```python
scratch_api.users('Imhim_LM', 'bio')
```

User's Status (Or what Scratcher's call "What I'm Working On") can be collected in the following way (with `status`):
```python
scratch_api.users('Imhim_LM', 'status')
```

User's Follower Count can be collected in the following way (with `followerCount`):
```python
scratch_api.users('Imhim_LM', 'followerCount')
```

User's Following Count can be collected in the following way (with `followingCount`):
```python
scratch_api.users('Imhim_LM', 'followingCount')
```

Check if the User is part of the Scratch Team can be collected in the following way (with `scratchTeam`):
```python
scratch_api.users('Imhim_LM', 'scratchTeam')
```

### Projects

Default project function:
```python
scratch_api.projects(id, data)
```

List of texts that can replace `data` (Note that "660981552" is just an example project ID, it can be replaced with another existing project ID on Scratch):

Project Name can be collected in the following way (with `projectName`):
```python
scratch_api.projects('660981552', 'projectName')
```

Project Author can be collected in the following way (with `author`):
```python
scratch_api.projects('660981552', 'author')
```

Project Views can be collected in the following way (with `views`):
```python
scratch_api.projects('660981552', 'views')
```

Project Loves can be collected in the following way (with `loves`):
```python
scratch_api.projects('660981552', 'loves')
```

Project Favorites can be collected in the following way (with `favorites`):
```python
scratch_api.projects('660981552', 'favorites')
```

Project Remixes can be collected in the following way (with `remixes`):
```python
scratch_api.projects('660981552', 'remixes')
```

Project Instructions can be collected in the following way (with `instructions`):
```python
scratch_api.projects('660981552', 'instructions')
```

Project Notes and Credits can be collected in the following way (with `notesAndCredits`):
```python
scratch_api.projects('660981552', 'notesAndCredits')
```

Project's Comment Count can be collected in the following way (with `commentCount`):
```python
scratch_api.projects('660981552', 'commentCount')
```

Check if Project Comments are allowed can be collected in the following way (with `commentsAllowed`):
```python
scratch_api.projects('660981552', 'commentsAllowed')
```

## Errors

The following errors are shared between projects and users, meaning they are same:

`{error_code} Error, could not connect to "{link}"` - The username or project ID may be written incorrectly (If the error code is 404). For other error codes, the repl may have failed to connect to the API for some reason.

`Unknown data for "{data}". Please read the instructions in "README.md"` - The data written in the function is not existing or is not written properly.
