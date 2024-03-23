# AwakeWheel
## Inspiration
Over 7,000 Americans die every year from distracted and/or drowsy driving according to the US DOT. This is a number close to the number of drunk driving deaths annually, and it is a serious problem. Distractions pervade our everyday lives, and sometimes those short distractions can take away lives. AWakeWheel is a potential solution that isn't intrusive and can realistically keep someone's attention on the road.

## What it does
AWakeWheel is a a steering wheel with a camera, vibration sensors, and an LED built in to prevent drowsy and distracted driving. The camera sits in the center of the driving wheel and takes photos at 2-second intervals, determining whether or not the driver is beginning to become tired or distracted by something other than the road in front of them. If AWakeWheel determines that the driver is in danger aka is not aware enough of the road, then it will buzz the wheel gently and also turn on an LED to draw the driver's attention back to reality!

## How we built it
Hardware wise, it was not difficult. We took an ESP32 CAM and attached it to the center of a steering wheel. The camera analyzes if your eyes stay closed for a certain length of time (drowsy) or are not looking ahead for the majority of the time (distracted). The steering wheel has a couple of vibration sensors built in as well as a bright LED: the intention is to either wake someone up or gently remind someone to keep their eyes on the road ahead.

Software wise, this project was extremely tough yet rewarding. We used MongoDB Atlas, ReactJS, Flask, a custom machine learning model (using cascading classifiers), an ESP32 Camera, and a steering wheel to make a device that could feasibly save lives! We used two clusters on MongoDB Atlas: one was for the ESP32 CAM to store images (base64Image) and metadata and other cluster for determining which images taken in the car contained open eyes or closed eyes after running our ML model. We prepared our data from encoding base64 data to be images and then uses to pre-trained models to crop out everything other than the eyes from the images. We then tried to determine if the eyes were closed by calculating the median blur.

## Challenges we ran into
This project was extremely tough in terms of connecting the ESP32 CAM to send and receive data from MongoDB Atlas. We spent a long time getting proper requests to send, and it was tough troubleshooting if it was an issue with our hardware or if our certificates/SSL handshakes were the issue. After that, we had challenges with running the ML model quickly and displaying pictures on our website; however, we fixed a lot of our issues with multithreaded processing to actively determine if the driver's eyes were closed.

## Accomplishments that we're proud of
It was a huge accomplishment for us to make a custom ML model since none of us have done it before! We are grateful that are good datasets online to train on for people's eyes. We are super happy that we got so many different parts working together, and it was not an easy feat integrating hardware into it. Getting to see our camera populate the MongoDB database in real time and then show up on our website after being analyzed by our model was really cool!

## What we learned
We learned the difficulties and approaches to having data communication between a database and hardware. We learned how to make and train machine learning models. We also learned the power of effective teamwork and time management...the hard way!

## What's next for AWakeWheel
We really do believe that even tiny devices can make a big difference in the world. Possibly preventing thousands of deaths could be huge, and we want to make sure that our product works more seamlessly, faster, and better at detecting drowsiness/distraction and stopping it.
