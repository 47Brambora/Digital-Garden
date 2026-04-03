# Guidelines for Contributing  

Česká verze: [CONTRIBUTING.md](./docs/CS/CONTRIBUTING.md)  

Thank you for wanting to add new plants to our beautiful garden or take care of the older ones.  
To ensure that gardening is enjoyable for everyone, please follow these guidelines.


## 1. No Duplicates  

If a similar plan already exist in the garden, try to expand on it or approach it differently.  

**Example:**
Tulip → Yellow tulip

When editing an existing plant, try to preserve its "family" (varieties, subspecies).


## 2. Write Your Own Code  

Only add code that you understand and that you wrote yourself.  
Inspiration is fine - copying is not!  


## 3. Sing Your Code  

Add the following comment at the beginning of the file.  

`#Author: YourName (email@example.com)`  

The email address is optional, but it's useful (e.g., for agreeing on changes).  


## 4. Name The Plant  

Every plant should have a name.  
If similar one already exist, create a subspecies or variant.  


## 5. Keep Things Organized  

 - Place flowers in the correct folder based on their technology  
 - If you're not sure, leave it in the root folder and note it in the PR  
 - New flower types → create a new folder  


## 6. Workflow  

### 1. Create a new branch  

Each change should have its own branch:  
`<action>/<technology>-<flower>`  
For example:  
`git checkout -n planting/css-red-tulip`  

### 2. Add a flower  

Save it to the correct folder.  

### 3. Sing your work  

Add the author to beginning of the file.  

### 4. Take a screenshot  

Create an image (ideally a .png) and place it in `gallery/images/`  

### 5. Update the gallery  

Add the following to `gallery/GALLERY.md`:

 - image  
 - name  
 - technology used  

### 7. Open a pull request  

Give a brief description of:

 - what you’re adding
 - why (if it’s a modification)
 - how it works
 - tag the author of the original flower if applicable


## 7. Editing Other People's Flowers  

Want to edit someone else's flower?  

 - Try contacting author  
 - Describe what you want to change and why  
 - If the agree, you will be listed as a **Co-Author**

If the author:

 - does not agree  
 - or is unavailable  

→ Create a new subspecies.


## 8. AI  

The use of AI is permitted, but:  

 - You should understand what you're adding  
 - Try to create as much of your own work as possible  
 - Use AI only as a tool  


## 9. Pull Requests  

In every PR, include:  

 - what you're adding or changing  
 - why (if it's a change)
 - how it works  
 - whether you're modifying the existing structure  
 - tag the author (if you're editing their code)  


## 10. Commit Messages  

Use gardening prefixes to keep your history clear and in gardening terms.

 - `plant:` — a new plant or a new file  
 - `grow:` — improvements to an existing plant  
 - `prune:` — cleanup, deletion, fixes, refactoring
 - `gallery:` — adding or editing images or GALLERY.md  
 - `structure:` — changes to directories, moves, adding .gitignore, etc.
 - `docs:` — editing documentation (README, CONTRIBUTING, ...)  

**Example:** `plant: add red-tulip.html (css)`


## 11. Branch Naming  

Each change should have its own branch. We use a simple and consistent naming system:

`<action>/<technology>-<plant>`  

### Action Type  

- `planting` — adding a new plant  
- `growing` — improving an existing plant  
- `pruning` — cleanup, deletion, fixes  
- `structuring` — changes to folders, moves  
- `documenting` — documentation updates  
- `gallery` — work with images and GALLERY.md  

### Branch Examples

- `planting/css-tulip-yellow`  
- `growing/python-rose-red`  
- `pruning/js-daisy-cleanup`  
- `structuring/svg-folder-move`  
- `documenting/docs-readme-update`  
- `gallery/images-tulip-add`


---


And now all that’s left is to let the garden grow
