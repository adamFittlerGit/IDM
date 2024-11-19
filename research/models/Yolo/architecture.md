# Voltron Architecture
## Stage One: Object Detection
Yolo Object Segmentation

## Stage Two: Data Processing and Extraction 
1. Convert Labels to Polygons
2. Identify All entities Label top left to bottom right labelling/numbering to make referencing easier later (Maybe incorperate this into   YOLO labelling by forking the repo and making some changes to the labelling system)
3. Calculate Parkinsonia height using derived equation as well as pixel-meter-ratio
4. Compute Risk Distribution assuming risk probability is gaussian
5. Identify Risk Level for each risk type using std from the mean or center

## Stage Three: RAG LLM Generation (Support Conclusions with relevant documents and regulations) -- might not be fully necessary
Pass gathered data to the LLM applying RAG to pass the relevant documents to the LLM to provide the most accurate justifications of its choices 


## Potential Extension 
Can we extend this to more than one image can we leverage distributed computing to perform this on the whole orthomosiac of somehow leverage yolov11 object tracking through the drone images in order to achieve this?
