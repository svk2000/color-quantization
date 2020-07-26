
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
		

- Images used from this URL https://personal.utdallas.edu/~axn112530/cs6375/unsupervised/images/

		image1.jpg
		image2.jpg
		image3.jpg

- Output images will get generated in **quantizedImages** folder

		Sample File Names
		------------------
		quantized_image_2_K_12.jpg
		quantized_image_1_K_2.jpg

