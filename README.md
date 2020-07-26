
Setting up
------------
- Install following packages in python path before executing python files

	- ***sklearn***: For K Means cluster model
	- ***numpy***: To give new shape to an array without changing its data

### Copy following files into project folder
	Color_Quantization.py: Implemented Color quantization for images
  
### Program Execution

- Program accepts comma seperated K Values as argument 

		python Color_Quantization.py 2,4,6,8,12,16  - Comma separated K value
		python Color_Quantization.py - If none provided default [4,8,12]
		

- Images used 

		python Color_Quantization.py 2,4,6,8,12,16  - Comma separated K value
		python Color_Quantization.py - If none provided default [4,8,12]
		

- Above program outputs two plots with below file names in the same project folder 
along with output txt file which records ***learning rate***, ***Number of iterations***, ***Train MSE***, ***Test MSE***

		MSE_vs_Iterations_LearningRate0.1.png
		MSE_vs_Iterations_LearningRate0.01.png
		output.txt

- Executing Gradient Descent using sklearn library

		python SkiLearn_Regression_Model.py >> output1.txt

- Above program outputs below file names in the same project folder which records ***weights caluclated***, ***Mean Squared Error***

		output1.txt
