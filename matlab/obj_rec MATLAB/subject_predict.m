function subject_predict()  
net = alexnet;
trainsferLayer = net.Layers(1:end-3);  

imdsTrain = imageDatastore('C:\Users\CFL_Laptop2\Desktop\Robotic Hand\obj_rec MATLAB\subject_train_imgs',... 
    'includeSubfolders',true,...  
    'labelsource','foldernames','ReadFcn',@IMAGERESIZE);  
layers = [trainsferLayer;  
    fullyConnectedLayer(6,'WeightLearnRateFactor',50,'BiasLearnRateFactor',50);%??????????????????5  
    softmaxLayer();  
    classificationLayer()];  
options = trainingOptions('sgdm',...  
    'Maxepochs',5,...  
    'InitialLearnRate',0.0001, ...
    'ExecutionEnvironment','cpu');  

network = trainNetwork(imdsTrain,layers,options);  
 
camera = webcam; % Connect to the camera
nnet = network;  % Load the neural net
save('nnet')
while true   
     picture = camera.snapshot;              % Take a picture    
     picture = imresize(picture,[227,227]);  % Resize the picture 
     label = classify(nnet, picture);        % Classify the picture        
     image(picture);     % Show the picture
     title(char(label)); % Show the label
     drawnow; 
end

function output = IMAGERESIZE(input)  
input = imread(input);  
if numel(size(input)) == 2  
    input = cat(3,input,input,input);% ??3???  
end  
output = imresize(input,[227,227]);  
