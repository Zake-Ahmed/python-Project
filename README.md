Coverage: 100%
# python-Project

This is a project to create a bare-bones social media application. Functionality inculudes ablility to create a user,update a user, read all user and delete user. The same can be one for posts done by a user. Can also view all posts done by a particular user. 

## Getting Started

These instructions will get you a copy of the application up and running on your VM. Why the end of the you should have the application up and running on Jenkins.

### Prerequisites

What things you need to install the software and how to install them

```
Visual Studio Code - https://code.visualstudio.com/download
Java - https://qa-community.co.uk/~/_/learning/java-beginner/java--installation
gitBash - https://qa-community.co.uk/~/_/learning/git/git--git-bash#installing-git-bash
GCP Account - https://cloud.google.com

```
## Set up application on personal VM

Make sure to folk this repositry Zake-Ahmed/python-Project. \
Go on GCP and create an account, gives you $300 of free credit. \
Create firewall rules to open ports 5000 and ports 8080, making sure port 5000 is open to all id addresses. \
Create VM making sure its an medium with ubuntu. \
Open visual studio and open the ```.ssh/config file```. \
Create a new user with the hostname being the VM IP address. \
Delete the file ```.ssh/known_hosts```. \
Run commands ```ssh-keygen``` making sure to press enter when prompted. \
Run cat ```.ssh/id_rsa.pub```, copy output and edit VM to have this ssh key. \
Then connect to vm using open a remote window button, then connect to host. \
once connected to the vm run both ```ssh-keygen``` and ```cat .ssh/id_rsa.pub``` like before copying the key generated. \
paste key into github account under ssh and gpg keys in the settings. \
Then git clone repo on to vm using git clone <repo-ssh-link>. \
Then the setup.sh file using the ```./setup.sh``` command. \
Once you VM has been updated run ```chmod +x jenkins.sh``` and ```./jenkins.sh```. \
Then copy the inital admin password and visit the VM on port 8080, and paste admin password. \
Install suggested plugins. \
Create admin user,contiune with next until welcome page reached. \
Run sudo visudo in VM terminal and add ```%jenkins ALL=(ALL:ALL) NOPASSWD:ALL``` under sudo user. \
Visit the jenkins page and craete a new job making sure to add your github links and select the correct branch to build. \
Then copy the contents of the ```jenkinsExecute.txt``` file in to the execute shell of the job. \
Then save and press build now to get application up and running. \
Visit the VM on port 5000 to use the application.


## Running the tests
Jenkins will auto run the tests using the command
```
python3 -m pytest --cov-report term-missing --cov application/ tests/

```

### Unit Tests 

Standard unit test on the html page testing if a GET request is made.

```
class TestViews(TestBase):
    def test_about_get(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is the About Page', response.data)
```

### Integration Tests 
The Intergration Tests are testing the intergration of the database on top of the application. When adding a Post of example this method will test if the new post is added to the database or not and is it viewable on the webpage as well.


```
class TestAdd(TestBase):
    def test_add_user(self):

        response = self.client.post(
            url_for('addUser'),
            data = dict(userName="abc",firstName="abc",lastName="abc")
        )
        assert len(Users.query.all()) == 3
        assert Users.query.filter_by(userName="abc").first().id ==3
    
    def test_add_post(self):

        response = self.client.post(
            url_for('add'),
            data = dict(message="abc",userID=1)
        )
        assert len(Posts.query.all()) == 3
        assert Posts.query.filter_by(message="abc").first().id ==3
```
## Built With

* [Jenkins](https://www.jenkins.io) - CI Server

## Authors

* **Zake Ahmed** - *Completed work* - [Zake-Ahmed](https://github.com/Zake-Ahmed)

## License

This project is licensed under the MIT license - see the [LICENSE.md](LICENSE.md) file for details 

*For help in [Choosing a license](https://choosealicense.com/)*

## Acknowledgments

* ME
* MYSELF
* I
