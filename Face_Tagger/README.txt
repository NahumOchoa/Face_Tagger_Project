############################################################
#Preconditions
############################################################
1. Define the features associated with the face morphology. 
For this, you have to create a tab for each face component
to be considered (face, eyes, mouth, nose, etc.) in the file
TabInfo.xlsx

2. On each tab representing a face's component, 
you have to include its properties of interest (at least one).

3. Each property can be valued in the following ways:
  a. Multiple values, not mutually exclusive.
  b. Multiple values mutually exclusive.
4. The values of a property are separated by commas.
5. The mutual exclusivity will be determined by the values
defined in the column layout which are:
	Radio: Mutually exclusive
	Combo: Mutually exclusive
        Check: Not mutually exclusive

We suggest to use the template file TabInfoTemplate.xlsx

############################################################
#Execution
############################################################
1. Make sure to copy your customized configuration file TabInfo.xlslx
to the directory resources.
2. Make sure you have installed Python environment (3.0 or higher)
3. If it is the first time, make sure to execute the command:
   > pip install -r requirements.txt
4. Execute the following command:
   > py  __init__.py
	
