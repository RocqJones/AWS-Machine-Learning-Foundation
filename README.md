# AWS-Machine-Learning-Foundation (Udacity Scholarship)

An introduction to machine learning concepts.
* practical experience with software engineering for AWS machine learning, as well as deep learning.
* **AWS(Amazon Web Services)** is a secure cloud services platform, offering compute power, database storage, content delivery and other functionality to help businesses scale and grow.
* **Machine Learning** is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.

## Four organized course parts:
### Part 1 – Software Engineering Practices: Learn how to write well documented, modularized code.
#### a. Writing clean and modular code.
* **PRODUCTION CODE:** software running on production servers to handle live users and data of the intended audience. Note this is different from production quality code, which describes code that meets expectations in reliability, efficiency, etc., for production. Ideally, all code in production meets these expectations, but this is not always the case.<br>
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/productioncode.png" height="300" width="100%" ></a>

* **CLEAN:** readable, simple, and concise. A characteristic of production quality code that is crucial for collaboration and maintainability in software development.

#### b. Writing efficient code.
**Efficient Code** Optimizing code to be more efficient can mean making it:
* Execute faster
* Take up less space in memory/storage

* **MODULAR:** logically broken up into functions and modules. Also an important characteristic of production quality code that makes your code more organized, efficient, and reusable.<br>
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/modularcode.png" height="300" width="100%" ></a>

* **MODULE:** a file. Modules allow code to be reused by encapsulating them into files that can be imported into other files.

#### c. Code refactoring.
* **REFACTORING:** restructuring your code to improve its internal structure, without changing its external functionality. This gives you a chance to clean and modularize your program after you've got it working.

**NOTE:** Using ````vectorized operations```` and more ```efficient data structures``` can optimize your code.

#### d. Adding meaningful documentation.
* **DOCUMENTATION:** additional text or illustrated information that comes with or is embedded in the code of software.
  * Helpful for clarifying complex parts of code, 
  * making your code easier to navigate, and 
  * quickly conveying how and why different components of your program are used.
  
Several types of documentation can be added at different levels of your program:
* In-line Comments - line level ```# this is a comment```
* Docstrings - module and function level ```"""This fun explains population density"""```
```
def population_density(population, land_area):
    """Calculate the population density of an area."""
    return population / land_area
```
* Project Documentation - project level e.g ```README.md```
Project documentation is essential for getting others to understand why and how your code is relevant to them, whether they are potentials users of your project or developers who may contribute to your code. A great first step in project documentation is your README file. It will often be the first interaction most users will have with your project.

#### e Using version control.
**Version control** is a system that records changes to a file or set of files over time so that you can recall specific versions later.<br>
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/version_control.png" height="300" width="100%" ></a>
  
##### VC GIT commands.
##### Scenario 1
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/scenerio1.png" height="300" width="100%" ></a>

* You have a local version of this repository on your laptop, and to get the latest stable version, you pull from the develop branch.
  - Switch to the develop branch
  ```$ git checkout develop```
  
  - Pull latest changes in the develop branch
  ```$ git pull```
* When you start working on this demographic feature, you create a new branch for this called demographic, and start working on your code in this branch.
  - Create and switch to new branch called demographic from develop branch
  ```$ git checkout -b demographic```
  
  - Work on this new feature and commit as you go
  ```$ git commit -m 'added gender recommendations'```
  ```$ git commit -m 'added location specific recommendations'```
* However, in the middle of your work, you need to work on another feature. So you commit your changes on this demographic branch, and switch back to the develop branch.
  - Commit changes before switching
  ```$ git commit -m 'refactored demographic gender and location recommendations '```
  
  - Switch to the develop branch
  ```$ git checkout develop```
* From this stable develop branch, you create another branch for a new feature called friend_groups.
  Create and switch to new branch called friend_groups from develop branch
  ```$ git checkout -b friend_groups```
* After you finish your work on the friend_groups branch, you commit your changes, switch back to the development branch, merge it back to the develop branch, and push this to the remote repository’s develop branch.
  - Commit changes before switching
  ```$ git commit -m 'finalized friend_groups recommendations '```

  - Switch to the develop branch
  ```$ git checkout develop```

  - Merge friend_groups branch to develop
  ```$ git merge --no-ff friends_groups```

  - Push to remote repository
  ```$ git push origin develop```
 * Now, you can switch back to the demographic branch to continue your progress on that feature.
  Switch to the demographic branch
  ```$ git checkout demographic```
  
##### Scenario 2
* You check your commit history, seeing messages of the changes you made and how well it performed.
  - View log history
  ```$ git log```
* The model at this commit seemed to score the highest, so you decide to take a look. 
  - Checkout a commit
  ```$ git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560```
* Merging this back into the development branch, and pushing the updated recommendation engine.
  - Switch to develop branch
  ```$ git checkout develop```
  
  - Merge friend_groups branch to develop
  ```$ git merge --no-ff friend_groups```
  
  - Push changes to remote repository
  ```$ git push origin develop```
##### Scenario 3
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/scenerio3.png" height="300" width="100%" ></a>

* Commits your changes to the documentation branch, switches to the development branch, and pulls down the latest changes from the cloud on this development branch, including the change you merged previously for the friends group feature.
  - Commit changes on documentation branch
  ```$ git commit -m "standardized all docstrings in process.py"```

  - Switch to develop branch
  ```$ git checkout develop```

  - Pull latest changes on develop down
  ```$ git pull```
* Merges your documentation branch on the develop branch on your local repository, and then pushes your changes up to update the develop branch on the remote repository.
  - Merge documentation branch to develop
  ```$ git merge --no-ff documentation```

  - Push changes up to remote repository
  ```$ git push origin develop```
* After the team reviewed both of your work, they merge the updates from the development branch to the master branch. Now they push the changes to the master branch on the remote repository. These changes are now in production.
  - Merge develop to master
  ```$ git merge --no-ff develop```

  - Push changes up to remote repository
  ```$ git push origin master```
[More resources.](https://nvie.com/posts/a-successful-git-branching-model/)

### Part 2 – Software Engineering Practices: Learn to test your code and log best practices.
#### f. Testing
#### g. Logging
#### h. Code reviews

### Part 3 – Object-Oriented Programming: Learn about this programming style and prepare to write your own Python package.

### Part 4 – Introduction to Machine Learning on AWS: Learn about machine learning, generative AI, and AWS DeepComposer including how to build a custom Generative Adversarial Network.
