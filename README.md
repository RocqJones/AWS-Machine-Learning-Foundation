# AWS-Machine-Learning-Foundation (From my Udacity Scholarship)

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
#### f. Testing.
* Testing your code is essential before deployment. It helps you catch errors and faulty conclusions before they make any major impact.
##### Testing And Data Science
 
 * **UNIT TEST:** a type of test that covers a “unit” of code, usually a single function, independently from the rest of the program.
  - The advantage of unit tests is that they are isolated from the rest of your program, and thus, no dependencies are involved.
 * **Unit Testing tools.**
  - [Pytest](https://docs.pytest.org/en/latest/) - Name testfiles as ```test_example.py``` and also all funtions should be defined as ```def test_example_fun():```
  
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/test1.png" height="400" width="100%" ></a>
  
 * **TEST DRIVEN DEVELOPMENT:** a development process where you write tests for tasks before you even write the code to implement those tasks.
  * Test driven development for data science is relatively new and has a lot of experimentation and breakthroughs appearing, which you can learn more about in the resources below.
   - [Data Science TDD](https://medium.com/uk-hydrographic-office/test-driven-development-is-essential-for-good-data-science-heres-why-db7975a03a44)
   - [Testing Your Code (general python TDD)](https://docs.python-guide.org/writing/tests/)
   
#### g. Logging.
 * Logging is valuable for understanding the events that occur while running your program. 
 **For example**, if you run your model over night and see that it's producing ridiculous results the next day, log messages can really help you understand more about the context in which this occurred. 
 ##### Appropriate level for logging
  - **DEBUG** - level you would use for anything that happens in the program.
  - **ERROR** - level to record any error that occurs
  - **INFO** - level to record all actions that are user-driven or system specific, such as regularly scheduled operations
 
#### h. Code reviews.
 * [Code reviews](https://github.com/lyst/MakingLyst/tree/master/code-reviews) benefit everyone in a team to promote best programming practices and prepare code for production. 
 * [Code Review Best Practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html)
 ##### Questions to Ask Yourself When Conducting a Code Review
   - Is the code clean and modular?
   - Is the code efficient?
   - Is documentation effective?
   - Is the code well tested?
   - Is the logging effective?
  
 * Example of a good code review
 ```
 BAD: Make model evaluation code its own module - too repetitive.

 BETTER: Make the model evaluation code its own module. This will simplify models.py to be less repetitive and focus primarily on building models.

 GOOD: How about we consider making the model evaluation code its own module? This would simplify models.py to only include code for building models.
 ```

### Part 3 – Object-Oriented Programming: Learn about this programming style and prepare to write your own Python package.
#### Why Object-Oriented Programming?
**Object-oriented programming** has a few benefits over procedural programming, which is the programming style you most likely first learned.

* object-oriented programming allows you to create large, modular programs that can easily expand over time;
* object-oriented programs hide the implementation from the end-user.
Consider Python packages like [Scikit-learn](https://scikit-learn.org/stable/), [pandas](https://pandas.pydata.org/), and [NumPy](https://numpy.org/). These are all Python packages built with object-oriented programming.

When you train a machine learning algorithm with Scikit-learn, you don't have to know anything about how the algorithms work or how they were coded. You can focus directly on the modeling.
##### Objective
Building a Python package using object-oriented programming.
#### a) Procedural vs Object-Oriented Programming.
**Procedural programming** is a programming paradigm, derived from structured programming, based on the concept of the procedure call. Procedures, also known as routines, subroutines, or functions, simply contain a series of computational steps to be carried out.

**Object-oriented programming** is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields, and code, in the form of procedures. A feature of objects is an object's procedures that can access and often modify the data fields of the object with which they are associated.
 * **Note:** Object has a Characteristics/Attributes and Actions.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/oop1.png" height="400" width="100%" ></a>

#### b) Class, object, method, attribute.
 * **Class** - a blueprint consisting of methods and attributes
 * **Object** - an instance of a class. It can help to think of objects as something in the real world like a yellow pencil, a small dog etc
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/oop2.png" height="400" width="100%" ></a> 
 * **Attribute**(Characteristics) - a descriptor or characteristic. Examples would be color, length, size, etc. These attributes can take on specific values like blue, or 3 inches.
 * **Method** - an action that a class or object could take.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/oop3.png" height="400" width="100%" ></a>
 * **Encapsulation** - You can combine functions and data all into a single entity in OOP, this single entity is called a class. Encapsulation allows you to hide implementation details much like how the scikit-learn package hides the implementation of machine learning algorithms.

#### What is self?
```
shirt_one = Shirt('red', 'S', 'short-sleeve', 15)
short_two = Shirt('yellow', 'M', 'long-sleeve', 20)

def change_price(self, new_price):
    self.price = new_price

shirt_one.change_price(12)
```
```Self``` tells Python where to look in the computer's memory for the shirt_one object. And then Python changes the price of the shirt_one object. When you call the change_price method, shirt_one.change_price(12), self is implicitly passed in.

#### Inheritance.
Inheritance is the mechanism of basing an object or class upon another object or class, retaining similar implementation. Also defined as deriving new classes from existing ones such as super class or base class and then forming them into a hierarchy of classes.
#### List of resources for advanced Python object-oriented programming topics.
* [**Class methods, instance methods, and static methods**](https://realpython.com/instance-class-and-static-methods-demystified/) - these are different types of methods that can be accessed at the class or object level
* [**Class attributes vs instance attributes**](https://www.python-course.eu/python3_class_and_instance_attributes.php) - you can also define attributes at the class level or at the instance level
* [**Multiple inheritance, mixins**](https://easyaspython.com/mixins-for-fun-and-profit-cb9962760556) - A class can inherit from multiple parent classes
* [**Python decorators**](https://realpython.com/primer-on-python-decorators/) - Decorators are a short-hand way for using functions inside other functions

[Objective project here](https://github.com/RocqJones/distributions_gauss_bi)

### Part 4 – Introduction to Machine Learning on AWS: Learn about machine learning, generative AI, and AWS DeepComposer including how to build a custom Generative Adversarial Network.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-learning.png" height="300" width="100%" ></a> 
#### Why AWS?
* AWS offers the broadest and deepest set of AI and ML services with unmatched flexibility.
* You can accelerate your adoption of machine learning with AWS SageMaker. Models that previously took months and required specialized expertise can now be built in weeks or even days.
* AWS offers the most comprehensive cloud offering optimized for machine learning.
* More machine learning happens at AWS than anywhere else.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-AI-service.jpg" height="600" width="100%" ></a>

##### Amazon Code Guru.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-code-guru.jpg" height="300" width="100%" ></a>
##### Getting started.
* **a. AWS DeepLens:** deep learning and computer vision.
* **b. AWS DeepRacer and the AWS DeepRacer League:** reinforcement learning.
* **c. AWS DeepComposer:** Generative AI.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-deep.png" height="300" width="100%" ></a>

#### Machine Learning Techniques
##### a. Supervised Learning: 
Models are presented wit input data and the desired results. The model will then attempt to learn rules that map the input data to the desired results.
##### b. Unsupervised Learning: 
Models are presented with datasets that have no labels or predefined patterns, and the model will attempt to infer the underlying structures from the dataset. Generative AI is a type of unsupervised learning.
##### c. Reinforcement learning: 
The model or agent will interact with a dynamic world to achieve a certain goal. The dynamic world will reward or punish the agent based on its actions. Overtime, the agent will learn to navigate the dynamic world and accomplish its goal(s) based on the rewards and punishments that it has received.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/types-of-ml.jpg" height="300" width="100%" ></a>

#### Generative AI.
Generative AI is one of the biggest recent advancements in artificial intelligence technology because of its ability to create something new. It opens the door to an entire world of possibilities for human and computer creativity, with practical applications emerging across industries, from turning sketches into images for accelerated product development, to improving computer-aided design of complex objects. It takes two neural networks against each other to produce new and original digital works based on sample inputs.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/generative-ai.jpg" height="300" width="100%" ></a>

#### AWS DeepComposer and Generative AI.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-dcomposer.png" height="300" width="100%" ></a>
AWS Deep Composer uses Generative AI, or specifically **Generative Adversarial Networks (GANs)**, to generate music. GANs pit 2 networks, a generator and a discriminator, against each other to generate new content.
##### Adding some more light on Generator and Discriminator:
* **The generator* plays and generates the music. 
* **The discriminator** judges the music created by the generator and coaches the generator to improve for future iterations. 
* So a generator, trains, practices, and tries to generate music, and then the discriminator coaches them to produced more polished music.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-mle-orchestra-metaphor.jpg" height="300" width="100%" ></a>

##### AWS DeepComposer Workflow.
- Use the AWS DeepComposer keyboard or play the virtual keyboard in the AWS DeepComposer console to input a melody.
- Use a model in the AWS DeepComposer console to generate an original musical composition. You can choose from jazz, rock, pop, symphony or Jonathan Coulton pre-trained models or you can also build your own custom genre model in Amazon SageMaker.
- Publish your tracks to SoundCloud or export MIDI files to your favorite Digital Audio Workstation (like Garage Band) and get even more creative.
#### Let's explore DeepComposer’s music studio, and we’ll end by generating a composition with a 4 part accompaniment.
1. To get to the main AWS DeepComposer console, navigate to AWS DeepComposer. Make sure you are in the US East-1 region.
Once there, click on Get started
2. In the left hand menu, select Music studio to navigate to the DeepComposer music studio.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/1studio.png" height="300" width="100%" ></a>
3. To generate music you can use a virtual keyboard or the physical AWS DeepComposer keyboard. For this lab, we’ll use the virtual keyboard.
4. To view sample melody options, select the drop down arrow next to Input, Next, choose a model to apply to the melody by clicking Select model
From the sample models and then click Select model, Next, select Generate composition. The model will take the 1 track melody and create a multitrack composition (in this case, it created 4 tracks)
5. Click play to hear the output.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/2studio.png" height="300" width="100%" ></a>

#### Model Training with AWS DeepComposer.
Each iteration of the training cycle is called an **epoch**. The model is trained for thousands of epochs.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/GANS1.png" height="300" width="100%" ></a>
##### Loss Functions.
The **measure of an error, given a set of weights**.
* In machine learning, the goal of iterating and completing epochs is to improve the output or prediction of the model.
  - Any **output** that **deviates from the ground truth** is referred to as an **error**. 
  - **Weights** represent how important an associated feature is to **determining the accuracy of a prediction**, and loss functions are used to update the weights after every iteration. 
  - As the weights update, the model improves making less and less errors. 
* Convergence happens once the loss functions stabilize.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/GANS2.png" height="300" width="100%" ></a>
**NOTE:** GAN loss functions have many fluctuations early on due to the “adversarial” nature of the generator and discriminator.

##### AWS DeepComposer Under the Hood.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/under1.png" height="300" width="100%" ></a>
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/under2.png" height="300" width="100%" ></a>

#### Training Architecture.
1. User launch a training job from the AWS DeepComposer console by selecting hyperparameters and data set filtering tags.
2. The backend consists of an API Layer (API gateway and lambda) write request to DynamoDB.
3. Triggers a lambda function that starts the training workflow.
4. It then uses AWS Step Funcitons to launch the training job on Amazon SageMaker.
5. Status is continually monitored and updated to DynamoDB.
6. The console continues to poll the backend for the status of the training job and update the results live so users can see how the model is learning.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-mle-train-arch.png" height="600" width="100%" ></a>

##### How to measure the quality of the music we’re generating:
* We can monitor the loss function to make sure the model is converging.
* We can check the **similarity index** to see how close is the model to mimicking the style of the data. When the graph of the similarity index smoothes out and becomes less spikey, we can be confident that the model is converging.
* We can listen to the music created by the generated model to see if it's doing a good job. The musical quality of the model should improve as the number of training epochs increases.

##### Challenges with GANs
* Clean datasets are hard to obtain.
* Not all melodies sound good in all genres.
* Convergence in GAN is tricky – it can be fleeting rather than being a stable state.
* Complexity in defining meaningful quantitive metrics to measure the quality of music created.

### Generative AI
Generative AI has been described as one of the most promising advances in AI in the past decade by the MIT Technology Review.
* Generative AI opens the door to an entire world of creative possibilities with practical applications that turning sketches into images for accelerated product development, to improving computer-aided design of complex objects.
 - For example, Glidewell Dental is training a generative adversarial network adept at constructing detailed 3D models from images. One network generates images and the second inspects those images. This results in an image that has even more anatomical detail than the original teeth they are replacing.
* Generative AI enables computers to learn the underlying pattern associated with a provided input (image, music, or text), and then they can use that input to generate new content. 
 - Examples of Generative AI techniques include Generative Adversarial Networks (GANs), Variational Autoencoders, and Transformers.

#### What are GANs (Generative Adversarial Networks)?
GANs, a generative AI technique, pit 2 networks against each other to generate new content. The algorithm consists of two competing networks: a **generator** and a **discriminator**.
* **A generator** is a convolutional neural network (CNN) that learns to create new data resembling the source data it was trained on.
* **A discriminator** is another convolutional neural network (CNN) that is trained to differentiate between real and synthetic data.

**The generator and the discriminator are trained in alternating cycles such that the generator learns to produce more and more realistic data while the discriminator iteratively gets better at learning to differentiate real data from the newly created data.**

##### A scheme Scheme representing AWS DeepComposer GAN
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/aws-deepcomoserr-gan-schema.png" height="300" width="100%" ></a>
As a conductor provides feedback to make an orchestra sound better, a GAN's discriminator gives the generator feedback on how to make its data more realistic.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/gan-representation.png" height="300" width="100%" ></a>

#### Introduction to U-Net Architecture.
##### Training a machine learning model using a dataset of Bach compositions.
* AWS DeepComposer uses GANs to create realistic accompaniment tracks. When you provide an input melody, such as twinkle-twinkle little star, using the keyboard U-Net will add three additional piano accompaniment tracks to create a new musical composition.
* The U-Net architecture uses a publicly available dataset of Bach’s compositions for training the GAN. In AWS DeepComposer, the generator network learns to produce realistic Bach-syle music while the discriminator uses real Bach music to differentiate between real music compositions and newly created ones.
* **The U-Net architecture learns from symphonies to create music.**
##### How U-Net based model interprets music.
* Modern GAN-based models instead treat music as a series of images, and can therefore leverage existing techniques within the computer vision domain.
* In AWS DeepComposer, we **represent music as a two-dimensional matrix** (also referred to as a piano roll) with **“time”** on the horizontal axis and **“pitch”** on the vertical axis. 
 - You might notice this representation looks similar to an image. 
 - A one or zero in any particular cell in this grid indicates if a note was played or not at that time for that pitch.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/piano-rolls.png" height="400" width="100%" ></a>

#### Model Architecture - How the generator and discriminator networks used in AWS DeepComposer.
##### Generator.
The generator network used in AWS DeepComposer is adapted from the U-Net architecture, a popular **convolutional neural network (CNN)** that is used extensively in the computer vision domain. 
*The network consists of an **1. “encoder”** that maps the single track music data (represented as piano roll images) to a relatively lower dimensional **2. “latent space“** and a **3. ”decoder“** that maps the latent space back to multi-track music data.*

Here are the inputs provided to the generator:
 * Single-track piano roll: A single melody track is provided as the input to the generator.
 * Noise vector: A latent noise vector is also passed in as an input and this is responsible for ensuring that there is a flavor to each output generated by the generator, even when the same input is provided.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/u-net.png" height="600" width="100%" ></a>
***NOTE: The encoding layers of the generator on the left side and decoder layer on on the right side are connected to create a U-shape, thereby giving the name U-Net to this architecture***

##### Discriminator.
The goal of the discriminator is to provide feedback to the generator about how **realistic** the generated piano rolls are, so that the generator can learn to produce more realistic data. 
*The discriminator provides this feedback by outputting a scalar value that represents how **“real” or “fake”** a piano roll is.*
* Since the discriminator tries to classify data as “real” or “fake”, it is not very different from commonly used binary classifiers. We use a simple architecture for the critic, composed of four convolutional layers and a dense layer at the end.
<a href="url"><img src="https://github.com/RocqJones/AWS-Machine-Learning-Foundation/blob/master/imgs/discriminator.png" height="700" width="100%" ></a>

**TAKES:**
 1. Discriminators are also referred to as critics because they evaluate the input from the generator and provide feedback.
 2. discriminator's role is solely focused on determining if the input is realistic.
 3. Input noise is important because it ensures that that the generated output is varied.

#### Training Methodology.
* Training over more epochs will take longer but can lead to a better sounding musical output
* Model training is a trade-off between the number of epochs (i.e. time) and the quality of sample output.
##### Learning Rate.
The learning rate controls how rapidly the weights and biases of each network are updated during training. A higher learning rate might allow the network to explore a wider set of model weights, but might pass over more optimal weights.

##### Update ratio.
A ratio of the number of times the discriminator is updated per generator training epoch. Updating the discriminator multiple times per generator training epoch is useful because it can improve the discriminators accuracy. Changing this ratio might allow the generator to learn more quickly early-on, but will increase the overall training time.

* **Hyperparameters:** A parameter whose value is set before the training process begins.

#### Evaluation: Graphical measurements within the AWS DeepComposer console.
* **Empty bar rate:** The ratio of empty bars to total number of bars.
* **Number of pitches used:** A metric that captures the distribution and position of pitches.
* **In Scale Ratio:** Ratio of the number of notes that are in the key of C, which is a common key found in music, to the total number of notes.

#### Inference.
Once this model is trained, the generator network alone can be run to generate new accompaniments for a given input melody. 
The final process for music generation then is as follows:
* Transform single-track music input into piano roll format.
* Create a series of random numbers to represent the random noise vector.
* Pass these as input to our trained generator model, producing a series of output piano rolls. Each output piano roll represents some instrument in the composition.
* Transform the series of piano rolls back into a common music format (MIDI), assigning an instrument for each track.

#### Why Do We Need to Prepare Data?
Data often comes from many places (like a website, IoT sensors, a hard drive, or physical paper) and it’s usually not clean or in the same format. Before you can better understand your data, you need to make sure it’s in the right format to be analyzed. Thankfully, there are library packages that can help! One such library is called NumPy, which was imported into our notebook.

TAKES:
* **[Tensorflow Framework](https://www.tensorflow.org/)**
* **[Keras Library](https://keras.io/)**

#### How the Model Works
The model consists of two networks, a generator and a critic. These two networks work in a tight loop:
- The generator takes in a batch of single-track piano rolls (melody) as the input and generates a batch of multi-track piano rolls as the output by adding accompaniments to each of the input music tracks.
- The discriminator evaluates the generated music tracks and predicts how far they deviate from the real data in the training dataset.
- The feedback from the discriminator is used by the generator to help it produce more realistic music the next time.
- As the generator gets better at creating better music and fooling the discriminator, the discriminator needs to be retrained by using music tracks just generated by the generator as fake inputs and an equivalent number of songs from the original dataset as the real input.
- We alternate between training these two networks until the model converges and produces realistic music.

**The discriminator is a *binary classifier*** which means that it *classifies inputs into two groups, e.g. **“real” or “fake” data**.*

