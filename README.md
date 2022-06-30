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

Make sure to folk this repositry Zake-Ahmed/python-Project.
Go on GCP and create an account, gives you $300 of free credit.
Create firewall rules to open ports 5000 and ports 8080, making sure port 5000 is open to all id addresses.
Create VM making sure its an medium with ubuntu.
Open visual studio and open the .ssh/config file.
Create a new user with the hostname being the VM IP address.
Delete the file .ssh/known_hosts.
Run commands ssh-keygen making sure to press enter when prompted.
Run cat .ssh/id_rsa.pub, copy output and edit VM to have this ssh key.
Then connect to vm using open a remote window button, then connect to host.
once connected to the vm run both ssh-keygen and cat .ssh/id_rsa.pub like before copying the key generated.
paste key into github account under ssh and gpg keys in the settings. 
Then git clone repo on to vm using git clone <repo-ssh-link>.
Then the setup.sh file using the ./setup.sh command.
Once you VM has been updated run chmod +x jenkins.sh and ./jenkins.sh.
Then copy the inital admin password and visit the VM on port 8080, and paste admin password.
Install suggested plugins.
Create admin user,contiune with next until welcome page reached.
Run sudo visudo in VM terminal and add %jenkins ALL=(ALL:ALL) NOPASSWD:ALL under sudo user.
Visit the jenkins page and craete a new job making sure to add your github links and select the correct branch to build.
Then copy the contents of the jenkinsExecute.txt file in to the execute shell of the job.
Then save and press build now to get application up and running.
Visit the VM on port 5000 to use the application.
```

## Running the tests

Explain how to run the automated tests for this system. Break down into which tests and what they do

### Unit Tests 

Standard unit test on the DAO methods which is the back-bone of the application. It is where all the connection is happening between java and mySQL, inputing and updating the database.

```
@Test 
	public void testCreate() {
		final Item created = new Item(2L, "Car ", 1000.00D);
		assertEquals(created, DAO.create(created));
	}
```

### Integration Tests 
Mockito is used for integration testing, this is to mock the methods to test the controller is working for each object and each method called in the controller.

```

	@Mock
	private Utils utils;

	@Mock
	private ItemDAO dao;

	@InjectMocks
	private ItemController controller;
	
	@Test
	public void testCreate() {
		final String name = "watch";
		final double price = 10;
		final Item created = new Item(name, price);

		Mockito.when(utils.getString()).thenReturn(name);
		Mockito.when(utils.getDouble()).thenReturn(price);
		Mockito.when(dao.create(created)).thenReturn(created);

		assertEquals(created, controller.create());

		Mockito.verify(utils, Mockito.times(1)).getString();
		Mockito.verify(utils, Mockito.times(1)).getDouble();
		Mockito.verify(dao, Mockito.times(1)).create(created);
	}
```


## Deployment

Run maven clean package to make a new .jar file if any changes was made to the code.

## Built With

* [Maven](https://maven.apache.org/) - Dependency Management

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Chris Perrins** - *Initial work* - [christophperrins](https://github.com/christophperrins)
* **Zake Ahmed** - *Completed work* - [Zake-Ahmed](https://github.com/Zake-Ahmed)

## License

This project is licensed under the MIT license - see the [LICENSE.md](LICENSE.md) file for details 

*For help in [Choosing a license](https://choosealicense.com/)*

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
