microAI_Outupt_Network contains one class: mAI_N.

Before this class can be used, first double check that the route table in the directory being used is correct.

mAI_N(group=’1’) objects are initialized with 1 parameter. This parameter is group number and should contain a string of the group number corresponding to the channels in the route table within the Y subdirectory the user wishes to see. If no group number is provided, the default string of '1' is used.   

mAI has 5 public methods:

getInputValues() will return an array of floats of the values entered into MicroAI.   

getUpperBounds() will return an array of floats of the calculated acceptable upper bounds of each value given to MicroAI.  

getLowerBounds() will return an array of floats of the calculated acceptable lower bounds of each value given to MicroAI.  

isAbnormal()  will return an array of the integers 1 and 0. A value of 1 indicates that channel is currently experiencing abnormal behavior. A value of 0 indicates normal behavior.  

AbnormalRatio()  will return a float of the percentage of channels that are currently behaving abnormally.  
