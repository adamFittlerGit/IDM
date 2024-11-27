# Voltron Architecture
## Stage One: Object Detection
Yolo Object Segmentation

## Stage Two: Data Processing and Extraction 
1. Convert Labels to Polygons
2. Identify All entities Label top left to bottom right labelling/numbering to make referencing easier later (Maybe incorperate this into   YOLO labelling by forking the repo and making some changes to the labelling system)
3. Calculate Parkinsonia height using derived equation as well as pixel-meter-ratio
4. Compute Risk Distribution assuming risk probability is gaussian
5. Identify Risk Level for each risk type using std from the mean or center

## Stage Three: RAG LLM Generation (Support Conclusions with relevant documents and regulations) -- might not be fully necessary, initially we will start just with pure CV as this approach is all thats needed to solve the problem no need to over engineer
Pass gathered data to the LLM applying RAG to pass the relevant documents to the LLM to provide the most accurate justifications of its choices 


## Potential Extension 
Can we extend this to more than one image can we leverage distributed computing to perform this on the whole orthomosiac of somehow leverage yolov11 object tracking through the drone images in order to achieve this?


## Additional models
I will also be comparing the CV and Algorithmic Driven architecture with the result achieve by finetuning a multimodel model such as llava in order to see how well this can do in its image descriptions compared to that of the pure cv model.
This means there will need to be a comparative criteria I can use in order to effectively compare the results of each of the models performances.  