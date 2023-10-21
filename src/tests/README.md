## The Three Parts of a Test
	1. Arrange
        This is where you set up the test. You create any objects you need, and you put them into the state you need 
        them to be in for the test to run.
	2. Act
        This is where you run the code you want to test. 
        Usually, this is just a single method call.
	3. Assert
        This is where you check the results of the code you ran in the Act section. 
        You check that the method call returned the correct value, or that it set the correct properties, or that it 
        called the correct methods on other objects, or whatever it is you are trying to test.