# Background removal 
Removed background from a photo with a person, leaving only the head in it

Ex:
| Photo                         | Mask                        | Removed                        |
| ----------------------------- | --------------------------- | ------------------------------ |
| ![Photo](./static/input.jpeg) | ![mask](./static/mask.jpeg) | ![output](./static/output.png) |


## Test task (?)
Explanations and work demonstation can be found in [Example.ipynb](https://github.com/EmpyEmpt/image-segmentation/blob/920f7ca434d642ae4f7cbb39bbfed4ecc7204315/Main.ipynb#L31)  

## Usage:
- git clone
- pip install -r requirements.txt
- python3 main.py
- send POST request to /facial-landmark-detection with 'image' parameter
- interactive web verison availible at /
- docker container availible at [dockerhub](https://hub.docker.com/repository/docker/empyempt/fbr)  

~~~bash
docker pull empyempt/fbg:latest
~~~

## Dataset: 
[Face/Head Segmentation Dataset Community Edition](https://store.mut1ny.com/product/face-head-segmentation-dataset-community-edition?v=21412759b93b)

Exact images, compressed images and .csv files can be pulled via [DVC](https://dvc.org/)
~~~bash
dvc pull
~~~

